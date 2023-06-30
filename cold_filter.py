from re import X
from cv2 import VideoCapture
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
BG = cv2.imread("BGwinter3.png")
cv2.imshow("INPUT Background",BG)
# cv2.waitKey(0)

while True:
    ref, frame = cap.read()
    cv2.imshow("INPUT video real-time",frame)
    result = cv2.addWeighted(frame,0.7,BG,0.3,gamma=0)
    cv2.imshow("Cold Filter",result)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()       
