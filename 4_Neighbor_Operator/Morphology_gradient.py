import cv2
import numpy as np

#Morphology gradient = dilate(sourse) - erode(source)
if __name__ == "__main__":
    img = cv2.imread("anh_data/morphology_gradient.png")
    kernels = np.ones((5, 5), dtype = np.uint8)
    src1 = cv2.dilate(img, kernel = kernels, iterations = 1)
    src2 = cv2.erode(img, kernel = kernels, iterations = 1)
    rs = cv2.addWeighted(src1, 1, src2, -1, 0)
    cv2.imshow("Original", img)
    cv2.imshow("After", rs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #-----Cách 2 sử dụng hàm trực tiếp từ opencv--------
    # kernel = np.ones((5, 5), dtype = np.uint8)
    # dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    # cv2.imshow("Original", img)
    # cv2.imshow("After", dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()