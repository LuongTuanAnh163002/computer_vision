import cv2
import numpy as np

if __name__ == "__main__":

    img = cv2.imread("hcn.jpg")
    img_ori = img.copy()
    if img is None:
        print("Error in read image")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 100, 200)
    #Tính toán các vị trị được xác định là line, các vị trí được xác định thông qua hệ tọa độ cực
    #Hàm bên dưới trả về các bán kính và góc trong hệ tọa độ cực tương ứng với các điểm
    line = cv2.HoughLines(canny, 1, np.pi / 180, 200)
    if line is not None:
        for i in range(len(line)):
            r = line[i][0][0] #Giá trị của bán kính
            theta = line[i][0][1] #Giá trị của góc theta
            cosin = np.cos(theta)
            sins = np.sin(theta)
            x0 = r * cosin
            y0 = r * sins
            
            #Tọa độ đầu mút thứ nhất của 1 đường thẳng
            x1 = int(x0 - 1000 * sins)
            y1 = int(y0 + 1000 * cosin)

            #Tọa độ đầu mút thứ 2 của 1 đường thẳng
            x2 = int(x0 + 1000 * sins)
            y2 = int(y0 - 1000 * cosin)

            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    img_ori = cv2.resize(img_ori, (500, 500))
    img = cv2.resize(img, (500, 500))
    cv2.imshow("Origin image:", img_ori)
    cv2.imshow("HoughLine Transform", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
