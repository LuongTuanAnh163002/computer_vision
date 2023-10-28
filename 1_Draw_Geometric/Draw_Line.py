import cv2

if __name__ == "__main__":
    img = cv2.imread("white.jpg")
    img = cv2.resize(img, (500, 500))
    #Vẽ đường thắng nối 2 điểm (50, 50) và (200, 200)
    cv2.line(img, (50, 50), (200, 200), (0, 255, 0), 2)
    cv2.imshow("Line", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()