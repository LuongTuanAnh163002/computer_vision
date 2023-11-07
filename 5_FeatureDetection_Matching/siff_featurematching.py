import cv2
if __name__ == "__main__":
    #Đọc ảnh
    img1 = cv2.imread("Elon1.jpg")
    img2 = cv2.imread("Elon_Musk.jpg")

    #Chuyển ảnh sang gray
    imray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    imray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    #Tạo đối tượng sift
    sift = cv2.SIFT_create()

    #Tính toán các keypoint và keypoint descriptor
    #Phương thức bên dưới trả về 2 output với kp là các keypoint và des là các descriptor ứng với các keypoint với 128 chiều cho mỗi một descriptor
    #des là ma trận 2 chiều với số cột là 128, số hàng là số descriptor ứng với số keypoint
    kp1, des1 = sift.detectAndCompute(imray1,None)
    kp2, des2 = sift.detectAndCompute(imray2,None)

    #Tạo đối tượng để match giữa 2 ảnh
    bf = cv2.BFMatcher()

    #Tiến hành match giữa 2 hình ảnh dựa vào descriptor của 2 hình ảnh với số hàng xóm để so sánh là 2
    matches = bf.knnMatch(des1, des2, k = 2)

    #Tính toán xem match nào là tốt nhất
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])
    
    #vẽ match giữa 2 hình ảnh
    rs = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags = 2)
    rs1 = cv2.resize(rs, (300, 300))

    #4 đoạn code bên dưới dùng để vẽ các keypoint đã tìm được trong bức ảnh
    #-----------------------------------------------
    img3 = cv2.drawKeypoints(imray1,kp1,img1)
    img4 = cv2.drawKeypoints(imray2,kp2,img2)
    img3 = cv2.resize(img3, (500, 500))
    img4 = cv2.resize(img4, (500, 500))
    rs1 = cv2.resize(rs1, (500, 500))
    cv2.imshow("kp1", img3)
    cv2.imshow("kp2", img4)
    cv2.imshow("Matches", rs1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
