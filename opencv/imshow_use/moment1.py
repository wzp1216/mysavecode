import cv2 as cv
import numpy as np

img=cv.imread("./image/stuff.jpg",0)
#cv.imshow("img",img)
ret,thresh=cv.threshold(img,160,255,0)
contours,hierarchy=cv.findContours(thresh,1,2)

#print(contours)

cnt=contours[0]
M=cv.moments(cnt)
print(M)
cx=int(M['m10']/M['m00'])
cy=int(M['m01']/M['m00'])
print(cx,",",cy)

area=cv.contourArea(cnt)
print(area)

perimeter=cv.arcLength(cnt,True)
print(perimeter)



#cv.drawContours(img,contours,-1,(0,255,0),3)
#cv.imshow("contours",img)
#cv.waitKey()


