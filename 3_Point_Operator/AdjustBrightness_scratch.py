import cv2
import numpy as np

def adjust_brightness(img, value=30):
    '''
    Augment: Input: img: np.array([[[]]]) (h,w,c)
                    value: int
            Output: np.array([[[]]]) (h,w,c)
    '''
    b, g, r = cv2.split(img)
    if value < 0:
        lim = 0 + abs(value)
        b[b < lim] = 0
        b[b >= lim] -= abs(value)
        g[g < lim] = 0
        g[g >= lim] -= abs(value)
        r[r < lim] = 0
        r[r >= lim] -= abs(value)
    
    elif value > 0:
        lim = 255 - value
        b[b > lim] = 255
        b[b <= lim] += value
        g[g > lim] = 255
        g[g <= lim] += value
        r[r > lim] = 255
        r[r <= lim] += value
    
    final_img = cv2.merge((b, g, r))
    return final_img

if __name__ == "__main__":
    img = cv2.imread("image.png")
    img_bright = adjust_brightness(img, 50)
    cv2.imshow("Original", img)
    cv2.imshow("Adjust bright", img_bright)
    cv2.waitKey(0)
    cv2.destroyAllWindows()