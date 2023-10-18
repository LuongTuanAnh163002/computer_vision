import cv2
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    img = cv2.imread("anh_data/image.png", cv2.IMREAD_GRAYSCALE)
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT) #Chuyển sang hệ fourier(hệ tọa độ tần số)
    dft_shift = np.fft.fftshift(dft) #Dịch tọa độ tần số (0, 0) về tâm của ảnh
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])) #Tính toán độ lớn của tần số cho mỗi pixel
    plt.imshow(magnitude_spectrum, cmap = "gray")
    plt.show()

    #--------------Làm mờ ảnh bằng fourier transform-----------------------
    # rows, cols = img.shape
    # crow,ccol = rows//2 , cols//2
    # mask = np.zeros((rows,cols,2),np.uint8)
    # mask[crow-30:crow+30, ccol-30:ccol+30] = 1
    # fshift = dft_shift*mask
    # f_ishift = np.fft.ifftshift(fshift) #Dịch tọa độ tâm về lại vị trí góc trên trái của ảnh
    # img_back = cv2.idft(f_ishift) #Chuyển về hệ tọa độ oxy
    # img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1]) #Tính toán lại độ lớn các pixel
    # plt.subplot(1, 2, 1)
    # plt.imshow(img_back, cmap = "gray")
    # plt.subplot(1, 2, 2)
    # plt.imshow(img, cmap = "gray")
    # plt.show()