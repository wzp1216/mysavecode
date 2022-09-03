# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget
from PyQt5.QtWidgets import QCheckBox,QLabel,QGraphicsView,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QImage,QPixmap

import cv2 as cv


class my_main_win(QMainWindow):
    def __init__(self):
        super(my_main_win,self).__init__()
        self.initUI()
        self.addmenu()

    def initUI(self):
        #set title and add label1  check1  view
        centerwidget=QWidget()
        self.setWindowTitle('QMainWindow')
        label1=QLabel("main windows test")
        check1=QCheckBox('check box test:',self)
        view=QGraphicsView()
        
        lay=QVBoxLayout()
        lay.addWidget(label1)
        lay.addWidget(check1)
        lay.addWidget(view)
        centerwidget.setLayout(lay)
        self.setCentralWidget(centerwidget)
        

        #add a image;
        img=cv.imread("./gui/zjipc.png",cv.IMREAD_GRAYSCALE)
        #res=cv.equalizeHist(img)
        res=cv.cvtColor(img,cv.COLOR_GRAY2BGR)
        cv.putText(res,"text",(10,50),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
        frame=cv.cvtColor(res,cv.COLOR_BGR2RGB)
        h,w,c=frame.shape
        imgshow=QImage(frame,w,h,w*3,QImage.Format_RGB888)
        pix=QPixmap.fromImage(imgshow)
        self.item=QGraphicsPixmapItem(pix)
        self.scene=QGraphicsScene()
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        view.setScene(self.scene)
        view.fitInView(QGraphicsPixmapItem(QPixmap(imgshow)))


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

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFIle.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


       


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w=my_main_win()
    w.show()
    sys.exit(app.exec_())
