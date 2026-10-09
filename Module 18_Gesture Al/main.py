import math
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

print("Hand tracking started, press 'q' to quit")


def detect_gesture(hand_landmarks):
    landmarks = hand_landmarks.landmark

    tip_ids = [4, 8, 12, 16, 20]
    pip_ids = [2, 6, 10, 14, 18]

    # extended = [Thumb, Index, Middle, Ring, Pinky]
    extended = [False] * 5

    # 1. Thumb Check (x-axis distance)
    if abs(landmarks[tip_ids[0]].x - landmarks[pip_ids[0]].x) > 0.04:
        extended[0] = True

    # 2. Four Fingers Check (y-axis comparison)
    for i in range(1, 5):
        if landmarks[tip_ids[i]].y < landmarks[pip_ids[i]].y:
            extended[i] = True

    # Calculate distance for Pinching / Snap / OK
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    pinch_dist = math.hypot(thumb_tip.x - index_tip.x, thumb_tip.y - index_tip.y)

    # --- Single Hand Gestures from Image ---

    # Pinching / Snap (Thumb and Index tips touching)
    if pinch_dist < 0.05:
        return "Pinching / Snap"

    # Call Me / Shaka (Thumb and Pinky extended)
    elif extended[0] and not extended[1] and not extended[2] and not extended[3] and extended[4]:
        return "Call Me / Shaka"

    # I Love You / Finger Gun / Rock (Thumb, Index, Pinky extended)
    elif extended[0] and extended[1] and not extended[2] and not extended[3] and extended[4]:
        return "I Love You"

    # Gun / Pointing (Index extended, Thumb open)
    elif extended[0] and extended[1] and not extended[2] and not extended[3] and not extended[4]:
        return "Gun"

    # Point / No (Only Index finger extended)
    elif not extended[0] and extended[1] and not extended[2] and not extended[3] and not extended[4]:
        return "Point"

    # Peace / Counting 2 (Index and Middle extended)
    elif extended[1] and extended[2] and not extended[3] and not extended[4]:
        return "Peace"

    # Counting 3 (Index, Middle, Ring extended)
    elif not extended[0] and extended[1] and extended[2] and extended[3] and not extended[4]:
        return "Counting"

    # Thumbs Up / Thumbs Down (Only Thumb extended)
    elif extended[0] and not extended[1] and not extended[2] and not extended[3] and not extended[4]:
        if landmarks[4].y < landmarks[0].y:
            return "Thumbs Up"
        else:
            return "Thumbs Down"

    # Wave / High Five / Stop / Open Hand (All 5 fingers extended)
    elif extended.count(True) >= 4:
        return "Wave / High Five / Stop"

    # Fist (All fingers folded down)
    elif extended.count(True) == 0:
        return "Fist"

    else:
        return "Custom Gesture"


while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)  # Mirror view
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    gesture = "No Hand Detected"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            gesture = detect_gesture(hand_landmarks)

    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (0, 255, 0),
        2
    )

    cv2.imshow("Gesture Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
hands.close()
cv2.destroyAllWindows()