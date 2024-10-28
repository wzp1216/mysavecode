#!/usr/bin/env python
# coding=utf-8
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Test Image')
    label = QLabel(w)
    pixmap = QPixmap('./test.jpg')
    label.setPixmap(pixmap)
    w.resize(pixmap.width(),pixmap.height())
    w.show()
    sys.exit(app.exec_())
