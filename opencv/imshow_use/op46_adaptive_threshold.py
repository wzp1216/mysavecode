import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img=cv.imread("./image/sudoku.png",0)
img=cv.medianBlur(img,5)

ret,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)

th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

plt.subplot(2,2,1),plt.imshow(img,'gray')
plt.subplot(2,2,2),plt.imshow(th1,'gray')
plt.subplot(2,2,3),plt.imshow(th2,'gray')
plt.subplot(2,2,4),plt.imshow(th3,'gray')


plt.show()


