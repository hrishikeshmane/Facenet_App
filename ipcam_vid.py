import cv2

cap = cv2.VideoCapture('http://192.168.1.39:8080/video')

while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.imshow('frame',frame)
    cv2.imwrite("./train_vids/vid1",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break