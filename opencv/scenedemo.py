import cv2 as cv


import sys 
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QGraphicsScene,QGraphicsView
from PyQt5.QtGui import QImage,QPixmap

class scenedemo(QWidget):
    def __init__(self):
        super().__init__()

        img=cv.imread("./image/test1.jpg")
        h,w,d=img.shape
        cvimg=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        qimg=QImage(cvimg.data,w,h,w*d,QImage.Format_RGB888)
        pix=QPixmap.fromImage(qimg).scaled(300,200)

        self.resize(800,800)
        self.label1=QLabel("tests")
        self.scene=QGraphicsScene()
        #self.scene.setSceneRect(0,0,1000,1000)
        self.scene.addPixmap(pix)
        self.view1=QGraphicsView()
        self.view1.resize(400,400)
        self.view1.setScene(self.scene)
        self.view2=QGraphicsView()
        self.view2.resize(300,300)
        self.view2.setScene(self.scene)
        


        lay=QVBoxLayout()
        lay.addWidget(self.label1)
        lay.addWidget(self.view1)
        lay.addWidget(self.view2)
        self.setLayout(lay)
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    w=scenedemo()
    w.show()
    sys.exit(app.exec_())


