import numpy as np
import cv2
img = cv2.imread('image.png')
rows, cols = img.shape[0:2]
#flip the image horizontally
M1 = np.float32([[1,  0, 0],
                [0, -1, rows],
                [0,  0, 1]])

#flip the image vertical
M2 = np.float32([[-1, 0, cols], 
                [0, 1, 0], 
                [0, 0, 1]])




flip_x = cv2.warpPerspective(img, M1, (int(cols),int(rows)))
flip_y = cv2.warpPerspective(img, M2, (int(cols),int(rows)))

cv2.imshow('flip x-horizontally', flip_x)
cv2.imshow('original image', img)
cv2.imshow("flip y-vertical", flip_y)
cv2.waitKey(0)
cv2.destroyAllWindows()