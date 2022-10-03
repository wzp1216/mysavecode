#!/home/wzp/anaconda3/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont 

#读取TIME；看时间是否到21；

class Test1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('使用提醒')
        self.label1=QLabel("现在不在使用时间")
        self.setCentralWidget(self.label1)
        self.show()

if __name__=='__main__':
    t=time.localtime(time.time())
    thour=t.tm_hour
    if (thour>0 and thour<8) or (thour>21 and thour<=24):
        app = QApplication(sys.argv)
        font=QFont()
        font.setPointSize(24); 
        app.setFont(font); 
        ex=Test1()
        os.system("echo 'wzy091030' | sudo -S shutdown -a +4")
        sys.exit(app.exec_())


