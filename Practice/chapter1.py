# Chapter 1 : Read images, videos and webcams
import cv2 #cv2 stands for computer vision
print("Package Imported")


# In order to read images we have a function by the name imread
img1 = cv2.imread("Resources/brain.jpg")

# To display we have the function known as imshow 
cv2.imshow("Output", img1)
cv2.waitKey(0)


cap = cv2.VideoCapture("Resources/Sirus.mp4")
while True:
    success, img2 = cap.read()
    cv2.imshow("Video", img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap_cam = cv2.VideoCapture(0)
cap_cam.set(3, 640) #width
cap_cam.set(4, 480) #height
cap_cam.set(10, 100)

while True:
    success, img3 = cap_cam.read()
    cv2.imshow("Video Webcam", img3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break