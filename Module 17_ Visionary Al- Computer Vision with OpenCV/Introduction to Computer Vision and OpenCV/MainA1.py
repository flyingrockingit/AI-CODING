import cv2

image = cv2.imread("IWCT.jpg")
resized_image = cv2.resize(image, (800, 500))

cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded Image", 800, 500)

cv2.imshow("Loaded Image", resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()