import cv2 as cv
import numpy as np
import argparse
import random 
random.seed(12345)

def thresh_callback(val):
    threshold=val

    canny_output=cv.Canny(src_gray,threshold,threshold*2)
    contours,_=cv.findContours(canny_output,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    hull_list=[]
    for i in range(len(contours)):
        hull=cv.convexHull(contours[i])
        hull_list.append(hull)

    drawing=np.zeros((canny_output.shape[0],canny_output.shape[1],3),dtype=np.uint8)
    for i in range(len(contours)):
        color=(random.randint(0,256),random.randint(0,256),random.randint(0,255))
        cv.drawContours(drawing,contours,i,color)
        cv.drawContours(drawing,hull_list,i,color)
    cv.imshow('contours',drawing)


src=cv.imread(cv.samples.findFile('stuff.jpg'))
if src is None:
    print('Could not open file')
    exit(0)
src_gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
src_gray=cv.blur(src_gray,(3,3))


win='source'
cv.namedWindow(win)
cv.imshow(win,src)
max_thresh=255
thresh=100
cv.createTrackbar('canny-thresh:',win,thresh,max_thresh,thresh_callback)
thresh_callback(thresh)

cv.waitKey()

        
