import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt

fname=sys.argv[1]
img=cv.imread(fname)

r,g,b=cv.split(img)
arg=(r+g+b)/3
img1=cv.merge((arg,arg,arg))

gray1=cv.imread(fname,0)

plt.subplot(2,2,1),plt.imshow(img)
plt.subplot(2,2,2),plt.imshow(arg,"gray")
plt.subplot(2,2,3),plt.imshow(gray1,"gray")


plt.show()


