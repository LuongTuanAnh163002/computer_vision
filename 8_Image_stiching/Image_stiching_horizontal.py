import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_stitching_horizontal(img1, img2):
    #img1 là ảnh ở phía trước(bên trái), img2 là ảnh ở phía sau(bên phải)
    imray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    imray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    sift_detector = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift_detector.detectAndCompute(imray1, None) #Trước
    kp2, des2 = sift_detector.detectAndCompute(imray2, None) #Sau
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck = False)
    rawMatches = bf.knnMatch(des2, des1, 2)
    matches = []
    for m, n in rawMatches:
        if m.distance < 0.75 * n.distance:
            matches.append(m)
    matches = sorted(matches, key = lambda x: x.distance, reverse = True)
    matches = matches[:200]
    kp1 = np.float32([kp.pt for kp in kp1]) #Trước
    kp2 = np.float32([kp.pt for kp in kp2]) #Sau
    pts1 = np.float32([kp1[m.trainIdx] for m in matches])
    pts2 = np.float32([kp2[m.queryIdx] for m in matches])
    h, status = cv2.findHomography(pts2, pts1, cv2.RANSAC)
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    result = cv2.warpPerspective(img2, h, (w1+w2, max(h1, h2)))
    result[0:h1, 0:w1] = img1
    return result

def draw_keypoint(im1, im2):
    #img1 là ảnh ở phía trước(bên trái), img2 là ảnh ở phía sau(bên phải)
    imray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    imray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY) 
    sift_detector = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift_detector.detectAndCompute(imray1, None)
    kp2, des2 = sift_detector.detectAndCompute(imray2, None)
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck = False)
    rawMatches = bf.knnMatch(des1, des2, 2)
    matches = []
    for m, n in rawMatches:
        if m.distance < 0.75 * n.distance:
            matches.append(m)
    matches = sorted(matches, key = lambda x: x.distance, reverse = True)
    matches = matches[:200]
    img = cv2.drawMatches(im1, kp1, im2, kp2, matches, None, flags = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    plt.figure(figsize = (10, 10))
    plt.axis("off")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

if __name__ == "__main__":
    im1 = cv2.imread(r"D:\Sourcecodepython\Image_processing\anh_data\query.jpg")
    im2 = cv2.imread(r"D:\Sourcecodepython\Image_processing\anh_data\train.jpg")
    #draw_keypoint(im1, im2)
    rs = image_stitching_horizontal(im1, im2)
    plt.subplot(1, 3, 1)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(im1, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 3, 2)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 3, 3)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(rs, cv2.COLOR_BGR2RGB))
    plt.show()