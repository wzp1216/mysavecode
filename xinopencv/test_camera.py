# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5.QtWidgets import QVBoxLayout,QLabel
from PyQt5 import Qt,QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage,QPixmap
import cv2 as cv

class test_camera(QWidget):
    def __init__(self):
        super(test_camera,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("test_camera")
        label1=QLabel("test the camera!")
        lay=QVBoxLayout()
        lay.addWidget(label1)
        self.setLayout(lay)

       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w=test_camera()
    w.show()
    sys.exit(app.exec_())

