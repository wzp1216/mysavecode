# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget
from PyQt5.QtWidgets import QCheckBox,QLabel,QGraphicsView,QGraphicsScene,QGraphicsPixmapItem,QGroupBox,QTextBrowser
from PyQt5.QtWidgets import QVBoxLayout,QGridLayout
from PyQt5.QtGui import QImage,QPixmap,QFont

import cv2 as cv
## 4 image;
## top image;
## result_dlg


class main_dlg(QWidget):
    def __init__(self,wsize,hsize):
        super(main_dlg,self).__init__()
        self.width=wsize; self.height=hsize;
        print("main_dlg wsize:",wsize,hsize)
        self.init()

    def init(self):
        testimg=cv.imread('./gui/test.png')
        frame=cv.cvtColor(testimg,cv.COLOR_BGR2RGB)
        h,w,c=frame.shape
        frame=QImage(frame,w,h,3*w,QImage.Format_RGB888)
        pix=QPixmap.fromImage(frame)
        lay=QGridLayout();    lay.setSpacing(10)
        scence1=QGraphicsScene();scence2=QGraphicsScene();scence3=QGraphicsScene()
        self.view1=QGraphicsView(scence1); self.view2=QGraphicsView(scence2); self.view3=QGraphicsView(scence3);
        lay.addWidget(self.view1,0,1);lay.addWidget(self.view2,0,2);lay.addWidget(self.view3,0,3)
        scence1.addPixmap(pix);
        scence2.addPixmap(pix);
        scence3.addPixmap(pix);
        scence4=QGraphicsScene();scence5=QGraphicsScene();
        self.view4=QGraphicsView(scence4); self.view5=QGraphicsView(scence5); 
        lay.addWidget(self.view4,1,1);lay.addWidget(self.view5,1,2);
        scence4.addPixmap(pix);
        scence5.addPixmap(pix);

        lab_msg=QTextBrowser()
        font=QFont();   font.setFamily("黑体");    font.setPointSize(10)
        lab_msg.setFont(font)
        lab_msg.setFixedHeight(60)
        lab_msg.setText("system is start...")
        lab_msg.append("系统启动正常...")
        lab_msg.append("显示图片正常...")
        lay.addWidget(lab_msg,2,0,1,4)
        self.setLayout(lay)




