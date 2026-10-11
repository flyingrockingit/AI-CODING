import cv2, time, numpy as np
import mediapipe as mp

H = mp.solutions.hands

TIP = H.HandLandmark

ids = {
    "thumb": TIP.THUMB_TIP,
    "index": TIP.INDEX_FINGER_TIP,
    "middle": TIP.MIDDLE_FINGER_TIP,
    "ring": TIP.RING_FINGER_TIP,
    "pinky": TIP.PINKY_TIP,
}

hands = H.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

draw = mp.solutions.drawing_utils

pairs = {
    "middle": ("SEPIA", "NEGATIVE"),
    "ring": ("GLITCH", "EDGE")
}

st = {k: 0 for k in pairs}

cur = "SEPIA"

DEB, CAP, TT, TP = 0.6, 1.2, 30, 20

la = lc = 0

pinch_on, paused = False, False

freeze = None

MAIN, POP = "Gesture-Controlled Photo App", "Captured"

SEPIA_M = np.array([
    [0.272, 0.534, 0.131],
    [0.349, 0.686, 0.168],
    [0.393, 0.769, 0.189]
])


def apply(img, t):

    if t == "SEPIA":
        return np.clip(cv2.transform(img, SEPIA_M), 0, 255).astype(np.uint8)

    if t == "NEGATIVE":
        return cv2.bitwise_not(img)

    if t == "EDGE":
        return cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 80, 160)

    if t == "GLITCH":
        h, w = img.shape[:2]
        r, g, b = img[:, :, 2], img[:, :, 1], img[:, :, 0]

        return cv2.merge([
            np.roll(b, -int(0.02 * w), 1),
            g,
            np.roll(r, int(0.04 * w), 1)
        ])

    return img


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

cv2.namedWindow(MAIN, cv2.WINDOW_NORMAL)

while True:

    if paused:
        cv2.imshow(MAIN, freeze)

        k = cv2.waitKey(50) & 0xFF

        if k == ord("q"):
            break

        if k == 27:
            paused, pinch_on = False, False

            try:
                cv2.destroyWindow(POP)
            except:
                pass

            continue

    ok, img = cap.read()

    if not ok:
        break

    img = cv2.flip(img, 1)

    h, w = img.shape[:2]

    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    now = time.time()

    capture = False

    if res.multi_hand_landmarks:

        hand = res.multi_hand_landmarks[0]

        draw.draw_landmarks(img, hand, H.HAND_CONNECTIONS)

        lm = hand.landmark

        tips = {
            k: (int(lm[v].x * w), int(lm[v].y * h))
            for k, v in ids.items()
        }

        tx, ty = tips["thumb"]

        ix, iy = tips["index"]

        pinch = abs(tx - ix) < TP and abs(ty - iy) < TP

        if pinch and not pinch_on and now - lc > CAP:
            pinch_on, capture, lc = True, True, now

        if not pinch and pinch_on:
            pinch_on = False

        if not pinch:
            t = next(
                (k for k in pairs
                 if abs(tx - tips[k][0]) < TT
                 and abs(ty - tips[k][1]) < TT),
                None
            )

            if t and now - la > DEB:
                cur = pairs[t][st[t]]
                st[t] ^= 1
                la = now
                print("Filter:", cur)

    out = apply(img, cur)

    if cur == "EDGE":
        out = cv2.cvtColor(out, cv2.COLOR_GRAY2BGR)

    if capture:
        name = f"picture_{int(now)}.jpg"
        cv2.imwrite(name, out)
        print("Saved:", name)
        paused, freeze = True, out.copy()
        cv2.imshow(POP, freeze)

    cv2.imshow(MAIN, out)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()