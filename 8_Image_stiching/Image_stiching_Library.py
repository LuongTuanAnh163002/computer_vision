import cv2
import matplotlib.pyplot as plt
import imutils
import numpy as np

#Hàm xóa những phần bị đen sau khi ghép ảnh
def convert_img(image):
    image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0,0,0))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_img = cv2.threshold(gray, 0, 255 , cv2.THRESH_BINARY)[1]
    contours = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv2.contourArea)

    mask = np.zeros(thresh_img.shape, dtype="uint8")
    x, y, w, h = cv2.boundingRect(areaOI)
    cv2.rectangle(mask, (x,y), (x + w, y + h), 255, -1)

    minRectangle = mask.copy()
    sub = mask.copy()

    while cv2.countNonZero(sub) > 0:
        minRectangle = cv2.erode(minRectangle, None)
        sub = cv2.subtract(minRectangle, thresh_img)
    
    contours = cv2.findContours(minRectangle.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(areaOI)

    image = image[y:y + h, x:x + w]
    return image


if __name__ == "__main__":
    im1 = cv2.imread(r"D:\Sourcecodepython\Image_processing\anh_data\first.jpg")
    im2 = cv2.imread(r"D:\Sourcecodepython\Image_processing\anh_data\second.jpg")
    im3 = cv2.imread(r"D:\Sourcecodepython\Image_processing\anh_data\third.jpg")
    images = [im1, im2, im3]
    sticher = cv2.Stitcher_create()
    status, stitched_img = sticher.stitch(images) #Ghép 3 ảnh lại với nhau(Panorama)
    if not status:
        stitched_img = convert_img(stitched_img) #Xóa những phần bị đen của ảnh
        plt.axis("off")
        plt.imshow(cv2.cvtColor(stitched_img, cv2.COLOR_BGR2RGB))
        plt.show()
        print(status)

    else:
        print("Can not be stitching image")
        print("I think not enough keypoint to stitching")

    