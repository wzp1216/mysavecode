import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

#img=cv.imread('./image/lena.jpg')
img=cv.imread('./test_img/side/Image_30.jpg')
edges=cv.Canny(img,100,200)
plt.imshow(edges,cmap='gray')
plt.show()