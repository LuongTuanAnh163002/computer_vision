import cv2

if __name__ == "__main__":
    img = cv2.imread("white.jpg")
    img = cv2.resize(img, (500, 500))
    #Vẽ hình chữ nhật với điểm đầu là (50, 50), điểm cuối là (200, 200)
    cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)
    cv2.imshow("Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    