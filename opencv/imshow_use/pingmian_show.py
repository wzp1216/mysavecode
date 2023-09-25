import cv2 as cv
import numpy as np
lena=cv.imread("./image/lena.jpg",0)
cv.imshow('lean',lena)
r,c=lena.shape
x=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i]=2**i

r=np.zeros((r,c,8),dtype=np.uint8)

for i in range(8):
    r[:,:,i]=cv.bitwise_and(lena,x[:,:,i])
    mask=r[:,:,i]>0
    r[mask]=255
    cv.imshow(str(i),r[:,:,i])

cv.waitKey(),cv.destroyAllWindows()

