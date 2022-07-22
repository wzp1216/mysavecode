import cv2 as cv
import numpy as np


def test():
    img=cv.imread("test.jpg")
    cv.imshow("a",img)
    for i in range(5,49,2):
        img1=cv.medianBlur(img,i)
    cv.imshow("b",img1)


e1=cv.getTickCount()
test()
e2=cv.getTickCount()
time=(e2-e1)/cv.getTickFrequency()
print("this time is ",time)
cv.waitKey()
cv.destroyAllWindows()
