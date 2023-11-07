import cv2
import numpy as np
img = cv2.imread("coin.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3 ,3))
circle = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)
if circle is not None:
    detect_circle = np.uint16(np.around(circle))
    for i in range(len(detect_circle[0, :])):
        x = detect_circle[0, :][i][0]
        y = detect_circle[0, :][i][1]
        r = detect_circle[0, :][i][2]
        cv2.circle(img, (x, y), r, (0, 255, 0), 3)
cv2.imshow("HouseCircle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
