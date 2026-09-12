import cv2
import matplotlib.pyplot as plt


image = cv2.imread("YOUR_IMAGE.jpg")

img_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("Original image")
plt.show()

(h, w) = image.shape[:2]

center = (w // 2, h // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

rotated_image = cv2.warpAffine(
    image,
    rotation_matrix,
    (w, h)
)

rotated_rgb = cv2.cvtColor(
    rotated_image,
    cv2.COLOR_BGR2RGB
)

plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

brightened_image = cv2.convertScaleAbs(
    rotated_image,
    alpha=1.2,
    beta=40
)

brightened_rgb = cv2.cvtColor(
    brightened_image,
    cv2.COLOR_BGR2RGB
)

plt.imshow(brightened_rgb)
plt.title("Brightened Image")
plt.show()

height, width = brightened_image.shape [:2]

cropped_image = brightened_image[
    50:height-50,
    50:width-50
]

cropped_rgb = cv2.cvtColor(
    cropped_image,
    cv2.COLOR_BGR2RGB
)

plt.imshow(cropped_rgb)
plt.title("Cropped Image")
plt.show()

gray_image = cv2.cvtColor(
    cropped_image,
    cv2.COLOR_BGR2GRAY
)

plt.imshow(gray_image, cmap="gray")
plt.title("Black and White Image")
plt.show()

blurred_image = cv2.GaussianBlur(
    cropped_image,
    (15, 15),
    0
)

blurred_rgb = cv2.cvtColor(
    blurred_image,
    cv2.COLOR_BGR2RGB
)

plt.imshow(blurred_rgb)
plt.title("Blurred Image")
plt.show()

sharpened_image = cv2.detailEnhance(
    cropped_image,
    sigma_s=10,
    sigma_r=0.15
)

sharpened_rgb = cv2.cvtColor(
    sharpened_image,
    cv2.COLOR_BGR2RGB
)

plt.imshow(sharpened_rgb)
plt.title("Sharpened Image")
plt.show()

cv2.imwrite("rotated_image.jpg", rotated_image)
cv2.imwrite("brightened_image.jpg", brightened_image)
cv2.imwrite("cropped_image.jpg", cropped_image)
cv2.imwrite("black_white_image.jpg", gray_image)
cv2.imwrite("blurred_image.jpg", blurred_image)
cv2.imwrite("sharpened_image.jpg", sharpened_image)
