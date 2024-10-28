# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '单独设置阈值对话框.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import json
import multiprocessing
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow

global value_duan
value_duan = 70
global value_ce
value_ce = 38
global min_duan
min_duan = 120
global min_ce
min_ce = 120
global block
block = 16


class Ui_Dialog(object):
    def setupUi2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 199)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(130, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(530, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(130, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(240, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(530, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 150, 171, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 150, 171, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 150, 191, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.set_needed_value)
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_3.clicked.connect(Dialog.get_needed_value)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def get_needed_value(self):
        self.textEdit.setText(str(value_duan))
        self.textEdit_2.setText(str(min_duan))
        self.textEdit_3.setText(str(value_ce))
        self.textEdit_5.setText(str(min_ce))
        self.textEdit_4.setText(str(block))

    def set_needed_value(self):
        global value_duan
        global value_ce
        global min_duan
        global min_ce
        global block
        value_duan = self.textEdit.toPlainText()
        min_duan = self.textEdit_2.toPlainText()
        value_ce = self.textEdit_3.toPlainText()
        min_ce = self.textEdit_5.toPlainText()
        block = self.textEdit_4.toPlainText()
        with open('./paraments/paraments.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        data['value_duan'] = str(value_duan)
        data['min_duan'] = str(min_duan)
        data['value_ce'] = str(value_ce)
        data['min_ce'] = str(min_ce)
        data['block'] = str(block)
        with open('./paraments/paraments.json', "w") as jsonFile:
            json.dump(data, jsonFile, ensure_ascii=False)
        return value_duan, value_ce, min_ce, min_duan, block

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "阈值设置"))
        self.label.setText(_translate("Dialog", "端面阈值："))
        self.label_2.setText(_translate("Dialog", "端面移除最小值："))
        self.label_3.setText(_translate("Dialog", "侧面阈值："))
        self.label_4.setText(_translate("Dialog", "侧面移除最小值："))
        self.pushButton.setText(_translate("Dialog", "设置参数"))
        self.pushButton_2.setText(_translate("Dialog", "关闭"))
        self.pushButton_3.setText(_translate("Dialog", "获取参数"))


class MyMainWindow_dialog1(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainWindow_dialog1, self).__init__(parent)
        self.setupUi2(self)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./gui/Icon.png'))
    myWin = MyMainWindow_dialog1()
    myWin.show()
    sys.exit(app.exec())
