
import cv2
lena=cv2.imread("lena.jpg")
gray=cv.cvtColor(lena,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
print("lena.shape:",lena.shape)
print("gray.shape:",gray.shape)
print("rgb.shape:",rgb.shape)
cv2.imshow("lena",lena)
cv2.imshow("gray",gray)
cv2.imshow("rgb",rgb)
cv2.waitKey()
cv2.destroAllWindows()








'''
import cv2
import numpy as np
img=np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rst=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print("img=",img)
print("rst=",rst)
print("img[1,0]=",img[1,0,0]*0.114+img[1,0,1]*0.587+img[1,0,2]*0.299)
print("cv2.color_bgr2gray:img[1,0]=",rst[1,0])
'''


