import cv2

image = cv2.imread("closeup-shot-beautiful-butterfly-with-interesting-textures-orange-petaled-flower.jpg")

#Resize the image into three different sizes

small_image = cv2.resize(image,(200,200))

medium_image = cv2.resize(image,(400,400))

large_image = cv2.resize(image,(600,600))

cv2.imshow("Small Image - 200x200",small_image)

cv2.imshow("Medium Image - 400x400",medium_image)

cv2.imshow("Large Image - 600x600",large_image)

cv2.imwrite("input_image_small.jpg", small_image)

cv2.imwrite("input_image_medium.jpg", medium_image)

cv2.imwrite("input_image_large.jpg", large_image)

cv2.waitKey(0)

cv2.destroyAllWindows()