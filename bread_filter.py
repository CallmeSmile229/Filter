import cv2
import numpy as np
import dlib
# Loading Camera and Nose image and Creating mask
cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows, cols, _ = frame.shape
filter = cv2.imread("bread.png")
cv2.imshow('INPUT filter',filter)
# Loading Face detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
maskk = np.zeros((rows,cols),np.uint8)
while True:
    _, frame = cap.read()
    maskk.fill(0)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(frame)
    for face in faces:
        landmarks = predictor(gray_frame, face)
        filter_width = int(landmarks.part(14).x)- int(landmarks.part(2).x)
        filter_height = int(filter_width/1.65)
        top_left = (int(landmarks.part(3).x),int(landmarks.part(19).y))
        bottom_right = (int(landmarks.part(13).x),int(landmarks.part(13).y))
        
        mask = cv2.resize(filter,(filter_width,filter_height))
        mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        _, glass_mask = cv2.threshold(mask_gray, 25, 200, cv2.THRESH_BINARY)
        
        filter_area = frame[top_left[1]: top_left[1] + filter_height,top_left[0]: top_left[0] + filter_width]
        final_filter = cv2.bitwise_and(filter_area,filter_area,mask = glass_mask)
        frame[top_left[1]: top_left[1] + filter_height,top_left[0]: top_left[0] + filter_width] = final_filter
    cv2.imshow("Bread Filter", frame)
    key = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q') or key == 27:
        break