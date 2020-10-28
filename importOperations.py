import cv2
print("Success")

"""
For an image:

image = cv2.imread("DATA2/01-parrot.jpg")
cv2.imshow("Output", image)
cv2.waitKey(0)


For a video:

cap = cv2.VideoCapture("Path/video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # q ile donguden cik
        break


For webcam:

cap = cv2.VideoCapture(0)
cap.set(3, 640) # yukseklik
cap.set(4, 480) # genislik
cap.set(10, 100) # parlaklik


while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # q ile donguden cik
        print("Adios amigo!")
        break

"""