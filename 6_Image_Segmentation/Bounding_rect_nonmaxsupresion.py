import numpy as np
import cv2
#Hàm xóa đi những hình chữ nhật bị overlap
def non_max_suppression(boxes, overlapThresh):
    #Nếu len(boxes) = 0 trả về []
    if len(boxes)==0:
        return []
    
    #Nếu dtype là integer thì đưa về float
    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")
    pick = []

    #Lấy ra tọa độ của các bounding box
    x1 = boxes[:,0]
    y1 = boxes[:,1]
    x2 = boxes[:,2]
    y2 = boxes[:,3]
    
    # Tính toàn diện tích của các bounding boxes và sắp xếp chúng theo thứ tự từ bottom-right, chính là tọa độ theo y của bounding box
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)
    while len(idxs) > 0:
        # Lấy ra index cuối cùng của list các indexes và thêm giá trị index vào danh sách các indexes được lựa chọn
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        # Tìm cặp tọa độ lớn nhất (x, y) là điểm bắt đầu của bounding box và tọa độ nhỏ nhất (x, y) là điểm kết thúc của bounding box
        #Tức là tìm các bounding box có diện tích nhỏ hơn 
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        #Tính toán width, height của bounding bõ và chọn ra các bounding box có width và height dương
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        overlap = (w * h) / area[idxs[:last]]
        # Xóa index cuối cùng và index của bounding box mà tỷ lệ diện tích overlap > overlapThreshold
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0])))
    
    return boxes[pick].astype("int")

if __name__ == "__main__":
    img = cv2.imread("anhso.jpg")
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, imBin = cv2.threshold(imgray, 100, 255, cv2.THRESH_BINARY)
    contours, hierarichy = cv2.findContours(imBin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    area_contour = [cv2.contourArea(j) for j in contours]
    area_sort = np.argsort(area_contour)[::-1]
    
    #Tìm các tọa độ của các bounding box và xóa đi bounding box có tọa độ (0, 0)
    boundingbox = []
    for i in area_sort[0:25]:
        cnt = contours[i]
        x,y,w,h = cv2.boundingRect(cnt)
        boundingbox.append((x,y,x+w,y+h))
    boundingbox = [box for box in boundingbox if box[:2] != (0, 0)]
    boundingbox = np.array(boundingbox)
    
    pick = non_max_suppression(boundingbox, 0.5)
    for k in pick:
        cv2.rectangle(img, (k[0], k[1]), (k[2], k[3]), (255, 0, 0), 2)
        
    cv2.imshow("Bounding Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
