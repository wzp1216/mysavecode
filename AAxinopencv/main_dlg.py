# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget
from PyQt5.QtWidgets import QCheckBox,QLabel,QGraphicsView,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.QtWidgets import QVBoxLayout,QGridLayout
from PyQt5.QtGui import QImage,QPixmap

import cv2 as cv
## 4 image;
## top image;
## result_dlg

class main_dlg(QWidget):
    def __init__(self):
        super(main_dlg,self).__init__()
        self.init()

    def init(self):
        lay=QGridLayout()
        lay.setSpacing(10)
        img1=QImage("./gui/no_img.png")
        imgLab1=QLabel()
        imgLab1.setFixedSize(400,400)
        img1=img1.scaled(400,400,Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        imgLab1.setPixmap(QPixmap.fromImage(img1))
        lay.addWidget(imgLab1,0,0,1,1)
        imgLab2=QLabel()
        imgLab2.setPixmap(QPixmap.fromImage(img1))
        lay.addWidget(imgLab2,0,1,1,1)
        imgLab3=QLabel()
        imgLab3.setPixmap(QPixmap.fromImage(img1))
        lay.addWidget(imgLab3,1,0,1,1)
        imgLab4=QLabel()
        imgLab4.setPixmap(QPixmap.fromImage(img1))
        lay.addWidget(imgLab4,1,1,1,1)
        imgLab_top=QLabel()
        imgLab_top.setPixmap(QPixmap.fromImage(img1))
        lay.addWidget(imgLab_top,0,2,1,1)
        lab_msg=QLabel("system is start...")
        lay.addWidget(lab_msg,2,0,1,3)
        self.setLayout(lay)





