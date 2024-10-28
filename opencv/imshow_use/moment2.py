import cv2 as cv
import numpy as np

img=cv.imread("./image/stuff.jpg",0)
cv.imshow("img",img)
ret,thresh=cv.threshold(img,100,255,0)
contours,hierarchy=cv.findContours(thresh,1,2)



cnt=contours[0]

x,y,w,h=cv.boundingRect(cnt)
img=cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow("contours",img)

cv.waitKey(),cv.destroyAllWindows()


