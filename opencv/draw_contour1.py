import numpy as np
import cv2 as cv

img=cv.imread("./image/test.jpg")
imgray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(imgray,170,255,0)
contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

out=cv.drawContours(img,contours,-1,(0,255,0),3)
cv.imshow("out",out)
cv.waitKey()
cv.destroyAllWindows()


