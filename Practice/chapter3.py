# Chapter 3 : Resizing and Cropping
import cv2 #cv2 stands for computer vision


img = cv2.imread("Resources/brain.jpg")
print(img.shape)        # (253, 450, 3) first is height, second is width, third is number of channels which is BGR

imgReduced = cv2.resize(img, (300,150))      # here we define the width first and then the height
print(imgReduced.shape)

imgStretched = cv2.resize(img, (600,300)) 

imgCropped = img[0:200, 200:400] # height comes first and then the width

cv2.imshow("Original Image", img)
cv2.imshow("Reduced Image", imgReduced)
cv2.imshow("Stretched Image", imgStretched)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)