# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1428, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 1291, 941))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.layoutWidget = QtWidgets.QWidget(self.tab1)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 1131, 841))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox1 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox1.setObjectName("groupBox1")
        self.gridLayout.addWidget(self.groupBox1, 0, 0, 1, 1)
        self.groupBox2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox2.setObjectName("groupBox2")
        self.gridLayout.addWidget(self.groupBox2, 0, 1, 1, 1)
        self.groupBox3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox3.setObjectName("groupBox3")
        self.gridLayout.addWidget(self.groupBox3, 1, 0, 1, 1)
        self.groupBox4 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox4.setObjectName("groupBox4")
        self.gridLayout.addWidget(self.groupBox4, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tabWidget.addTab(self.tab2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1428, 35))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
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

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionexit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox1.setTitle(_translate("MainWindow", "电压"))
        self.groupBox2.setTitle(_translate("MainWindow", "电流"))
        self.groupBox3.setTitle(_translate("MainWindow", "温度"))
        self.groupBox4.setTitle(_translate("MainWindow", "SOC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Tab 2"))
        self.menuFIle.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

