import  cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("./image/lena.jpg")
print(img.size)
print(type(img))

plt.imshow(img)
plt.show()


