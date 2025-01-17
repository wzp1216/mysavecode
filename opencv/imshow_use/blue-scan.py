import cv2 as cv
import numpy as np


img=cv.imread("./image/lena.jpg")
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

low_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])
low_blue=np.array([0,0,0])
upper_blue=np.array([30,255,255])

mask=cv.inRange(hsv,low_blue,upper_blue)

res=cv.bitwise_and(img,img,mask=mask)

cv.imshow('frame',img)
cv.imshow('mask',mask)
cv.imshow('res',res)


cv.waitKey()
cv.destroyAllWindows()

