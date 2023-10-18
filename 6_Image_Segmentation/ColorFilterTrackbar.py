import cv2
import numpy as np

#Đoạn code comment dưới đây dùng để xác đinh Hue Min, Hue Max, Sat Min, Sat Max, Val Min, Val Max của 1 ảnh khi chuyển sang hsv
#Sử dụng trackbar để xác định các giá trị nêu trên
# def empty(a):
#     pass

# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars", 640, 240)
# cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
# cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
# cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
# cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
# cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
# cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

# while True:
#     img = cv2.imread("anh_data/image.png")
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
#     h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
#     s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
#     v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])

#     mask = cv2.inRange(hsv, lower, upper)
#     cv2.imshow("mask", mask)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# Sau khi đã tìm được Hue Min, Hue Max, Sat Min, Sat Max, Val Min, Val Max thì gán nó vào 2 biến lower, upper
img = cv2.imread("anh_data/image.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Chuyển ảnh sang hsv
lower = np.array([0, 109, 42]) #lower = [Hue Min, Sat Min, Val Min]
upper = np.array([93, 255, 255]) #upper = [Hue Max, Sat Max, Val Max]

#Trả về ảnh đen trắng với những pixel nằm trong vùng lower đến upper thì thành màu trắng, còn lại là màu đen
mask = cv2.inRange(hsv, lower, upper)

rs = cv2.bitwise_and(img, img, mask = mask)
rs[rs == 0] = 255 #Những điểm pixel đen thì đổi thành trắng
cv2.imshow("COlor Filter", rs)
cv2.waitKey(0)
cv2.destroyAllWindows()

