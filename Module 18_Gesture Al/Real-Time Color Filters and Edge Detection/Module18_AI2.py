import cv2
import numpy as np

def apply_filter(image, ftype):
    img = image.copy()
    if ftype == "red tint":
        img[:, :, 0] = 0  # Remove Blue
        img[:, :, 1] = 0  # Remove Green
    elif ftype == "green tint":
        img[:, :, 0] = 0  # Remove Blue
        img[:, :, 2] = 0  # Remove Red
    elif ftype == "blue tint":
        img[:, :, 1] = 0  # Remove Green
        img[:, :, 2] = 0  # Remove Red
    elif ftype == "canny_tint":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.Canny(gray, 100, 200)
        
    return img

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    filter_type = "original"

    print("--- KEY CONTROLS ---")
    print("Press 'r' for Red Tint")
    print("Press 'g' for Green Tint")
    print("Press 'b' for Blue Tint")
    print("Press 'c' for Canny Edge Detection")
    print("Press 'o' for Original Video")
    print("Press 'q' to Quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video stream ended or frame failed to load.")
            break

        filtered_frame = apply_filter(frame, filter_type)

        cv2.imshow("Video Filter", filtered_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        elif key == ord('r'):
            filter_type = "red tint"
        elif key == ord('g'):
            filter_type = "green tint"
        elif key == ord('b'):
            filter_type = "blue tint"
        elif key == ord('c'):
            filter_type = "canny_tint"
        elif key == ord('o'):
            filter_type = "original"

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()