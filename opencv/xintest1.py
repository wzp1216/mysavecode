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
    cv.imshow("img",imga)

def gass(img):
    img_gass=cv.GaussianBlur(img,5,5,None,None)
    return img_gass


def main():
    imgs=cv.imread("./image/test1.jpg")
    show(imgs)
    for img in imgs:
        imggass=gass(img)
        show(imggass)



if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
