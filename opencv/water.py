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

plt.subplot(221),plt.imshow(img,cmap='gray')
plt.subplot(222),plt.imshow(gray,cmap='gray')
plt.subplot(223),plt.imshow(sure_bg,cmap='gray')
plt.subplot(224),plt.imshow(sure_fg,cmap='gray')
plt.show()
