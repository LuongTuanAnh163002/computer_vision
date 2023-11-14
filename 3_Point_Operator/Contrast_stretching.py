import numpy as np
import cv2


def contrast_stretching(img):
    min_val = np.min(img)
    max_val = np.max(img)
    matric = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            matric[i, j] = int(((img[i, j] - min_val) / (max_val - min_val)) * (255 - 1))
    matric = matric.astype(np.uint8)
    return matric

if __name__ == "__main__":
    img = cv2.imread("image.png")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_contraster = contrast_stretching(img_gray)
    cv2.imshow("before", img_gray)
    cv2.imshow("after", img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()