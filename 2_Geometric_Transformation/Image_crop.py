import numpy as np
import cv2
img = cv2.imread('image.png')
cropped_img = img[100:250, 100:250, :]
# print(img.shape)

cv2.imshow("crop", cropped_img)
cv2.imshow("origin", img)
cv2.waitKey(0)
cv2.destroyAllWindows()