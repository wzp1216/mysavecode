import cv2 as cv
import numpy as np
import sys
img = cv.imread('aaa.png')
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sobelx = cv.Sobel(grey, cv.CV_32F, 1, 0)
# find minimum and maximum intensities
minVal = np.amin(sobelx)
maxVal = np.amax(sobelx)
draw = cv.convertScaleAbs(
    sobelx, alpha=255.0/(maxVal - minVal), beta=-minVal * 255.0/(maxVal - minVal))
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
cv.imshow('image', draw)
cv.waitKey()

