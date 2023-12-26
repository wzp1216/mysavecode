# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget
from PyQt5.QtWidgets import QCheckBox,QLabel,QGraphicsView,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QImage,QPixmap

from main_dlg import main_dlg

##主窗口；
##MENU：
##FILE  
##设置
##检测
##工具
##HELP：help  about about Qt;
##工具栏
## main_dlg; 5 image; result; message;
##状态栏

#import appstart


class my_main_win(QMainWindow):
    def __init__(self):
        super(my_main_win,self).__init__()
        self.initUI()
        self.addmenu()

    def initUI(self):
        #set title and add label1  check1  view
        screen=app.primaryScreen()
        w=screen.size().width()-40
        h=screen.size().height()-60
        mainDlg=main_dlg(w,h)
        self.setCentralWidget(mainDlg)
        self.show()
        

    def addmenu(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(self)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(self)
        self.actionsave.setObjectName("actionsave")
        self.actionexit = QtWidgets.QAction(self)
        self.actionexit.setObjectName("actionexit")
        self.actionHelp = QtWidgets.QAction(self)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionopen)
        self.menuFIle.addAction(self.actionsave)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionexit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionexit.triggered.connect(self.close)

        _tr= QtCore.QCoreApplication.translate
        self.setWindowTitle(_tr("MainWindow","瑕疵检测系统zjipc_0.1"))
        self.menuFIle.setTitle(_tr("MainWindow","File"))
        self.menuHelp.setTitle(_tr("MainWindow","Help"))
        self.actionopen.setText(_tr("MainWindow","open"))
        self.actionsave.setText(_tr("MainWindow","save"))
        self.actionexit.setText(_tr("MainWindow","exit"))
        self.actionHelp.setText(_tr("MainWindow","Help"))
        self.actionAbout.setText(_tr("MainWindow","About"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w=my_main_win()
    screen=app.primaryScreen()
    w.resize(screen.size())
    w.move(0,0)
    w.show()
    sys.exit(app.exec_())

