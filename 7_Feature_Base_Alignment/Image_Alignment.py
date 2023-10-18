import cv2
import numpy as np
max_feature = 5000
img_tem = cv2.imread(r"D:\Sourcecodepython\Image_processing\anh_data\anh1.jpg")
img_align = cv2.imread(r"D:\Sourcecodepython\Image_processing\anh_data\anh2.jpg")

imray1 = cv2.cvtColor(img_tem, cv2.COLOR_BGR2GRAY)
imray2 = cv2.cvtColor(img_align, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create(max_feature)
keypoint1, descriptors1 = orb.detectAndCompute(imray1, None)
keypoint2, descriptors2 = orb.detectAndCompute(imray2, None)
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
matches = matcher.match(descriptors1, descriptors2, None)
matches = list(matches)
matches.sort(key=lambda x: x.distance, reverse=False)
numGoodMatches = int(len(matches) * 0.9)
matches = matches[:numGoodMatches]
imMatches = cv2.drawMatches(img_tem, keypoint1, img_align, keypoint2, matches, None)

points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)
for i, match in enumerate(matches):
    points1[i, :] = keypoint1[match.queryIdx].pt
    points2[i, :] = keypoint2[match.trainIdx].pt

h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)
height, width, channel = img_tem.shape
im1Reg = cv2.warpPerspective(img_align, h, (width, height))

cv2.imshow("Template", img_tem)
cv2.imshow("Before", img_align)
cv2.imshow("After", im1Reg)
cv2.waitKey(0)
cv2.destroyAllWindows()