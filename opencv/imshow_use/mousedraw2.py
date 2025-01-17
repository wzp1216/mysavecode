import numpy as np
import cv2 as cv

drawing=False
mode=True
#true draw rect; m to curve;
ix,iy=-1,-1

def draw_crilcle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event==cv.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    elif event==cv.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event==cv.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
           cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
           cv.circle(img,(x,y),5,(0,0,255),-1)
            

    if event==cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),50,(255,0,0),-1)

img=np.zeros((512,512,3),np.uint8)
cv.namedWindow('draw')
cv.setMouseCallback('draw',draw_crilcle)

while(1):
    cv.imshow('draw',img)
    k= cv.waitKey(1) & 0xFF
    if k==ord('m'):
        mode=not mode
    elif k==27:
        break

cv.destroyWindow()

