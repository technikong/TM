import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 780)

while True:
    success, img = cap.read()
    cv2.imshow('My Frist OpenCV', img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllwindows()
        break