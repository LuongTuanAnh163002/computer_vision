import cv2
import numpy as np
import matplotlib.pyplot as plt

def align_image(img_align, img_template, value1 = 5000, value2 = 0.9):
  #Chuyển ảnh sang ảnh xám
  img1 = cv2.cvtColor(img_align, cv2.COLOR_BGR2GRAY)
  img2 = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)
  height, width = img2.shape
    
  #Tạo ORB object với 5000 features(đọc về thuật toán ORB)
  orb_detector = cv2.ORB_create(value1)
    

  #TÌm keypoint và ma trận descriptors cho mỗi hình ảnh, kp chính là keypoint và d chính là descriptor
  kp1, d1 = orb_detector.detectAndCompute(img1, None)
  kp2, d2 = orb_detector.detectAndCompute(img2, None)
    

  #Tạo ra đối tương Brute Force matcher để tiến hành nối các điểm giống nhau trên 2 bức ảnh
  matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    
  #Tiến hành nối các điểm giống nhau giữa 2 hình ảnh dựa vào descriptor giữa 2 hình ảnh
  matches = matcher.match(d1, d2)


  matches = list(matches)
  #Sắp xếp các khoảng cách giữa các điểm giống nhau giữa 2 hình ảnh theo thứ tự từ bé đến lớn
  matches.sort(key = lambda x: x.distance)
    
  # Lấy khoảng 90% các điểm trong matches
  matches = matches[:int(len(matches)*value2)]
  no_of_matches = len(matches)
    
  # Tạo 2 ma trận trống(toàn 0) có shape = (no_of_matches, 2)
  p1 = np.zeros((no_of_matches, 2))
  p2 = np.zeros((no_of_matches, 2))

  #Tiến hành điền tọa độ của các keypoint của 2 bức ảnh vào 2 ma trận trên  
  for i in range(len(matches)):
    p1[i, :] = kp1[matches[i].queryIdx].pt #Truy cập đến index của keypoint đó và lấy ra tọa độ của ảnh align
    p2[i, :] = kp2[matches[i].trainIdx].pt #Truy cập đến index của keypoint đó và lấy ra tọa độ của ảnh template(ảnh mẫu)
    
  # Tìm ma trận homography(H)
  homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)
    
  # Tiến hành chuyển bức ảnh cần align về dạng giống với bức ảnh template(ảnh mẫu)
  transformed_img = cv2.warpPerspective(img1_color,
                      homography, (width, height))
  
  return transformed_img

if __name__ == "__main__":
  #Show hình ảnh
  img1_color = cv2.imread("anh2.jpg")  # Ảnh cần align
  img2_color = cv2.imread("anh1.jpg")    # Ảnh template(ảnh mẫu)
  img_transform = align_image(img1_color, img2_color)
  img1_color = cv2.resize(img1_color, (500, 500))
  img2_color = cv2.resize(img2_color, (500, 500))
  img_transform = cv2.resize(img_transform, (500, 500))
  cv2.imshow("Template", img2_color)
  cv2.imshow("Before", img1_color)
  cv2.imshow("After", img_transform)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
