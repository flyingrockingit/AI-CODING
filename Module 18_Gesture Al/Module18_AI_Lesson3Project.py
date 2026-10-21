import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

shape_x, shape_y, shape_size = 200, 200, 50

SMOOTH_ALPHA = 0.2  

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    hand_detected = False

    if contours:
        max_contour = max(contours, key=cv2.contourArea)  # Get largest contour
        
        if cv2.contourArea(max_contour) > 1000:  # Increased threshold slightly to prevent tracking noise
            hand_detected = True
            
            x, y, w, h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            target_x = int(x + w / 2)
            target_y = int(y + h / 2)
            cv2.circle(frame, (target_x, target_y), 5, (0, 0, 255), -1)  # Red dot at center

            tracking_error = int(((target_x - shape_x)**2 + (target_y - shape_y)**2)**0.5)

            shape_x = int(shape_x + SMOOTH_ALPHA * (target_x - shape_x))
            shape_y = int(shape_y + SMOOTH_ALPHA * (target_y - shape_y))

    cv2.rectangle(frame, (10, 10), (310, 130), (0, 0, 0), -1) 
    
    hand_x_str = target_x if hand_detected else 'N/A'
    hand_y_str = target_y if hand_detected else 'N/A'
    cv2.putText(frame, f"Hand Center:  X:{hand_x_str}, Y:{hand_y_str}", 
                (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    cv2.putText(frame, f"Circle Pos:   X:{shape_x}, Y:{shape_y}", 
                (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    
    lag_val = tracking_error if hand_detected else 0
    error_color = (0, 255, 255) if lag_val > 30 else (0, 255, 0)
    cv2.putText(frame, f"Catch-up Lag: {lag_val} px", 
                (20, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.5, error_color, 1)

    if hand_detected:
        cv2.putText(frame, "STATUS: TRACKING ACTIVE", (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # Draw a yellow line showing the mechanical pulling force of the smoothing algorithm
        cv2.line(frame, (target_x, target_y), (shape_x, shape_y), (0, 255, 255), 2)
    else:
        cv2.putText(frame, "STATUS: HAND LOST", (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.circle(frame, (shape_x, shape_y), shape_size, (255, 0, 0), -1)  # Blue circle

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Filtered Frame", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
