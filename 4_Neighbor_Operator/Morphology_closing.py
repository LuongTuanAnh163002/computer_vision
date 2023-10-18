import cv2
import numpy as np

#Morphology closing = erode(dilate(source))
if __name__ == "__main__":
    img = cv2.imread("anh_data/morphology_close.png")
    kernels = np.ones((5, 5), dtype = np.uint8)
    dst1 = cv2.dilate(img, kernel = kernels, iterations = 1)
    dst2 = cv2.erode(dst1, kernel = kernels, iterations = 1)
    cv2.imshow("Original", img)
    cv2.imshow("After", dst2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #-----------Cách 2 sử dụng trực tiếp hàm trong opencv---------
    # kernel = np.ones((5, 5), dtype = np.uint8)
    # dst = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("Original", img)
    # cv2.imshow("window", dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()