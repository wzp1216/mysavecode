import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use('tkAgg')

from matplotlib import pyplot as plt


img=cv.imread('./image/test.jpg')
img2=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

plt.subplot(2,2,1)
plt.imshow(img2,'gray')
plt.subplot(2,2,2)
plt.hist(img2.ravel(),256,[0,255]);

img1=cv.imread('./image/test.jpg')
plt.subplot(2,2,3)
plt.imshow(img1)


plt.subplot(2,2,4)
color=('b','g','r')
for i,col in enumerate(color):
    hist=cv.calcHist([img1],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()



