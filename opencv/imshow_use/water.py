import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread('../opencv452help/4.5.2/water_coins.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)


kernel=np.ones((3,3),np.uint8)
opening=cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel,iterations=2)
sure_bg=cv.dilate(opening,kernel,iterations=3)

dist_transform=cv.distanceTransform(opening,1,5)
ret,sure_fg=cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

sure_fg=np.uint8(sure_fg)
unknow=cv.subtract(sure_bg,sure_fg)

ret,markers1=cv.connectedComponents(sure_fg)
markers=markers1+1
markers[unknow==255]=0
markers3=cv.watershed(img,markers)
img1=gray
img1[markers3==-1]==[255,0,0]

xx=cv.subtract(gray,img1)
plt.imshow(xx)
plt.show()

plt.subplot(231),plt.imshow(gray)
plt.subplot(232),plt.imshow(img1)
plt.subplot(233),plt.imshow(sure_bg,cmap='gray')
plt.subplot(234),plt.imshow(sure_fg,cmap='gray')
plt.subplot(235),plt.imshow(unknow,cmap='gray')
plt.subplot(236),plt.imshow(dist_transform,cmap='gray')
plt.show()
