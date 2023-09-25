import cv2 as cv
import numpy as np

#img=cv.imread('./opencv_logo.jpg')
img=cv.imread('./image/lena.jpg')
imgray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(imgray,197,255,0)
contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cv.namedWindow('imgray')
cv.imshow('imgray',imgray)
#cv.imshow('contours',contours)
#cv.imshow('hierarchy',hierarchy)
#img2=cv.drawContours(img,contours,3,(0,255,0),3)
img2=cv.drawContours(imgray,contours,-1,(0,255,0),3)
cv.namedWindow('img2')
cv.imshow('img2',img2)
cv.waitKey()
cv.destroyAllWindows()

