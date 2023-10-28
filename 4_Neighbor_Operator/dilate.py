import cv2
import numpy as np

if __name__ == "__main__":
    #Chỉ phù hợp với ảnh nhị phân(đen và trắng), ảnh màu vẫn dùng được nhưng đầu ra sẽ không như mong muốn
    img = cv2.imread("morphology_gradient.png")
    kernel = np.ones((5, 5), np.uint8)
    #Làm giãn nở các đối tượng trong ảnh, đối tượng trong ảnh trông béo hơn
    img_dilate = cv2.dilate(img, kernel, iterations = 2)
    cv2.imshow('Original', img)
    cv2.imshow("Dilate image", img_dilate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()