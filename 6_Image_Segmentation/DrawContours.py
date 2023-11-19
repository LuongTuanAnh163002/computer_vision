import cv2

if __name__ == "__main__":
    img = cv2.imread("hcn.jpg")
    #Chuyển từ ảnh màu sang ảnh xám
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Chuyển từ ảnh xám sang ảnh nhị phân, pixel nào có giá trị nhỏ hơn 120 thì trả về 0, còn lại trả về 255
    ret, thresh = cv2.threshold(imgray, 120, 255, cv2.THRESH_BINARY)

    #Tìm và vẽ tất cả contours trong ảnh
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print(contours)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    #Tính diện tích của contours số 0
    cnt = contours[0]
    area = cv2.contourArea(cnt)
    print("Area of contours 0 is:", area)

    #Tính chu vi của contous số 0
    perimeter = cv2.arcLength(cnt, True)
    print("perimeter of contour 0 is:", perimeter)

    #Tính moment của contour số 0, m00 chính là diện tích của contours số 0, ngoài ra còn có thể tính được trọng tâm
    #của contours số 0
    moment = cv2.moments(cnt)
    print(moment)

    cv2.imshow("Draw Contours", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()