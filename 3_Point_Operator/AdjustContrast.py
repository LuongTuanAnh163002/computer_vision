import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("image.png")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equa = cv2.equalizeHist(img_gray)
    img_merge = np.hstack((img_gray, equa))
    cv2.imshow("before-after", img_merge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()