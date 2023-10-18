import cv2
import numpy as np

if __name__ == "__main__":
    image1 = cv2.imread("anh_data/Hull_Original_Image.jpg")
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (3, 3))
    ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    hull = []
    for i in range(len(contours)):
    # creating convex hull object for each contour
        hull.append(cv2.convexHull(contours[i], False))
    
    drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
    for i in range(len(contours)):
        color_contours = (0, 255, 0) # green - color for contours
        color = (255, 0, 0) # blue - color for convex hull
        # draw ith contour
        cv2.drawContours(drawing, contours, i, color_contours, 1)
        # draw ith convex hull object
        cv2.drawContours(drawing, hull, i, color, 1)
    
    cv2.imshow("convexhull", drawing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()