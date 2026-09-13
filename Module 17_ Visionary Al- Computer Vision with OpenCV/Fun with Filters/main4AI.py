import cv2
import numpy as np

img = cv2.imread('me.jpg')
image = cv2.resize(img, (200, 200))


def apply_red(img):
    red = img.copy()
    red[:, :, 0] = 0
    red[:, :, 1] = 0
    return red


def apply_blue(img):
    blue = img.copy()
    blue[:, :, 2] = 0
    blue[:, :, 1] = 0
    return blue


def apply_green(img):
    green = img.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    return green


def apply_magenta(img):
    magenta = img.copy()
    magenta[:, :, 1] = 0
    return magenta


def apply_yellow(img):
    yellow = img.copy()
    yellow[:, :, 0] = 0
    return yellow


def apply_gaussian(img):
    return cv2.GaussianBlur(img, (15, 15), 0)


def apply_original(img):
    return img.copy()


print("Press keys to apply filters:")
print("r - Red filter")
print("g - Green filter")
print("b - Blue filter")
print("m - Magenta filter")
print("y - Yellow filter")
print("a - Gaussian blur")
print("o - Original image")
print("q - Quit")

cv2.imshow("Filtered image", image)

while True:
    key = cv2.waitKey(0) & 0xFF
    if key == ord('r'):
        filtered = apply_red(image)

    elif key == ord('g'):
        filtered = apply_green(image)

    elif key == ord('b'):
        filtered = apply_blue(image)

    elif key == ord('m'):
        filtered = apply_magenta(image)

    elif key == ord('y'):
        filtered = apply_yellow(image)

    elif key == ord('a'):
        filtered = apply_gaussian(image)

    elif key == ord('o'):
        filtered = apply_original(image)

    elif key == ord('q'):
        break

    else:
        continue
    cv2.imshow("Filtered image", filtered)

cv2.destroyAllWindows()