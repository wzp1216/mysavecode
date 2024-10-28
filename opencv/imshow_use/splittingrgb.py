import sys
import numpy as np
import cv2 as cv


img=cv.imread('./lena.jpg')

b,g,r=cv.split(img)

cv.imshow('img',img)
cv.imshow('r',r)
cv.imshow('g',g)
cv.imshow('b',b)


cv.waitKey(0)
cv.destroyAllWindows()


