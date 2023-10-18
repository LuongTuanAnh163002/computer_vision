import cv2

if __name__ == "__main__":
    img = cv2.imread("anh_data/image.png")
    #Vẽ hình tròn với tọa độ tâm (50, 50) và bán kính bằng 20
    cv2.circle(img, (50, 50), 20, (0, 255, 0), 2)
    cv2.imshow("Circle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()