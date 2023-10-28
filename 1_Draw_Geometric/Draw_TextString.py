import cv2

if __name__ == "__main__":
    img = cv2.imread("white.jpg")
    img = cv2.resize(img, (500, 500))
    #Vẽ text với điểm xuất phát là (50, 50) với loại phông là FONT_HERSHEY_COMPLEX và fontsclale = 1
    cv2.putText(img, "Learn Opencv", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Text String", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()