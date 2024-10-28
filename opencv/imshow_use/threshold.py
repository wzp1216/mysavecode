import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot as plt


def test3():
    img=cv.imread("test.jpg",0)
    ret,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
    ret,th2=cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    blur=cv.GaussianBlur(img,(5,5),0)
    ret,th3=cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    imgs=[img,0,th1,img,0,th2,blur,0,th3]
    titles=['original','histogram','global-thre','noise-img','hist','qtsu-thre','gass-filter','hist','ostu-thre']
    for i in range(3):
        plt.subplot(3,3,i*3+1),plt.imshow(imgs[i*3],'gray')
        plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
        plt.subplot(3,3,i*3+2),plt.hist(imgs[i*3].ravel(),256)
        plt.title(titles[i*3+1]),plt.xticks([]),plt.yticks([])
        plt.subplot(3,3,i*3+3),plt.imshow(imgs[i*3+2],'gray')
        plt.title(titles[i*3+2]),plt.xticks([]),plt.yticks([])
    plt.show()





def test2():
    img=cv.imread("./image/test1.jpg",0)
    img=cv.medianBlur(img,5)
    ret,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
    th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
    th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

    title=['origianl','golbal threshold','adaptive mean threshold','adaptive gaussian threshold']
    imgs=[img,th1,th2,th3]

    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(imgs[i],'gray')
        plt.title(title[i])
        plt.xticks([]);plt.yticks([])
    plt.show()



def test1():
    img=cv.imread("test.jpg",0)
    ret,thresh1=cv.threshold(img,127,255,cv.THRESH_BINARY)
    ret,thresh2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
    ret,thresh3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
    ret,thresh4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
    ret,thresh5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

    title=['original image','binary','binary_inv','trunc','tozero','tozero_inv']
    imgs=[img,thresh1,thresh2,thresh3,thresh4,thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(imgs[i],'gray')
        plt.title(title[i])
        plt.xticks([]),plt.yticks([])  #hide the xtiks,yticks number
    plt.show()






test2()
