# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
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
        noImg=QImage("./gui/no_img.png")
        imgLab1=QLabel(QPixmap(QImage.fromImage(noImg)))
        lay.addWidget(imgLab1)
        self.setLayout(lay)




