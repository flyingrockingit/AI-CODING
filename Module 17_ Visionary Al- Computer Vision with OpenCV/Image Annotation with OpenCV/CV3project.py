import cv2

img = cv2.imread('roses.png')
image = cv2.resize(img, (200, 400))

height, width = image.shape[:2]
middle_y = height // 2

cv2.arrowedLine(
    image,
    (10, middle_y),
    (width // 2 - 10, middle_y),
    (0, 255, 0),
    2,
    tipLength=0.05
)
cv2.arrowedLine(
    image,
    (width - 10, middle_y),
    (width // 2 + 10, middle_y),
    (0, 255, 0),
    2,
    tipLength=0.05
)

cv2.putText(
    image,
    f"Width: {width} pixels",
    (10, middle_y - 20),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (0, 255, 0),
    1
)

cv2.imshow("Image Width", image)
cv2.waitKey(0)
cv2.destroyAllWindows()