import cv2
#Dùng để tìm vị trí của hình ảnh này trong 1 hình ảnh khác
if __name__ == "__main__":
    img = cv2.imread("Original.jpg")
    imray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Ảnh gốc
    temp = cv2.imread("TemplateMatching.jpg", 0) #Ảnh cần tìm vị trí trong hình ảnh gốc ở trên
    h, w = temp.shape
    res = cv2.matchTemplate(imray, temp, cv2.TM_CCOEFF_NORMED) #Tính toán mức độ tương đồng của các pixels trong cả 2 ảnh
    minval, maxval, minloc, maxloc = cv2.minMaxLoc(res, None) #Trả về pixel có độ tương đồng lớn nhất và vị trí của nó
    matchLoc = maxloc
    cv2.rectangle(img, matchLoc, (matchLoc[0] + w, matchLoc[1] + h), (0, 255, 0), 2) #Vẽ hình chữ nhật sau khi tìm được vị trí
    cv2.imshow("Template Matching", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()