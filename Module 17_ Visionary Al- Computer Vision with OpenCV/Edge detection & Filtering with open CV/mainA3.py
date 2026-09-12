import cv2
import numpy as np
import matplotlib.pyplot as plt


def show(title, img, gray=False):
    plt.figure(figsize=(6, 6))

    if gray:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    plt.title(title)
    plt.axis('off')
    plt.show()


def interactive_edges(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found in the server")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    show("Grayscale", gray, gray=True)

    menu = {
        "1": "Sobel",
        "2": "Canny",
        "3": "Laplacian",
        "4": "Exit"
    }
    while True:
        print("\nOptions")

        for k, v in menu.items():
            print(f"{k}. {v}")
        choice = input("Enter your preferred choice: ")

        if choice == "1":
            sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, 3)
            sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, 3)
            sobel = cv2.bitwise_or(sx.astype(np.uint8),sy.astype(np.uint8))
            show("Sobel Edge Detection", sobel, gray=True)

        elif choice == "2":
            edges = cv2.Canny(gray, 100, 200)
            show("Canny", edges, gray=True)

        elif choice == "3":
            lap = cv2.Laplacian(gray, cv2.CV_64F)
            show("Laplacian",np.abs(lap).astype(np.uint8),gray=True)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

interactive_edges("EYES.jpg")