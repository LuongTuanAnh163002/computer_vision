import cv2

if __name__ == "__main__":
    img = cv2.imread("anh_data/image.png")
    #Vẽ hình chữ nhật với điểm đầu là (50, 50), điểm cuối là (100, 100)
    cv2.rectangle(img, (50, 50), (100, 100), (0, 255, 0), 2)
    cv2.imshow("Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    