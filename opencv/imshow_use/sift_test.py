import cv2 as cv
import matplotlib.pyplot as plt


img=cv.imread('./lena.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift=cv.SIFT_create()
kp=sift.detect(gray,None)

img=cv.drawKeypoints(gray,kp,img)

plt.imshow(img)
plt.show()


