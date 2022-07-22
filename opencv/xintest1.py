#!/usr/bin/env python

'''
1.show test img;
2.gass filter
3.find IO,and draw
4.scrach test 
'''

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os
import sys


def show(imga):
    imgstr=str(imga)
    cv.imshow(imgstr,imga)

def gass(img)
    cv.GaussianBlur(img,5,5,None,None)

def main():
    imgs=cv.imread('./test_img/side/Image_29.jpg')
    show(imgs)
    for img in imgs:
        imggass=gass(img)
        show(imggass)



if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
