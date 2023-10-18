import cv2

if __name__ == "__main__":
    img = cv2.imread("anh_data/image.png")
    #Vẽ đường thắng nối 2 điểm (50, 50) và (100, 100)
    cv2.line(img, (50, 50), (100, 100), (0, 255, 0), 2)
    cv2.imshow("Line", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()