import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)
_, frame = cap.read()
while True:
    _, frame = cap.read()
    cv2.imshow("INPUT", frame)
    key = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q') or key == 27:
        break