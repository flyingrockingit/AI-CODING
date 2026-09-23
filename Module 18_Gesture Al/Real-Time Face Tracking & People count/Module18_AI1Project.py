import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open the camera.")
    exit()

emotion = "Detecting..."
frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read the camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    frame_count += 1

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 0, 0),
            4
        )

        face = frame[y:y+h, x:x+w]
        if frame_count % 30 == 0:

            try:
                result = DeepFace.analyze(
                    face,
                    actions=["emotion"],
                    enforce_detection=False
                )

                emotion = result[0]["dominant_emotion"]

            except Exception:
                emotion = "Detecting..."

        cv2.putText(
            frame,
            "Emotion: " + emotion,
            (x, y - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (255, 255, 255),
            3
        )

    cv2.imshow("Real-Time Face and Emotion Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()