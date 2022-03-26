import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('./image/sudoku.png',0)
img=cv.medianBlur(img,5)

ret,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)

th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)


title=['original', 'global threshold', 'adaptiveThreshold mean' ,'adaptiveThreshold gaussian']
imgs=[img,th1,th2,th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(imgs[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

print(ret)

plt.show()



