# Chapter 5 : Warp Perspective
import cv2 #cv2 stands for computer vision
import numpy as np

img = cv2.imread("Resources/cards.png")

width, height = 250, 350
pts1 = np.float32([ [282,13], [396,83], [180,186], [300,260] ])
pts2 = np.float32([ [0,0], [width,0], [0,height], [width,height] ])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)