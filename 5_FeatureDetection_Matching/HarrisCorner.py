import cv2
import numpy as np

if __name__ == "__main__":
    im = cv2.imread("hcn.jpg")
    img_original = im.copy()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #Chuyển ảnh sang gray
    gray_float = np.float32(gray)

    #Tính R với R là 1 ma trận 2 chiều với mỗi 1 phần tử ứng với 1 điểm ảnh
    dest = cv2.cornerHarris(gray_float, 2, 5, 0.04) #Tính R
    dest_dlt = cv2.dilate(dest, None) #Giãn nở ảnh
    im[dest_dlt > 0.01 * dest_dlt.max()] = (0, 0, 255) #Lấy ra những điểm là điểm góc trong ảnh
    
    img_original = cv2.resize(img_original, (500, 500))
    im = cv2.resize(im, (500, 500))
    cv2.imshow("Original", img_original)
    cv2.imshow("Harris corner", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    