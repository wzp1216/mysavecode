# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '单独设置端面检测方法和阈值对话框1108.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        Dialog.resize(531, 198)
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(130, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_33 = QtWidgets.QLabel(Dialog)
        self.label_33.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(440, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_32 = QtWidgets.QLabel(Dialog)
        self.label_32.setGeometry(QtCore.QRect(330, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_34 = QtWidgets.QLabel(Dialog)
        self.label_34.setGeometry(QtCore.QRect(20, 60, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(Dialog)
        self.label_35.setGeometry(QtCore.QRect(20, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(Dialog)
        self.label_36.setGeometry(QtCore.QRect(300, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 150, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 150, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(440, 101, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMaximum(1000.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(100, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(255)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(200, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_37 = QtWidgets.QLabel(Dialog)
        self.label_37.setGeometry(QtCore.QRect(20, 150, 51, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(100, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setMaximum(64)
        self.spinBox_3.setSingleStep(4)
        self.spinBox_3.setProperty("value", 4)
        self.spinBox_3.setObjectName("spinBox_3")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.yes)
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def yes(self):
        method_duan = self.comboBox_5.currentText()
        yzfg_duan = self.comboBox_4.currentText()
        value_duan = self.spinBox.value()
        c_duan = self.spinBox_2.value()
        block = self.spinBox_3.value()
        min_duan = self.doubleSpinBox.value()
        if yzfg_duan == 'Local' or yzfg_duan == 'Adaptive':
            print(int(value_duan))
            if int(value_duan) % 2 == 0:
                QMessageBox.warning(self, '错误', '此阈值分割方法下阈值应为奇数', QMessageBox.Yes)
        with open('./paraments/paraments.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        data['value_duan'] = str(value_duan)
        data['min_duan'] = str(min_duan)
        data['c_duan'] = str(c_duan)
        data['method_duan'] = str(method_duan)
        data['yzfg_duan'] = str(yzfg_duan)
        data['block'] = str(block)
        with open('./paraments/paraments.json', "w") as jsonFile:
            json.dump(data, jsonFile, ensure_ascii=False)
        jsonFile.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "端面检测方法和阈值设置"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "none"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "Black_hat"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "Fourier_transform"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "Light_compensation"))
        self.label_33.setText(_translate("Dialog", "端面检测方法："))
        self.comboBox_4.setItemText(0, _translate("Dialog", "none"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Global"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "Local"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "Adaptive"))
        self.label_32.setText(_translate("Dialog", "阈值分割方法："))
        self.label_34.setText(_translate("Dialog", "端面阈值分割参数设置："))
        self.label_35.setText(_translate("Dialog", "端面阈值："))
        self.label_36.setText(_translate("Dialog", "端面最小缺陷阈值："))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "关闭"))
        self.label_37.setText(_translate("Dialog", "block:"))


class MyMainWindow_dialog1(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainWindow_dialog1, self).__init__(parent)
        self.setupUi(self)

        with open('./paraments/paraments.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        if 'value_duan' not in data or 'c_duan' not in data or 'min_duan' not in data or 'method_duan' not in data or 'yzfg_duan' not in data or 'block' not in data:
            QMessageBox.warning(self, '警告', '参数文件缺少某些键，请先设置参数', QMessageBox.Yes)
        value_duan = data['value_duan']
        c_duan = data['c_duan']
        min_duan = data['min_duan']
        block = data['block']
        method_duan = data['method_duan']
        yzfg_duan = data['yzfg_duan']
        json_file.close()
        self.comboBox_5.setCurrentText(method_duan)
        self.comboBox_4.setCurrentText(yzfg_duan)
        self.spinBox.setValue(int(value_duan))
        self.spinBox_2.setValue(float(c_duan))
        self.spinBox_3.setValue(int(block))
        self.doubleSpinBox.setValue(float(min_duan))


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./gui/Icon.png'))
    myWin = MyMainWindow_dialog1()
    myWin.show()
    sys.exit(app.exec())
