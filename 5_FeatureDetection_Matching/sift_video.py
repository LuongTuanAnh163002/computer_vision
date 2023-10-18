import cv2
sift = cv2.xfeatures2d.SIFT_create()
video = cv2.VideoCapture(0)
while True:
    ret, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, des = sift.detectAndCompute(gray,None)
    img_rs = cv2.drawKeypoints(gray,kp,img)
    cv2.imshow("Feature Tracking", img_rs)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()