import cv2

if __name__ == "__main__":
    img = cv2.imread("image.png")
    scale1 = cv2.resize(img, (300, 400)) #resize to hơn và không dùng tham số fx, fy
    scale2 = cv2.resize(img, (0, 0), fx = 0.8, fy = 0.3) #resize nhỏ hơn và dùng tham số fx, fy
    cv2.imshow("Original", img)
    cv2.imshow("Rezise bigger", scale1)
    cv2.imshow("Resize smaller", scale2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    