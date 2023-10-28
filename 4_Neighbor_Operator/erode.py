import cv2
import numpy as np

if __name__ == "__main__":
    #Chỉ phù hợp với ảnh nhị phân(đen và trắng), ảnh màu vẫn dùng được nhưng đầu ra sẽ không như mong muốn
    img = cv2.imread("morphology_gradient.png")
    kernel = np.ones((5, 5), np.uint8)
    
    #Làm xói mòn các đối tượng trong ảnh, đối tượng trong ảnh trông gầy hơn
    img_erode = cv2.erode(img, kernel, iterations = 1)
    cv2.imshow('Original', img)
    cv2.imshow("Erode image", img_erode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()