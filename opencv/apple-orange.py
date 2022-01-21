import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt

a=cv.imread('apple.jpg')
channel=a.shape
if channel[2]==3:
    b,g,r=cv.split(a)
    a=cv.merge([r,g,b])

b=cv.imread('orange.jpg')
channel=b.shape
if channel[2]==3:
    b,g,r=cv.split(b)
    b=cv.merge([r,g,b])

G=a.copy()
gpA=[G]

for i in range(6):
    G=cv.pyrDown(G)
    gpA.append(G)

G=b.copy()
gpB=[G]
for i in range(6):
    G=cv.pyrDown(G)
    gpB.append(G)

lpA=[gpA[5]]
for i in range(5,0,-1):
    GE=cv.pyrUp(gpA[i])
    L=cv.subtract(gpA[i-1],GE)
    lpA.append(L)

lpB=[gpB[5]]
for i in range(5,0,-1):
    GE=cv.pyrUp(gpB[i])
    L=cv.subtract(gpB[i-1],GE)
    lpB.append(L)
LS=[]
for la,lb in zip(lpA,lpA):
    rows,cols,dpt=la.shape
    ls=np.hstack((la[:,0:cols//2],lb[:,cols//2:]))
    LS.append(ls)

ls_=LS[0]
for i in range(1,6):
    ls_=cv.pyrUp(ls_)
    ls_=cv.add(ls_,LS[i])

real=np.hstack((a[:,0:cols//2],b[:,cols//2:]))

cv.imwrite('pyramid-blending.jpg',ls_)
cv.imwrite('direct-blending.jpg',real)

plt.subplot(2,2,1),plt.imshow(a,cmap='viridis')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(b,cmap='viridis')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(ls_,cmap='viridis')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(real,cmap='viridis')
plt.xticks([]),plt.yticks([])

plt.show()

