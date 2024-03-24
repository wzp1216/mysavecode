# coding=utf-8
import sys
from PyQt5.QtGui import *
from PyQt5.Qt import *
from mainwin import Myapp


if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setStyleSheet(open('setting/AMOLED.qss',encoding='utf-8').read())
    win1=Myapp()
    win1.show()
    sys.exit(app.exec_())
