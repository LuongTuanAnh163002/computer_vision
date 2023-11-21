import numpy as np 
import cv2 
  
cap = cv2.VideoCapture('los_angeles.mp4') 
fgbg = cv2.createBackgroundSubtractorMOG2() 
  
while True: 
    ret, frame = cap.read() 
    if ret:
        fgmask = fgbg.apply(frame) 

        frame = cv2.resize(frame, (500, 500))
        fgmask = cv2.resize(fgmask, (500, 500))
    
        cv2.imshow('fgmask', fgmask) 
        cv2.imshow('frame',frame ) 
        if cv2.waitKey(1) & 0XFF == ord("q"):
            break
    else:
        break
  
cap.release() 
cv2.destroyAllWindows()