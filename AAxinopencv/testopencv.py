import cv2 as cv
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt



print(cv.__version__)
img=cv.imread("/home/wzp/lena.jpg")
plt.imshow(img)
plt.show()




