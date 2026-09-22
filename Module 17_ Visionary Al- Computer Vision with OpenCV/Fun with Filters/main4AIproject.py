import cv2
import numpy as np
import os
import re

image = cv2.imread("78d8d060-21ce-11f0-89a9-cb5ed9bbefd9.jpg.webp")

if image is None:
    print("Error: Image not found in the system")
    exit()

image = cv2.resize(image, (200, 200))

original = image.copy()

red_intensity = 50
green_intensity = 50
blue_intensity = 50


def apply_red(img, intensity):

    red = img.copy()

    red[:, :, 2] = np.clip(
        red[:, :, 2].astype(int) + intensity,
        0,
        255
    )

    return red


def apply_blue(img, intensity):

    blue = img.copy()

    blue[:, :, 0] = np.clip(
        blue[:, :, 0].astype(int) + intensity,
        0,
        255
    )

    return blue


def apply_green(img, intensity):

    green = img.copy()

    green[:, :, 1] = np.clip(
        green[:, :, 1].astype(int) + intensity,
        0,
        255
    )

    return green


def apply_original(img):
    return img.copy()


while True:

    cv2.imshow("Interactive Filters", image)

    key = cv2.waitKey(0) & 0xFF

    if key == ord('r'):
        image = apply_red(image, red_intensity)

    elif key == ord('g'):
        image = apply_green(image, green_intensity)

    elif key == ord('b'):
        image = apply_blue(image, blue_intensity)

    elif key == ord('t'):
        red_intensity = min(255, red_intensity + 10)
        print("Red intensity:", red_intensity)
        image = apply_red(original, red_intensity)

    elif key == ord('d'):
        blue_intensity = max(0, blue_intensity - 10)
        print("Blue intensity:", blue_intensity)
        image = apply_blue(original, blue_intensity)

    elif key == ord('u'):
        green_intensity = min(255, green_intensity + 10)
        print("Green intensity:", green_intensity)
        image = apply_green(original, green_intensity)

    elif key == ord('j'):
        red_intensity = max(0, red_intensity - 10)
        print("Red intensity:", red_intensity)
        image = apply_red(original, red_intensity)

    elif key == ord('q'):
        break


cv2.destroyAllWindows()