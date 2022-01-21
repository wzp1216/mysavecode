import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def test1():
    img=cv.imread("test.jpg",0)
    rows,cols=img.shape
    m=cv.getRotationMatrix2D((cols/2,rows/2),90,1.5)
    img2=cv.warpAffine(img,m,(2*cols,2*rows))
    while(1):
        cv.imshow("roate",img2)
        if cv.waitKey(1)&0xFF==27:break
    cv.destroyAllWindows()

def test2():
    img=cv.imread("test.jpg")
    rows,cols,ch=img.shape
    ps1=np.float32([[50,50],[200,50],[50,200]])
    ps2=np.float32([[10,100],[200,50],[100,200]])
    m=cv.getAffineTransform(ps1,ps2)
    dst=cv.warpAffine(img,m,(cols,rows))
    plt.subplot(1,2,1)
    plt.imshow(img);plt.title('input')
    plt.subplot(1,2,2)
    plt.imshow(dst);plt.title('output')
    plt.show()

def testmat():
    x=np.arange(1,11)
    y=2*x
    plt.title("test")
    plt.plot(x,y)
    plt.show()

if __name__=="__main__":
    test2()


