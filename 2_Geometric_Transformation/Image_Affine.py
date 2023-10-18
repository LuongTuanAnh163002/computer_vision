import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    img = cv2.imread("anh_data/image.png")
    h, w = img.shape[:2]
    psi = np.float32([[50, 50], [80, 50], [50, 80]]) #Chọn 3 điểm bất kỳ trên ảnh để Affine
    pso = np.float32([[50, 100], [80, 100], [100, 120]]) #Vị trí của 3 điểm ảnh sau khi Affine
    M = cv2.getAffineTransform(psi, pso)
    affine = cv2.warpAffine(img, M, (w, h))

    #----------Show ảnh bằng opencv--------------------
    # cv2.imshow("Original", img)
    # cv2.imshow("Affine", affine)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #----------Show ảnh bằng matplotlib----------------
    plt.subplot(121)
    plt.imshow(img)
    plt.title('Input')
    for (x, y) in psi:
        plt.scatter(x, y, s=50, c='green', marker='x')

    plt.subplot(122)
    plt.imshow(affine)
    plt.title('Output')
    for (x, y) in pso:
        plt.scatter(x, y, s=50, c='green', marker='x')
    plt.show()