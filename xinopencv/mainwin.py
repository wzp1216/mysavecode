# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5.QtWidgets import QCheckBox,QLabel,QGraphicsView,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QImage,QPixmap

import cv2 as cv


class my_main_win(QWidget):
    def __init__(self):
        super(my_main_win,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QMainWindow')
        label1=QLabel("main windows test")
        check1=QCheckBox('check box test:',self)
        view=QGraphicsView()
        
        lay=QVBoxLayout()
        lay.addWidget(label1)
        lay.addWidget(check1)
        lay.addWidget(view)
        self.setLayout(lay)

        #add a image;
        img=cv.imread("./test.jpg",cv.IMREAD_GRAYSCALE)
        #res=cv.equalizeHist(img)
        res=cv.cvtColor(img,cv.COLOR_GRAY2BGR)
        cv.putText(res,"text",(10,50),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
        frame=cv.cvtColor(res,cv.COLOR_BGR2RGB)
        h,w,c=frame.shape
        imgshow=QImage(frame,w,h,w*3,QImage.Format_RGB888)
        pix=QPixmap.fromImage(imgshow)
        self.item=QGraphicsPixmapItem(pix)
        self.scene=QGraphicsScene()
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        view.setScene(self.scene)
        view.fitInView(QGraphicsPixmapItem(QPixmap(imgshow)))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w=my_main_win()
    w.show()
    sys.exit(app.exec_())

