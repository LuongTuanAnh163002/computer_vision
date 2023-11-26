import cv2
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    img = cv2.imread("apple_2.jpg", cv2.IMREAD_GRAYSCALE)
    f = np.fft.fft2(img) #Chuyển sang hệ fourier(hệ tọa độ tần số)
    fshift = np.fft.fftshift(f) #Dịch tọa độ tần số (0, 0) về tâm của ảnh
    magnitude_spectrum = 20*np.log(np.abs(fshift)) #Tính toán độ lớn của tần số cho mỗi pixel

    #Với fourier transform thì càng xa tâm thì tần số càng cao, càng gần tâm thì tần số càng thấp
    #Các cạnh và nhiễu là các vị trí có tần số cao
    #--------------Phát hiện cạnh bằng fourier transform-----------------------
    rows, cols = img.shape
    crow, ccol = rows//2, cols//2
    fshift[crow-30:crow+31, ccol-30:ccol+31] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.real(img_back)

    plt.subplot(131)
    plt.imshow(magnitude_spectrum, cmap = "gray")
    plt.title('Mag')
    plt.subplot(132)
    plt.imshow(img, cmap = "gray")
    plt.title('Origin')
    plt.subplot(133)
    plt.imshow(img_back, cmap = "gray")
    plt.title('Edge detect')
    plt.tight_layout()
    plt.show()