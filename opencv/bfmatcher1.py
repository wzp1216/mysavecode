import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img1=cv.imread('./image/box.png')
img2=cv.imread('./image/box_in_scene.png')

orb=cv.ORB_create()
kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img2,None)

bf=cv.BFMatcher(cv.NORM_HAMMING,crossCheck=True)

matches=bf.match(des1,des2)
matches=sorted(matches,key=lambda x:x.distance)
# must sorted !!!

img3=cv.drawMatches(img1,kp1,img2,kp2,matches[:20],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.imshow(img3),plt.show()


