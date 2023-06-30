# Doc thu vien
import cv2
import dlib
import numpy as np

#doc video real-time
cap = cv2.VideoCapture(0)

# Doc file nhan dien khuon mat
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# doc background
BG = cv2.imread('BGcamera.png')
# dong comment de kiem tra background
# cv2.imshow("INPUT Background",BG)

# tim diem khong co gia tri trong Background (vung chen anh vao)
temp_roi = np.argwhere(BG == [255,255,255])
first_point_in_roi = temp_roi[0][1]
result = BG

while True:
    # roi la vung anh duoc chen vao
    roi = BG[0:480,first_point_in_roi:first_point_in_roi + 640]
    
    # xu ly video
    _, frame = cap.read()
    # cv2.imshow('INPUT Video real-time',frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # nhan dien khuon mat
    faces = detector(gray)
    # xu ly trong moi khuon mat
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        # ve hinh chu nhat voi moi khuon mat nhan duoc
        cv2.rectangle(frame,(x1,y1),(x2,y2),[150,150,150],thickness=3)
        landmarks = predictor(gray,face)
        filter_width = int(y1)- int(y2)
        filter_height = int(filter_width/1.3)
    roi = frame
    # chen anh vao vung dinh san
    result[0:480,first_point_in_roi:first_point_in_roi + 640] = roi
    cv2.imshow('Camera Phone',result)
    # an q de thoat chuong trinh
    key = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q') or key == 27:
        break    
cap.release
cv2.destroyAllWindows()