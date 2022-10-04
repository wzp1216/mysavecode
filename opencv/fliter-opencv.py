import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot as plt


def test():
    img=cv.imread("./image/opencv_logo.jpg")
    kernel=np.ones((5,5),np.float32)/25
    dst=cv.filter2D(img,-1,kernel)
    blur=cv.blur(img,(5,5))
    gass=cv.GaussianBlur(img,(5,5),0)

    plt.subplot(2,2,1),plt.imshow(img),plt.title('origin')
    plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(dst),plt.title('averaging')
    plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(blur),plt.title('blur')
    plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(gass),plt.title('gass')
    plt.xticks([]),plt.yticks([])
    plt.show()




test()
