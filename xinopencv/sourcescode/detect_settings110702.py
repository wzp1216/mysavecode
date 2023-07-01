# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '检测设置界面1105.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import json
import multiprocessing
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

global sample
sample = 0
global method_duan
method_duan = 'none'
global method_ce
method_ce = 'none'
global yzfg_duan
yzfg_duan = 'none'
global yzfg_ce
yzfg_ce = 'none'
global block
block = 16
global value_duan
value_duan = 0
global value_ce
value_ce = 0
global c_duan
c_duan = 0
global c_ce
c_ce = 0
global min_duan
min_duan = 0
global min_ce
min_ce = 0
global pic_directory
pic_directory = os.getcwd()
global temp_directory
temp_directory = os.getcwd()
global detect_model
detect_model = 'offline'
global delay_time
delay_time = 0.5

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 579)
        Dialog.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 481, 571))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("gui/bkp_175cfe82296ef49fd58695382401c75.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 121, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("gui/bkp_86fcfabc1f49031c8b7ffb853abd0a0.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 238, 121, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("gui/bkp_33e98335da3d11354cdd6ca2e513f9a.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(160, 240, 121, 161))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("gui/bkp_d341f1a823956d877c68ae9fd9aa1bc.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(40, 15, 51, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(200, 12, 54, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(40, 210, 54, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(190, 212, 54, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(280, 50, 291, 41))
        self.label_9.setObjectName("label_9")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(290, 80, 291, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(280, 180, 291, 41))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(290, 210, 171, 31))
        self.label_19.setObjectName("label_19")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(290, 110, 181, 31))
        self.label_10.setObjectName("label_10")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(290, 141, 54, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(290, 240, 171, 31))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(290, 270, 171, 31))
        self.label_22.setObjectName("label_22")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_7.setGeometry(QtCore.QRect(190, 10, 271, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(10, 140, 161, 31))
        self.label_13.setObjectName("label_13")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(260, 180, 141, 31))
        self.label_16.setObjectName("label_16")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(10, 280, 151, 31))
        self.label_25.setObjectName("label_25")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(90, 180, 61, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(10, 360, 71, 41))
        self.label_28.setObjectName("label_28")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(120, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(400, 180, 62, 31))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 500, 81, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 500, 81, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.label_11.setObjectName("label_11")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(10, 230, 81, 31))
        self.label_23.setObjectName("label_23")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_4.setGeometry(QtCore.QRect(170, 230, 61, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(270, 100, 101, 31))
        self.label_12.setObjectName("label_12")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(400, 460, 61, 31))
        self.radioButton.setObjectName("radioButton")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(170, 280, 61, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 320, 201, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(400, 230, 62, 31))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(10, 460, 141, 31))
        self.label_30.setObjectName("label_30")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(260, 230, 141, 31))
        self.label_24.setObjectName("label_24")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(80, 360, 331, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(10, 410, 71, 41))
        self.label_29.setObjectName("label_29")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(260, 270, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setGeometry(QtCore.QRect(260, 460, 81, 31))
        self.label_31.setObjectName("label_31")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 230, 61, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(10, 180, 81, 31))
        self.label_15.setObjectName("label_15")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(380, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 221, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 360, 51, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.label_14.setObjectName("label_14")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(340, 460, 61, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(260, 290, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 410, 51, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(150, 460, 62, 31))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(170, 180, 61, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 410, 331, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setGeometry(QtCore.QRect(270, 60, 101, 31))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.label_33.setObjectName("label_33")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_4.setGeometry(QtCore.QRect(380, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_5.setGeometry(QtCore.QRect(120, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(Dialog.set_para)
        self.pushButton_2.clicked.connect(Dialog.get_para)
        self.pushButton_5.clicked.connect(Dialog.yes)
        self.pushButton_6.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_3.clicked.connect(Dialog.get_pic_path)
        self.pushButton_4.clicked.connect(Dialog.get_temp_path)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def yes(self):
        global pic_directory
        global temp_directory
        global value_duan
        global value_ce
        global min_duan
        global min_ce
        global c_ce
        global c_duan
        global block
        global method_duan
        global method_ce
        global yzfg_duan
        global yzfg_ce
        global detect_model
        global delay_time
        global sample
        if self.radioButton.isChecked():
            detect_model = 'off_line'
        if self.radioButton_2.isChecked():
            detect_model = 'on_line'
        delay_time = self.doubleSpinBox_3.value()
        if sample == 'none' or sample == '':
            QMessageBox.critical(self, '错误', '请选择样品型号', QMessageBox.Yes)
        # if method_duan == 'none' or method_duan == '':
        #     QMessageBox.critical(self, '错误', '请选择端面检测方法', QMessageBox.Yes)
        # if method_ce == 'none' or method_ce == '':
        #     QMessageBox.critical(self, '错误', '请选择侧面检测方法', QMessageBox.Yes)
        if yzfg_duan == 'none' or yzfg_duan == '':
            QMessageBox.critical(self, '错误', '请选择端面阈值分割方法', QMessageBox.Yes)
        if yzfg_ce == 'none' or yzfg_ce == '':
            QMessageBox.critical(self, '错误', '请选择侧面阈值分割方法', QMessageBox.Yes)
        if yzfg_duan == 'Local' or yzfg_duan == 'Adaptive':
            if c_duan == '' or c_duan == 'none':
                QMessageBox.critical(self, '错误', '此阈值分割方法应设置两个参数', QMessageBox.Yes)
        if yzfg_ce == 'Local' or yzfg_ce == 'Adaptive':
            if c_ce == '' or c_ce == 'none':
                QMessageBox.critical(self, '错误', '此阈值分割方法应设置两个参数', QMessageBox.Yes)
        if float(delay_time) == 0:
            QMessageBox.critical(self, '错误', '建议设置循环延时时间为0.4-0.6', QMessageBox.Yes)
        dicts = {'directory': str(pic_directory),
                 'template': str(temp_directory),
                 'value_duan': str(value_duan),
                 'value_ce': str(value_ce),
                 'c_duan': str(c_duan),
                 'c_ce': str(c_ce),
                 'min_duan': str(min_duan),
                 'min_ce': str(min_ce),
                 'block': str(block),
                 'yzfg_duan': str(yzfg_duan),
                 'yzfg_ce': str(yzfg_ce),
                 'sample': str(sample),
                 'method_duan': str(method_duan),
                 'method_ce': str(method_ce),
                 'delay_time': str(delay_time),
                 'detect_model': str(detect_model)}
        json_str = json.dumps(dicts)
        with open('./paraments/paraments.json', 'w') as json_file:
            json_file.write(json_str)
        json_file.close()
        return pic_directory, temp_directory, value_ce, value_duan, min_ce, c_ce, c_duan, min_duan, sample, method_duan, method_ce, detect_model, delay_time, block, yzfg_duan, yzfg_ce

    def set_para(self):
        global value_duan
        global value_ce
        global min_duan
        global min_ce
        global c_ce
        global c_duan
        global block
        global method_duan
        global method_ce
        global yzfg_duan
        global yzfg_ce
        global sample
        value_duan = self.textEdit.toPlainText()
        value_ce = self.textEdit_3.toPlainText()
        c_duan = self.textEdit_2.toPlainText()
        c_ce = self.textEdit_4.toPlainText()
        min_duan = self.doubleSpinBox.value()
        min_ce = self.doubleSpinBox_2.value()
        block_state = self.comboBox_3.currentText()
        if str(block_state) == 'none' or '' or str(16):
            block = str(16)
        else:
            block = str(block_state)
        method_duan_state = self.comboBox_5.currentText()
        if method_duan_state == 'none' or '':
            method_duan = 'none'
        if method_duan_state == 'Fourier_transform':
            method_duan = 'Fourier_transform'
        if method_duan_state == 'Light_compensation':
            method_duan = 'Light_compensation'
        if method_duan_state == 'Black_hat':
            method_duan = 'Black_hat'
        yzfg_duan_state = self.comboBox_4.currentText()
        if yzfg_duan_state == 'none' or '' or 'Global':
            yzfg_duan = 'Global'
        if yzfg_duan_state == 'Local':
            yzfg_duan = 'Local'
        if yzfg_duan_state == 'Adaptive':
            yzfg_duan = 'Adaptive'
        print(yzfg_duan)
        print(111111)
        method_ce_state = self.comboBox.currentText()
        if method_ce_state == 'none' or '':
            method_ce = 'none'
        if method_ce_state == 'Fourier_transform':
            method_ce = 'Fourier_transform'
        if method_ce_state == 'Light_compensation':
            method_ce = 'Light_compensation'
        if method_ce_state == 'Black_hat':
            method_ce = 'Black_hat'
        yzfg_ce_state = self.comboBox_2.currentText()
        if yzfg_ce_state == 'none' or '' or 'Global':
            yzfg_ce = 'Global'
        if yzfg_ce_state == 'Local':
            yzfg_ce = 'Local'
        if yzfg_ce_state == 'Adaptive':
            yzfg_ce = 'Adaptive'
        print(yzfg_ce)
        print(222222)
        sample_state = self.comboBox_7.currentText()
        if sample_state == 'none' or '':
            sample = 'none'
        if sample_state == 'sample1':
            sample = '1'
        if sample_state == 'sample2':
            sample = '2'
        if sample_state == 'sample3':
            sample = '3'
        if sample_state == 'sample4':
            sample = '4'
        print(333333)
        if sample == 'none':
            QMessageBox.critical(self, '错误', '请选择样品型号', QMessageBox.Yes)
        print(444444)
        if yzfg_duan == 'Local' or yzfg_duan =='Adaptive':
            if c_duan == '' or c_duan == 'none':
                c_duan = 3
                QMessageBox.critical(self, '错误', '端面阈值分割方法需要设置两个参数', QMessageBox.Yes)
            print(555555)
            if int(value_duan) % 2 == 0:
                QMessageBox.critical(self, '错误', '此阈值分割方法阈值必须是奇数', QMessageBox.Yes)
            print(666666)
        print(999999)
        if yzfg_ce == 'Local' or yzfg_ce =='Adaptive':
            if c_ce == '' or c_ce == 'none':
                c_ce = 3
                QMessageBox.critical(self, '错误', '侧面阈值分割方法需要设置两个参数', QMessageBox.Yes)
            if int(value_duan) % 2 == 0:
                QMessageBox.critical(self, '错误', '此阈值分割方法阈值必须是奇数', QMessageBox.Yes)
        if yzfg_ce == 'Global':
            c_ce = '0'
        if yzfg_duan == 'Global':
            c_duan = '0'
        print(value_duan, value_ce, c_ce, c_duan, min_ce, min_duan, method_duan, method_ce, yzfg_ce, yzfg_duan, sample, block)
        return value_duan, value_ce, c_ce, c_duan, min_ce, min_duan, method_duan, method_ce, yzfg_ce, yzfg_duan, sample, block

    def get_para(self):
        global value_duan
        global value_ce
        global min_duan
        global min_ce
        global c_ce
        global c_duan
        self.textEdit.setText(str(value_duan))
        self.textEdit_2.setText(str(c_duan))
        self.textEdit_3.setText(str(value_ce))
        self.textEdit_4.setText(str(c_ce))
        self.doubleSpinBox.valueFromText(str(min_duan))
        self.doubleSpinBox_2.valueFromText(str(min_ce))

    def get_pic_path(self):
        global pic_directory
        pic_directory = QtWidgets.QFileDialog.getExistingDirectory(None, '选取图片所在的文件夹', os.getcwd())
        self.textBrowser.setText(pic_directory)
        return pic_directory

    def get_temp_path(self):
        global temp_directory
        temp_directory = QtWidgets.QFileDialog.getExistingDirectory(None, '选取模板所在的文件夹', os.getcwd())
        self.textBrowser_2.setText(temp_directory)
        return temp_directory

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "检测参数设置"))
        self.label_5.setText(_translate("Dialog", "样品一"))
        self.label_6.setText(_translate("Dialog", "样品二"))
        self.label_7.setText(_translate("Dialog", "样品三"))
        self.label_8.setText(_translate("Dialog", "样品四"))
        self.label_9.setText(_translate("Dialog", "1.本界面的四种样品检测方"))
        self.label_17.setText(_translate("Dialog", "法不完全相同，检测精度"))
        self.label_18.setText(_translate("Dialog", "2.每次设置阈值之前需要现"))
        self.label_19.setText(_translate("Dialog", "场进行打光设备的调试，"))
        self.label_10.setText(_translate("Dialog", "与缺陷大小以及设备调试"))
        self.label_20.setText(_translate("Dialog", "有关"))
        self.label_21.setText(_translate("Dialog", "根据调试的照片来确定"))
        self.label_22.setText(_translate("Dialog", "阈值"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "说明"))
        self.comboBox_7.setItemText(0, _translate("Dialog", "none"))
        self.comboBox_7.setItemText(1, _translate("Dialog", "sample1"))
        self.comboBox_7.setItemText(2, _translate("Dialog", "sample2"))
        self.comboBox_7.setItemText(3, _translate("Dialog", "sample3"))
        self.comboBox_7.setItemText(4, _translate("Dialog", "sample4"))
        self.label_13.setText(_translate("Dialog", "请设置阈值分割参数："))
        self.label_16.setText(_translate("Dialog", "端面最小缺陷阈值："))
        self.label_25.setText(_translate("Dialog", "光照补偿block设置："))
        self.label_28.setText(_translate("Dialog", "图片路径："))
        self.comboBox.setItemText(0, _translate("Dialog", "none"))
        self.comboBox.setItemText(1, _translate("Dialog", "Black_hat"))
        self.comboBox.setItemText(2, _translate("Dialog", "Fourier_transform"))
        self.comboBox.setItemText(3, _translate("Dialog", "Light_compensation"))
        self.pushButton_5.setText(_translate("Dialog", "确定"))
        self.pushButton_6.setText(_translate("Dialog", "关闭"))
        self.label_11.setText(_translate("Dialog", "侧面检测方法："))
        self.label_23.setText(_translate("Dialog", "侧面阈值："))
        self.label_12.setText(_translate("Dialog", "阈值分割方法："))
        self.radioButton.setText(_translate("Dialog", "离线"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "16"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "8"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "32"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "64"))
        self.pushButton_2.setText(_translate("Dialog", "获取参数"))
        self.label_30.setText(_translate("Dialog", "设置循环延时时间："))
        self.label_24.setText(_translate("Dialog", "侧面最小缺陷阈值："))
        self.label_29.setText(_translate("Dialog", "模板路径："))
        self.label_26.setText(_translate("Dialog", "只有当选择了光照补偿算法时"))
        self.label_31.setText(_translate("Dialog", "检测模式："))
        self.label_15.setText(_translate("Dialog", "端面阈值："))
        self.comboBox_2.setItemText(0, _translate("Dialog", "none"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Global"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Local"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Adaptive"))
        self.pushButton.setText(_translate("Dialog", "设置参数"))
        self.pushButton_3.setText(_translate("Dialog", "浏览"))
        self.label_14.setText(_translate("Dialog", "请选择检测样品的型号："))
        self.radioButton_2.setText(_translate("Dialog", "在线"))
        self.label_27.setText(_translate("Dialog", "才需要设置blocksize，默认为16"))
        self.pushButton_4.setText(_translate("Dialog", "浏览"))
        self.label_32.setText(_translate("Dialog", "阈值分割方法："))
        self.label_33.setText(_translate("Dialog", "端面检测方法："))
        self.comboBox_4.setItemText(0, _translate("Dialog", "none"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Global"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "Local"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "Adaptive"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "none"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "Black_hat"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "Fourier_transform"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "Light_compensation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "参数设置"))


class MyMainWindow_dialog(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainWindow_dialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./gui/Icon.png'))
    myWin = MyMainWindow_dialog()
    myWin.show()
    sys.exit(app.exec())