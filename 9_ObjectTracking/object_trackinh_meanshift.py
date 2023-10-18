import cv2
import numpy as np
video = cv2.VideoCapture(r"D:\2023_Spring\CPV301\Assignment\Hog_algorithm_human\Hogvideo.mp4")
ret,frame = video.read()
x,y,w,h = cv2.selectROI(frame)
track_window = (x, y, w, h)
roi = frame[y:y+h, x:x+w]
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])
cv2.normalize(roi_hist,roi_hist, 0, 255, cv2.NORM_MINMAX)
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while(True):
   ret, frame = video.read()
   if ret == True:
       hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
       dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
       ret, track_window = cv2.meanShift(dst, track_window, term_crit)
       x,y,w,h = track_window
       img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
       cv2.imshow('img2',img2)
       if cv2.waitKey(1) & 0xFF == ord("q"):
            break
   else:
       break
cv2.destroyAllWindows()
video.release()