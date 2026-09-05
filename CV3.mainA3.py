import cv2
import numpy as np

image=cv2.imread('Jemifinal.jpg')
height, width,_ = image.shape

#image = np.zeros((height, width, 3), dtype=np.uint8)

center_coord = (width // 2, height // 2)

radius = 85

cv2.circle(image, center_coord, radius, (0, 255, 0), 3)

top_left = (50, 50)

bottom_right = (200, 200)

cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 3)

cv2.line(image, (0, 0), (width - 1, height - 1), (0, 0, 255), 2)

text = "This is a picture of crazy coding"

org = (50, height - 50)

cv2.putText(
    image,
    text,
    org,
    cv2.FONT_HERSHEY_DUPLEX,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

cv2.imshow("Annotated image shown", image)

cv2.waitKey(0)

cv2.destroyAllWindows()