import cv2 as cv
import numpy as np


def line_detection(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    edges=cv.Canny(gray,50,150,apertureSize=3)
    #lines=cv.HoughLines(edges,1,np.pi/180,200)
    lines=cv.HoughLines(edges,1,np.pi/180,150,None,0,0)
    for line in lines:
        rho,theta=line[0]
        a=np.cos(theta)
        b=np.sin(theta)
        x0=a*rho
        y0=b*rho
        x1=int(x0+1000*(-b))
        y1=int(y0+1000*(a))
        x2=int(x0-1000*(-b))
        y2=int(y0-1000*(a))
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),3)
    cv.namedWindow('img_line')
    cv.imshow('img_line',img)


img=cv.imread('./image/sudoku.png')
line_detection(img)
cv.waitKey()
cv.destroyAllwindows()





