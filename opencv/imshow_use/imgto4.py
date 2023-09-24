import cv2 as cv
import numpy as np
import sys
import matplotlib 
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

a=cv.imread('zjipc.png')
G=a
for i in range(3):
    G=cv.pyrDown(G)
    cv.imshow('g',G)
    cv.waitKey()

cv.imwrite('zjipc1.png',G)


cv.waitKey()
cv.destroyAllWindows()



