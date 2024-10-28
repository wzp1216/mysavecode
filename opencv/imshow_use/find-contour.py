import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 


img=cv.imread("./image/star.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(gray,127,255,0)

contours,hieracy=cv.findContours(thresh,2,1)
cnt=contours[0]

print("hieracy")
print(hieracy)


hull=cv.convexHull(cnt,returnPoints=False)


defects=cv.convexityDefects(cnt,hull)
#cv.convexityDefects(cnt,hull,defects)

for i in range(defects.shape[0]):
    s,e,f,d=defects[i,0]
    start=tuple(cnt[s][0])
    end=tuple(cnt[e][0])
    far=tuple(cnt[f][0])
    cv.line(img,start,end,[0,255,0],2)
    cv.circle(img,far,5,[0,0,255],-1)

print(start,end,far,d)

plt.imshow(img);
plt.show()
'''
cv.namedWindow('img',cv.WINDOW_NORMAL)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
'''

