import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("image.png")
    h, w = img.shape[0:2]
    #Xoay 1 góc 45 độ quanh tâm của ảnh cùng chiều kim đồng hồ
    matrix_rotation = cv2.getRotationMatrix2D((int(w / 2), int(h / 2)), 45, scale = 1)
    rotate = cv2.warpAffine(img, matrix_rotation, (w, h))
    cv2.imshow("Before rotation", img)
    cv2.imshow("After rotation", rotate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()