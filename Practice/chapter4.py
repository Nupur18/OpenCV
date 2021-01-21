# Chapter 4 : Shapes and Texts
import cv2 #cv2 stands for computer vision
import numpy as np


img = np.zeros((512,512,3), np.uint8) # this is a grayscale image because it only has 512 by 512 pixels
# print(img.shape)
# img[:] = 255,0,0 # [:] means we want to do for the whole image 
# img[200:300, 100:300] = 255,0,0 # the colored part is only the range that we have defined here

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)
cv2.rectangle(img, (0,0), (250,350), (0,0,255), 2)
# cv2.rectangle(img, (0,0), (250,350), (0,0,255), cv2.FILLED) cv2.FILLED is used to fill the rectangular area
cv2.circle(img, (400,50), (30), (255,255,0), 5)
cv2.putText(img, " OPENCV ", (300,200), cv2.FONT_HERSHEY_COMPLEX, 1.4, (0,150,0), 3)


cv2.imshow("Image", img)
cv2.waitKey(0)