# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog
from PyQt5.QtWidgets import QGridLayout
from mainui import Ui_MainWindow

class mymainwin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mymainwin,self).__init__()
        self.setupUi(self)
        self.setUI()
    def setUI(self):
        self.desktop=QApplication.desktop()
        self.maxheight=self.desktop.height()-20
        self.maxwidth=self.desktop.width()-20
        self.setFixedSize(self.maxwidth,self.maxheight)
        self.statusbar.show()
        self.statusbar.showMessage("Battery Managet Sysem is ready!")
        self.layoutWidget.setGeometry(QRect(40, 20, self.maxwidth-100,self.maxheight-200))
        self.tabWidget.resize(self.maxwidth-40,self.maxheight-60)
