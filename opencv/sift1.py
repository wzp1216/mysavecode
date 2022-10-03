import numpy as np
import cv2 as cv
img=cv.imread('./image/home.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
<<<<<<< HEAD
sift=cv.SIFT_create()
=======
sift=cv.xfeatures2d.SIFT_create()
>>>>>>> b24a16190fc6175294f270c1f425eeddb4b7f453

