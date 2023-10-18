import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("anh_data/image.png")
    h, w = img.shape[0:2]
    tx = 100
    ty = 100
    matrix_translation = np.array([[1, 0, tx], [0, 1, ty]], dtype = np.float32)
    translation = cv2.warpAffine(img, matrix_translation, (w, h))
    cv2.imshow("Before translation", img)
    cv2.imshow("After translation", translation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()