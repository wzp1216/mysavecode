# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget



class mainwin(QMainWindow):
    def __init__(self, parent=None):
        super(mainwin, self).__init__(parent)
        self.setObjectName("MainWindow")
        screen = QDesktopWidget().screenGeometry()
        high = screen.height()
        width = screen.width()
        self.resize(width * 5 // 6, high * 5 // 6)
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))
        self.init()
        self.addmenu()

    def init(self):
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
    mywin = mainwin()
    mywin.show()
    sys.exit(app.exec_())
