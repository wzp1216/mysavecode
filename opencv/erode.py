import cv2 as cv
import numpy as np
import matplotlib 
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

def test1():
    img=cv.imread("./image/opencv_logo.jpg",0)
    kernel=np.ones((5,5),np.uint8)
    erosion=cv.erode(img,kernel,iterations=1)
    dilation=cv.dilate(img,kernel,iterations=1)
    plt.subplot(1,3,1),plt.imshow(img,'gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(1,3,2),plt.imshow(erosion,'gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(1,3,3),plt.imshow(dilation,'gray')
    plt.xticks([]),plt.yticks([])
    plt.show()


test1()
