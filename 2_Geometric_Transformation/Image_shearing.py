import numpy as np
import cv2
img = cv2.imread('image.png')
rows, cols = img.shape[0:2]

#shearing x-axis
shear_x = 0.5
M1= np.float32([[1, shear_x, 0], [0, 1, 0], [0, 0, 1]])

#shearing y-axis
shear_y = 0.5
M2= np.float32([[1, 0, 0], [shear_y, 1, 0], [0, 0, 1]])


sheared_img_x_axis = cv2.warpPerspective(img, M1, (int(cols*1.5), int(rows*1.5))) #shearing va resize anh gap 1.5 lan
sheared_img_y_axis = cv2.warpPerspective(img, M2, (int(cols*1.5), int(rows*1.5))) #sheraing va resize anh gap 1.5 lan

cv2.imshow('shearing_x_axis', sheared_img_x_axis)
cv2.imshow('shearing_y_axis', sheared_img_y_axis)
cv2.imshow('origin', img)
cv2.waitKey(0)
cv2.destroyAllWindows()