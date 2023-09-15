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
        self.init()

    def init(self):
        labw=(self.width-100)/3;labh=(self.height-260)/2;
        noimg=cv.imread('./gui/no_img.png')
        frame=cv.cvtColor(noimg,cv.COLOR_BGR2RGB)
        h,w,c=frame.shape
        frame=QImage(frame,w,h,3*w,QImage.Format_RGB888)
        pix=QPixmap.fromImage(frame)
        font=QFont();   font.setFamily("黑体");    font.setPointSize(14)
        lay=QGridLayout();    lay.setSpacing(10)
        self.view1=QLabel();self.view1.setFixedWidth(labw);self.view1.setFixedHeight(labh);
        self.view1.setPixmap(pix);        self.view1.setScaledContents(True)
        lay.addWidget(self.view1,0,0,1,1)
        self.view2=QLabel();self.view2.setFixedWidth(labw);self.view2.setFixedHeight(labh);
        self.view2.setPixmap(pix);        self.view2.setScaledContents(True)
        lay.addWidget(self.view2,0,1,1,1)
        self.view3=QLabel();self.view3.setFixedWidth(labw);self.view3.setFixedHeight(labh);
        self.view3.setPixmap(pix);        self.view3.setScaledContents(True)
        lay.addWidget(self.view3,1,0,1,1)
        self.view4=QLabel();self.view4.setFixedWidth(labw);self.view4.setFixedHeight(labh);
        self.view4.setPixmap(pix);        self.view4.setScaledContents(True)
        lay.addWidget(self.view4,1,1,1,1)
        self.view5=QLabel();self.view5.setFixedWidth(labw);self.view5.setFixedHeight(labh);
        self.view5.setPixmap(pix);        self.view5.setScaledContents(True)
        lay.addWidget(self.view5,0,2,1,1)

        font=QFont();   font.setFamily("黑体");    font.setPointSize(14)
        lab_msg=QTextBrowser()
        ##lab_msg.setFixedHeight(120)
        lab_msg.setFont(font)
        lab_msg.setText("system is start...\n")
        lay.addWidget(lab_msg,2,0,1,3)
        self.setLayout(lay)




