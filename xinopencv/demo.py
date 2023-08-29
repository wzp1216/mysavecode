# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5 import Qt,QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage,QPixmap
import cv2 as cv

       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w=my_main_win()
    w.show()
    sys.exit(app.exec_())

