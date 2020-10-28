import cv2
import numpy as np

img = cv2.imread("DATA2/02_animal_in_backpack.jpg")
print(img.shape) # height, width, rgb
imgResize = cv2.resize(img, (300,200)) # resize

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)