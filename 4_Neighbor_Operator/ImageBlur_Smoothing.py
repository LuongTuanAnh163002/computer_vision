import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("anh_data/image.png")

    #Làm mờ ảnh sử dụng phương pháp Mean với kernel có shape (5, 5)
    img_mean = cv2.blur(img, (5, 5))

    #Làm mờ ảnh sử dụng phương pháp Gaussian với kernel có shape (5, 5)
    img_gaussian = cv2.GaussianBlur(img, (5, 5), 0)

    #Làm mờ ảnh sử dụng phương pháp Median với kernel có shape (5, 5)
    img_median = cv2.medianBlur(img, 5)

    cv2.imshow("Bluring image Mean", img_mean)
    cv2.imshow("Bluring image Gaussian", img_gaussian)
    cv2.imshow("Bluring image Median", img_median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()