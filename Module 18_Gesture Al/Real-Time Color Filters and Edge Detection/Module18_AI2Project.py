import cv2

def apply_filter(frame, filter_type):
    result = frame.copy()

    if filter_type == "grayscale":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    elif filter_type == "blur":
        result = cv2.GaussianBlur(frame, (15, 15), 0)

    elif filter_type == "edges":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        result = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    elif filter_type == "warm_amber":
        result[:, :, 2] = cv2.multiply(result[:, :, 2], 1.3)
        result[:, :, 0] = cv2.multiply(result[:, :, 0], 0.6)

    elif filter_type == "cool_cyan":
        result[:, :, 0] = cv2.multiply(result[:, :, 0], 1.3)
        result[:, :, 1] = cv2.multiply(result[:, :, 1], 1.2)
        result[:, :, 2] = cv2.multiply(result[:, :, 2], 0.7)

    return result

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

filter_type = "original"
photo_count = 0  # Counter for saved snapshots

print("--- WEB-CAM STUDIO CONTROLS ---")
print("o - Original Feed")
print("g - Grayscale")
print("b - Blur")
print("e - Edge Detection")
print("a - Warm Amber Tint")
print("c - Cool Cyan Tint")
print("s - Take Snapshot")
print("q - Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    filtered_frame = apply_filter(frame, filter_type)

    combined_view = cv2.hconcat([frame, filtered_frame])

    cv2.imshow("Webcam Studio", combined_view)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('o'):
        filter_type = "original"
    elif key == ord('g'):
        filter_type = "grayscale"
    elif key == ord('b'):
        filter_type = "blur"
    elif key == ord('e'):
        filter_type = "edges"
    elif key == ord('a'):
        filter_type = "warm_amber"
    elif key == ord('c'):
        filter_type = "cool_cyan"
    elif key == ord('s'):
        photo_count += 1
        filename = f"snapshot_{filter_type}_{photo_count}.jpg"
        cv2.imwrite(filename, filtered_frame)
        print(f"Saved snapshot: {filename}")

cap.release()
cv2.destroyAllWindows()