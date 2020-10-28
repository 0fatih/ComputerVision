import cv2
import numpy as np

# Load OpenCV haardcascades
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("Resources/haarcascade_eye.xml")
cap = cv2.VideoCapture(0) # webcam

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = imgGray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

    cv2.imshow("Live", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
