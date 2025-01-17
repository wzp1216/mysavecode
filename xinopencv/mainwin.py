# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5 import Qt,QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget
from PyQt5.QtWidgets import QCheckBox,QLabel,QGraphicsView,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QImage,QPixmap

import cv2 as cv

#from test_camera import *

class my_main_win(QMainWindow):
    def __init__(self):
        super(my_main_win,self).__init__()
        self.initUI()
        self.addmenu()

    def initUI(self):
        #set title and add label1  check1  view
        centerwidget=QWidget()
        self.setWindowTitle('QMainWindow')
        label1=QLabel("show a important message!")
        check1=QCheckBox('check box test:',self)
        view=QGraphicsView()
        lay=QVBoxLayout()
        lay.addWidget(label1)
        lay.addWidget(check1)
        lay.addWidget(view)
        centerwidget.setLayout(lay)
        self.setCentralWidget(centerwidget)
        

        #add a image;
        img=cv.imread("./test.jpg",cv.IMREAD_GRAYSCALE)
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
        self.menubar.setObjectName("menuMain")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools= QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
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
        self.action_test_camera=QtWidgets.QAction(self)
        self.action_test_camera.setObjectName("action_test_camera")
        self.actionHelp = QtWidgets.QAction(self)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionexit)
        self.menuTools.addAction(self.action_test_camera)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.action_test_camera.setText(_translate("MainWindow", "Test_camera"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
#add connect action
        self.action_test_camera.triggered.connect(self.test_camera)
        self.actionexit.triggered.connect(self.close)
    def test_camera(self):
        pass
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w=my_main_win()
    w.show()
    sys.exit(app.exec_())

