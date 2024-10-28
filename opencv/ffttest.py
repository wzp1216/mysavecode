import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


img=cv.imread('./image/messi5.jpg',0)
f=np.fft.fft2(img)
fshit=np.fft.fftshift(f)

magnitude_spectrum=20*np.log(np.abs(fshit))

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Input image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum,cmap='gray')
plt.title('magnitude_spectrum'),plt.xticks([]),plt.yticks([])

plt.show()

