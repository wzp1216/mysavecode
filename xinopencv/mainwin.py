# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QCheckBox 


class my_main_win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        cb=QCheckBox('Show titel',self)
        cb.move(20,20)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QCheckBox')
        self.show()



