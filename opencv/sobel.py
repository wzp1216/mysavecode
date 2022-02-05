import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt


def test1():
    img=cv.imread("./image/lena.jpg",0)
    sobel1=cv.Sobel(img,cv.CV_8U,1,0,ksize=5)
    sobel2=cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
    abs_sobel=np.absolute(sobel2)
    sobel8=np.uint8(abs_sobel)

    plt.subplot(2,2,1),plt.imshow(img,'gray')
    plt.title('original'),plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(sobel1,'gray')
    plt.title('soble1'),plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobel2,'gray')
    plt.title('sobel2'),plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobel8,'gray')
    plt.title('sobel8'),plt.xticks([]),plt.yticks([])

    plt.show()



def test():
    img=cv.imread("./image/lena.jpg",0)
    laplacian=cv.Laplacian(img,cv.CV_64F)
    sobelx=cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
    sobely=cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

    plt.subplot(2,2,1),plt.imshow(img,'gray')
    plt.title('original'),plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,'gray')
    plt.title('laplacian'),plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,'gray')
    plt.title('sobelx'),plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,'gray')
    plt.title('sobely'),plt.xticks([]),plt.yticks([])

    plt.show()





test1()
