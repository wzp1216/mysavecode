import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img =cv.imread('../opencv452help/4.5.2/water_coins.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
res, thresh =cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

#plt.imshow(res),plt.show()


