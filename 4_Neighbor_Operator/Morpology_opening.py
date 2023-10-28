import cv2
import numpy as np

#Morphology opening = dilate(erode(source))
if __name__ == "__main__":
    img = cv2.imread("morphology_open.png")
    kernels = np.ones((5, 5), dtype = np.uint8)
    dst1 = cv2.erode(img, kernel = kernels, iterations = 1)
    dst2 = cv2.dilate(dst1, kernel = kernels, iterations = 1)
    cv2.imshow("Original", img)
    cv2.imshow("After", dst2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #------Cách số 2 sử dụng trực tiếp hàm của opencv------
    # kernel = np.ones((5, 5), dtype = np.uint8)
    # dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    # cv2.imshow("Original", img)
    # cv2.imshow("window", dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()