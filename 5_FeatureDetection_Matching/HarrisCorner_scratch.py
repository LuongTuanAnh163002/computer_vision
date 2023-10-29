import cv2
import numpy as np

#Hàm tìm giá trị max trong một cửa sổ 3x3 với tâm là [i, j]
def find_max(R, i, j):
 max_point = 0
 
 for k in [-1, 0, 1]:
     for l in [-1, 0, 1]:
         if (max_point < R[i+k][j+l]):
             max_point = R[i+k][j+l]
 return max_point

#Hàm nhân 2 ma trận với các điểm tương ứng
def matrix_multiply(I_x, I_y):
 (h, w) = I_x.shape
 result = np.empty((h, w))
 
 for i in range(0, h):
     for j in range(0, w):
         result[i][j] = I_x[i][j] * I_y[i][j]

 return result

#Hàm này sẽ giữ lại các vị trí có giá trị = giá trị max tại mỗi cửa sổ, các giá trị không thoả mãn sẽ bị đưa về 0
def nonmax_suppression(R, i, j, max_point):
 for k in [-1, 0, 1]:
     for l in [-1, 0, 1]:
         if (R[i+k][j+l] == max_point):
             continue
         else:
             R[i+k][j+l] = 0

#Hàm tính trace của ma trận M
def calculate_trace(A, B):
 return A + B

#Hàm tính det của ma trận M
def calculate_det(A, B, C):
 det = matrix_multiply(A, B) - matrix_multiply(C, C)
 
 return det

if __name__ == "__main__":
    img = cv2.imread("hcn.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (5, 5), 2)
    IX = cv2.Sobel(gaussian, cv2.CV_64F, 1, 0, ksize = 5) #Tính đạo hàm theo chiều dọc
    IY = cv2.Sobel(gaussian, cv2.CV_64F, 0, 1, ksize = 5) #Tính đạo hàm theo chiều ngang
    A = matrix_multiply(IX, IX) # A = IX^2
    B = matrix_multiply(IY, IY) # B = IY^2
    C = matrix_multiply(IX, IY) # C = IX*IY
    
    #Xóa nhiễu
    _A = cv2.GaussianBlur(A, (5, 5), 2)
    _B = cv2.GaussianBlur(B, (5, 5), 2)
    _C = cv2.GaussianBlur(C, (5, 5), 2)

    #Tính ma trận R
    k = 0.04
    R = calculate_det(_A, _B, _C) - k * (calculate_trace(_A, _B) ** 2) #Tính R quyết định xem pixel nào là góc
    _, R = cv2.threshold(R, R.max() // 500, R.max(), cv2.THRESH_BINARY)
    h, w = R.shape
    for i in range(1, h-1, 2):
        for j in range(1, w-1, 2):
            max_pixel = find_max(R, i, j)
            nonmax_suppression(R, i, j, max_pixel)

    R_dst = cv2.dilate(R, None) #Giản nở các điểm ảnh
    img[R_dst > 0.001 * R_dst.max()] = (0, 255, 0) #Những điểm nào là góc thì tô màu xanh lục

    cv2.imshow("Harry Corner", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()