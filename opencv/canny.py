import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('test.jpg')
edges=cv.Canny(img,100,200)
plt.imshow(edges,cmap='gray')
plt.show()
