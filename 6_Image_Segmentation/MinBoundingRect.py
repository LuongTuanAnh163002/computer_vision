import numpy as np
import cv2
#Hàm vẽ Bounding hình chữ nhật
def draw_bounding(image, cnt):
    rect = cv2.minAreaRect(cnt) #Trả về tâm, độ dài chiều rộng, chiều dài, và góc xoay của hình chữ nhật nhỏ nhất
    box = cv2.boxPoints(rect) #Trả về tọa độ 4 đỉnh của hình chữ nhất nhỏ nhất
    box = np.int0(box)
    cv2.drawContours(image, [box], 0, (0, 255, 0), 2)
    return image

#Hàm chính
if __name__ == "__main__":
    img = cv2.imread("anh_data/anhso.jpg") #Đọc ảnh
    imray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# Chuyển sang ảnh xám
    _, imBin = cv2.threshold(imray, 100, 255, cv2.THRESH_BINARY)# Chuyển về ảnh đen trắng
    contours, hierarichy = cv2.findContours(imBin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #Tìm contours
    area_contours = [cv2.contourArea(j) for j in contours] #Tính diện tích tất cả các contours
    area_sort = np.argsort(area_contours)[::-1] #Sắp xếp các contours theo thứ tự từ lớn đến bé
    #Vẽ Bounding rectangle cho 25 contours có diện tích lớn nhất
    for i in area_sort[:25]:
        cnt = contours[i]
        img = draw_bounding(img, cnt)
    
    cv2.imshow("Bounding Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()