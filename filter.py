import cv2
import numpy as np

# đọc ảnh foreground
def on_change(val):
    print(val)
    alpha = val/100
    beta = (1.0 - alpha)
    result = cv2.addWeighted(img1, alpha, img2, beta, 0.0);
    cv2.imshow('blend', result)
 
img1 = cv2.imread('E:\ComputerVision\add_filter\my_filter\culu.jpg')
img2 = cv2.imread('E:\ComputerVision\add_filter\my_filter\winterBG.png')
 
# img1 = cv2.resize(img1, (400, 400))
# img2 = cv2.resize(img2, (400, 400))
 
cv2.imshow('blend', img2)
 
cv2.createTrackbar('slider', 'blend', 0, 100, on_change)
 
cv2.waitKey(0)
cv2.destroyAllWindows()