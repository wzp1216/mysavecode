
python
{{
    pyqt5中的信号
    {{
         from PyQt5.QtCore import QOject ,pyqtSignal
         class a(QOject):
             mysignal=pyqtSignal(int)
             def send(self):
                 self.mysignal.emit(23);
    ss=a();ss.send()即可以发射23；
    ss.mysignal.connect(p.func);
    则可以将23传到p对象；
     }}

 }}


old_study
{{

about light
{{
光源选型（很重要）
背光源：，提升对比度，漫反射背光，平行背光（用的多，边缘模糊度低）（测量产品尺寸时候）；
同轴光：消除反光，均匀性提高，提升对比度（镀银45度反射）；
非同轴漫射光：测控金属表面；
偏振光：加偏振片，消除反光；
红外光：肉眼不可见，加对比度；
紫外线：黑暗时候荧光与背景对比；
彩色原理：互补色，比如红色照，红色会变淡，蓝色会加深；
色环原理：互补色，同上；
低角度环形光：芯片字迹不清；
条形光：字迹检查；
LIM条形组合光：可以调整角度，大产品尺寸检查；
RID球积分照明：提升对比度，抑制金属反光；
}}
g++ using opencv
{{
g++ example.cpp -o example  $(pkg-config --cflags --libs opencv)
编译exceple.cpp文件

可以用示例中的CMAKELIST  注意期中的文件名换为需要编译的文件；
也可以添加多个文件进行编译
cmake .
make 
可以生成可执行文件；
}}

sample show a jpg 
{{
##############################################################
import sys
import os
import cv2 as cv
from matplotlib import pyplot as plt

if __name__=="__main__":
    print("this is main function:")
    img=cv.imread("board.jpg",cv.IMREAD_COLOR)
    cv.namedWindow('sample',cv.WINDOW_NORMAL)
    
    if img is None:
        sys.exit("file is none!")
    
    cv.line(img,(0,0),(200,200),(255,0,0),10)
    cv.rectangle(img,(100,0),(450,100),(0,255,0),5)
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,'test writing',(20,300),font,4,(0,0,255),3)
    
    cv.imshow("sample",img)
    k=cv.waitKey(0)
    cv.destroyWindow("sample")
'''
    plt.imshow(img,cmap='gray',interpolation='bicubic')
    plt.xticks([]),plt.yticks([])
    plt.show()
'''

##############################################################
import sys
import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def draw_circle(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),20,(255,0,0),-1)

if __name__=="__main__":
    print("this is main function:")
    img=cv.imread("board.jpg",cv.IMREAD_COLOR)
    cv.namedWindow('sample',cv.WINDOW_NORMAL)
    
    if img is None:
        sys.exit("file is none!")
    
    
    cv.imshow("sample",img)

    cv.setMouseCallback('sample',draw_circle)

    while(1):
        cv.imshow('sample',img)
        if cv.waitKey(20)&0xFF==27:    #ESC==27
            break
    cv.destroyWindow("sample")

##############################################################
}}

sample: draw a circle;
{{
import cv2 as cv
import numpy as np

drawing=False
mode=True
ix,iy=-1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event==cv.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        if drawing==True:
            if mode==True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                cv.circle(img,(x,y),r,(0,0,255),-1)
#                cv.circle(img,(x,y),2,(0,0,255),-1)

    elif event==cv.EVENT_LBUTTONUP:
        drawing==False


img=np.zeros((512,512,3),np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1)&0xFF
    if k==ord('m'):
        mode= not mode
    elif k==27:
        break
cv.destroyWindow('image')

##############################################################
}}
sample: RGB trackbar;
{{
滑动条改变着色
import cv2 as cv
import numpy as np

def nothing(x):
    pass

img=np.zeros((512,512,3),np.uint8)
cv.namedWindow('image')

cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

switch='0:OFF\n1:ON'
cv.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv.imshow('image',img)
    r=cv.getTrackbarPos('R','image')
    g=cv.getTrackbarPos('G','image')
    b=cv.getTrackbarPos('B','image')
    s=cv.getTrackbarPos(switch,'image')
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
    k=cv.waitKey(1)&0xFF
    if k==27:
        break

cv.destroyWindow('image')

滑动条改变着色

##############################################################
import cv2 as cv
import numpy as np

if __name__=='__main__':
    img=cv.imread('board.jpg')

    print(img.shape)
    print(img.size)  #number of point
    print(img.dtype)

    #ROI 40,60,---180,120
    chip=img[60:120,40:180]
    img[60:120,340:480]=chip  #copy 2 chip ;
    img[260:320,340:480]=chip
    
    img[:,:,2]=0
    img[:,:,1]=0

    cv.imshow('image',img)
    k=cv.waitKey(0)
    cv.destroyWindow('image')

##############################################################
}}
sample: use pyplot
{{

import cv6 as cv
import numpy as np
from matplotlib import pyplot as plt

if __name__=='__main__':
    BLUE=[255,0,0]
    img=cv.imread('opencv_logo.jpg')

    replicate=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)
#重复最后一行数据；
    reflect=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT)
#镜像；
    reflect101=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT_101)
    wrap=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_WRAP)
#打包 緾
    constant=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)

#常量边缘填充；

    plt.subplot(231),plt.imshow(img,'gray'),plt.title('orginal')
    plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
    plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
    plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect101')
    plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
    plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')
    plt.show()

    k=cv.waitKey(0)
    cv.destroyWindow('image')




##############################################################
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

if __name__=='__main__':
    img=cv.imread('opencv_logo.jpg')
    img1=cv.imread('board.jpg')
    img1=img1[0:100,0:100]

    img2=cv.addWeighted(img,0.7,img1,0.3,0)
    img3=cv.addWeighted(img,0.3,img1,0.7,0)

    plt.subplot(221),plt.imshow(img,'gray'),plt.title("opencv")
    plt.subplot(222),plt.imshow(img1,'gray'),plt.title("b")
    plt.subplot(223),plt.imshow(img2,'gray'),plt.title("add")
    plt.subplot(224),plt.imshow(img3,'gray'),plt.title("opencv")
    plt.show() 

    k=cv.waitKey(0)

}}


opencv python error:
{{
##############################################################
opencv 库引入后 matplotlib 不能使用办法：
apt insatll python3-tk
import matplotlib; matplotlib.use("TkAgg")

#############################################################
当OPENCV SAMPLE FINDFILE ERROR时
export OPENCV_SAMPLES_DATA_PATH=/home/wzp/opencv-4.5.2/samples/data
#############################################################

}}

}}

