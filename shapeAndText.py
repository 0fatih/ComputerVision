import cv2
import numpy as np


img = np.zeros((512,512,3))
# print(img.shape)
# img[:] = 255,0,0 # BGR

cv2.line(img,(0,0), (512,512), (255,0,0), 2)
cv2.line(img, (0,512), (512,0), (0,0,255), 3)
#cv2.rectangle(img, (0,0), (250,350), (0,255,0), cv2.FILLED) # cv2.FILLED yerine sayi yazarak ici bos ve kenarlari girdigimiz sayi kalinliginda bir sekil olusturabiliriz
#cv2.rectangle(img, (0,0), (250,350), (0,255,0), 2)
#cv2.circle(img, (400,50), 30, (255,255,0), 5)
cv2.putText(img,"Hello, Fatih!", (200,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)