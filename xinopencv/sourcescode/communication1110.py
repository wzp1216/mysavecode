# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip通信对话框.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import json
import multiprocessing
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

global ip
ip = '192.168.0.11'
global port
port = 502
global value
value = 0
global read_model
read_model = 0
global write_model
write_model = 0

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        Dialog.resize(538, 282)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(80, 20, 271, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(370, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(430, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 511, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setGeometry(QtCore.QRect(420, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(280, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(90, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 511, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 30, 411, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 240, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.ip_config)
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def ip_config(self):
        global ip
        global port
        global value
        global read_model
        global write_model
        read_text = self.comboBox_2.currentText()
        if read_text == 'on':
            read_model = 1
        else:
            read_model = 0
        write_text = self.comboBox.currentText()
        if write_text == 'off':
            write_model = 0
        elif write_text == 'single model':
            write_model = 1
        elif write_text == 'multiple model':
            write_model = 2
        ip = self.textEdit.toPlainText()
        port = self.textEdit_2.toPlainText()
        value = self.textEdit_3.toPlainText()
        if ip == '':
            QMessageBox.critical(self, '错误', 'ip地址不可为空，请输入正确的PLC地址', QMessageBox.Yes)
        if port == '':
            QMessageBox.critical(self, '错误', '端口号不可为空，请输入正确的端口号（默认为502）', QMessageBox.Yes)
        if value == '':
            QMessageBox.critical(self, '错误', '请输入要写进保持寄存器的值，不可为空（0或1）', QMessageBox.Yes)
        ip_paraments = {
            'ip': str(ip),
            'port': str(port),
            'value': str(value),
            'read_model': str(read_model),
            'write_model': str(write_model)
        }
        json_str = json.dumps(ip_paraments)
        with open('./paraments/communication.json', 'w') as json_file:
            json_file.write(json_str)
        return ip, port, value, read_model, write_model

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "IP设置界面"))
        self.label.setText(_translate("Dialog", "ip地址："))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'宋体\'; font-size:18pt;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "端口号："))
        self.groupBox.setTitle(_translate("Dialog", "写入寄存器（保持）"))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'宋体\'; font-size:18pt;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "写入寄存器内的值："))
        self.comboBox.setItemText(0, _translate("Dialog", "off"))
        self.comboBox.setItemText(1, _translate("Dialog", "single model"))
        self.comboBox.setItemText(2, _translate("Dialog", "multiple"))
        self.label_4.setText(_translate("Dialog", "模式选择："))
        self.groupBox_2.setTitle(_translate("Dialog", "读寄存器"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "on"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "off"))
        self.label_5.setText(_translate("Dialog", "模式选择："))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "关闭"))


class MyMainWindow_dialog2(QMainWindow, Ui_Dialog2):
    def __init__(self, parent=None):
        super(MyMainWindow_dialog2, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./gui/Icon.png'))
    myWin = MyMainWindow_dialog2()
    myWin.show()
    sys.exit(app.exec())

