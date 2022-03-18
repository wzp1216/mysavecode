import numpy as np
import cv2 as cv
img=cv.imread('./image/home.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift=cv.SIFT_create()

