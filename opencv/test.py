import sys
import numpy as np
import cv2 as cv



def nothing(x):
    pass

img=np.zeros((300,512,3),np.uint8)
cv.namedWindow('img')


cv.createTrackbar('R','img',0,255,nothing)
cv.createTrackbar('G','img',0,255,nothing)
cv.createTrackbar('B','img',0,255,nothing)

switch='0: OFF \n1 :ON'
cv.createTrackbar(switch,'img',0,1,nothing)

while(1):
    cv.imshow('img',img)
    k=cv.waitKey(1) & 0xFF
    if k==27: break

    r=cv.getTrackbarPos('R','img')
    g=cv.getTrackbarPos('G','img')
    b=cv.getTrackbarPos('B','img')
    s=cv.getTrackbarPos(switch,'img')

    if s==0: img[:]=0
    else:
        img[:]=[b,g,r]




