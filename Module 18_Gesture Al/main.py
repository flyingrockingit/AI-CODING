import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

Hands = mp.solutions.hands
hands = Hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
draw = mp.solutions.drawing_utils

TH, IX = Hands.HandLandmark.THUMB_TIP, Hands.HandLandmark.INDEX_FINGER_TIP

try:
    dev = AudioUtilities.GetDefaultOutputDevice() if hasattr(AudioUtilities, "GetDefaultOutputDevice") else AudioUtilities.GetSpeakers()
    volctl = dev.EndpointVolume.QueryInterface(IAudioEndpointVolume)
    minv, maxv = volctl.GetVolumeRange()[:2]
except Exception as e:
    print(f"Pycaw error: {e}")
    exit()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not accessible.")
    exit()

WIN = "Hand Gesture System Control"
cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)

smoothed_vol = 50.0
smoothed_bright = 50.0
alpha = 0.15 

last_set_vol = -1
last_set_bright = -1

while True:
    ok, image = cap.read()
    if not ok:
        break

    img = cv2.flip(image, 1)
    h, w = img.shape[:2]

    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks and res.multi_handedness:
        for i, hand in enumerate(res.multi_hand_landmarks):
            label = res.multi_handedness[i].classification[0].label
            draw.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS)

            lm = hand.landmark
            tp = (int(lm[TH].x * w), int(lm[TH].y * h))
            ip = (int(lm[IX].x * w), int(lm[IX].y * h))

            # Pinch distance & hand scaling
            dist = float(np.hypot(ip[0] - tp[0], ip[1] - tp[1]))
            wrist = (int(lm[0].x * w), int(lm[0].y * h))
            mcp = (int(lm[9].x * w), int(lm[9].y * h))
            hand_size = np.hypot(mcp[0] - wrist[0], mcp[1] - wrist[1])
            
            norm_dist = dist / (hand_size + 1e-6)

            # Visual feedback on pinch points
            circle_color = (0, 0, 255) if norm_dist < 0.2 else (0, 255, 0)
            cv2.circle(img, tp, 10, circle_color, cv2.FILLED)
            cv2.circle(img, ip, 10, circle_color, cv2.FILLED)
            cv2.line(img, tp, ip, circle_color, 3)

            # LEFT HAND -> Volume Control
            if label == "Left":
                raw_vol_pct = np.interp(norm_dist, [0.15, 0.8], [0, 100])
                
                # Apply exponential smoothing
                smoothed_vol = (alpha * raw_vol_pct) + ((1 - alpha) * smoothed_vol)
                target_vol = int(smoothed_vol)

                # Convert target percentage to system decibels
                v = np.interp(target_vol, [0, 100], [minv, maxv])

                # Only issue OS call if changed by at least 1%
                if abs(target_vol - last_set_vol) >= 1:
                    try:
                        volctl.SetMasterVolumeLevel(v, None)
                        last_set_vol = target_vol
                    except Exception:
                        pass

                bar = int(np.interp(target_vol, [0, 100], [400, 150]))

                # Volume UI Bar
                cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)
                cv2.rectangle(img, (50, bar), (85, 400), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, f"Vol: {target_vol}%", (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

            # RIGHT HAND -> Brightness Control
            elif label == "Right":
                raw_bright_pct = np.interp(norm_dist, [0.15, 0.8], [0, 100])
                
                # Apply exponential smoothing
                smoothed_bright = (alpha * raw_bright_pct) + ((1 - alpha) * smoothed_bright)
                target_bright = int(smoothed_bright)

                # Only issue OS call if changed by at least 1%
                if abs(target_bright - last_set_bright) >= 1:
                    try:
                        sbc.set_brightness(target_bright)
                        last_set_bright = target_bright
                    except Exception:
                        pass

                bar = int(np.interp(target_bright, [0, 100], [400, 150]))
                x1, x2 = w - 85, w - 50

                # Brightness UI Bar
                cv2.rectangle(img, (x1, 150), (x2, 400), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, bar), (x2, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f"Bright: {target_bright}%", (w - 150, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow(WIN, img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
hands.close()
cv2.destroyAllWindows()