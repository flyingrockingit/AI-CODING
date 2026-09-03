import cv2
import matplotlib.pyplot as plt
image=cv2.imread('Yellow_sunflower.jpg')
img_rgb=cv2.cvtColor (image,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('RGB image')
plt.show()


gray_img=cv2.cvtColor (img_rgb,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img)
plt.title('BGR image')
plt.show()

Cropped_img=image[100:300,200:400]
cropped_rgb=cv2.cvtColor(Cropped_img,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title('cropped image')
plt.show()

(h,w)=image.shape[:2]
center = (w//2 , h//2)
rotation_matrix=cv2.getRotationMatrix2D(center, 45,1.0)
rotate_img=cv2.warpAffine(image,rotation_matrix,(w,h))
rotated_rgb= cv2.cvtColor(rotate_img,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title('rotated image')
plt.show()