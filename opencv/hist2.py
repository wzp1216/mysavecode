import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use('tkagg')

import matplotlib.pyplot as plt

img=cv.imread('./image/test1.jpg',0)
#equ=cv.equalizeHist(img)
#res=np.hstack((img,equ))

clahe=cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
res=clahe.apply(img)

plt.subplot(1,2,1),plt.imshow(img,'gray')
plt.subplot(1,2,2),plt.imshow(res,'gray')

plt.show()





'''
img=cv.imread('./image/lena.jpg',0)
#img=cv.imread('./image/lena.jpg',1)
#  1  read rgb   0--> read gray 

mask=np.zeros(img.shape[:2],np.uint8)
mask[100:300,100:400]=255
maskimg=cv.bitwise_and(img,img,mask=mask)

hist_full=cv.calcHist([img],[0],None,[256],[0,256])
hist_mask=cv.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(2,2,1),plt.imshow(img,'gray')
plt.subplot(2,2,2),plt.imshow(mask,'gray')
plt.subplot(2,2,3),plt.imshow(maskimg,'gray')
plt.subplot(2,2,4),plt.plot(hist_full),plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()
'''




