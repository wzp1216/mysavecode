# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import cv2
import json
import time
import numpy as np
import multiprocessing
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from functions import large_cylinder_top, concentric_cylinder_top, lid_cylinder_top, cylinder_side


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        Dialog.resize(389, 241)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(150, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 60, 221, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 190, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 190, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 100, 221, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 140, 221, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.open_pic)
        self.pushButton_2.clicked.connect(Dialog.start_tool)
        self.pushButton_3.clicked.connect(Dialog.write_para)
        # self.pushButton_4.clicked.connect(Dialog.send_duan)
        # self.pushButton_5.clicked.connect(Dialog.send_ce)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def write_para(self):
        global threshold
        if threshold == 'global':
            with open('./paraments/tool_values.json', 'r', encoding='utf8')as fp:
                json_data = json.load(fp)
            h_min = json_data['h_min']
            h_max = json_data['h_max']
            s_min = json_data['s_min']
            s_max = json_data['s_max']
            v_min = json_data['v_min']
            v_max = json_data['v_max']
            blur = json_data['blur']
            logyex = json_data['logyex']
            area = json_data['area']
            time_save = time.time()
            timeArray_save = time.localtime(time_save)
            otherStyleTime_save = time.strftime("%Y%m%d_%H%M%S", timeArray_save)
            result_file = os.getcwd() + '/' + 'values_' + otherStyleTime_save + '.txt'
            file = open(result_file, 'a')
            file.write('h_min：' + h_min)
            file.write('\n')
            file.write('h_max：' + h_max)
            file.write('\n')
            file.write('s_min：' + s_min)
            file.write('\n')
            file.write('s_max：' + s_max)
            file.write('\n')
            file.write('v_min：' + v_min)
            file.write('\n')
            file.write('v_max：' + v_max)
            file.write('\n')
            file.write('blur：' + blur)
            file.write('\n')
            file.write('logyex：' + logyex)
            file.write('\n')
            file.write('area：' + area)
            file.close()
        else:
            with open('./paraments/tool_values.json', 'r', encoding='utf8')as fp:
                json_data = json.load(fp)
            blocksize = json_data['blocksize']
            c = json_data['c']
            time_save = time.time()
            timeArray_save = time.localtime(time_save)
            otherStyleTime_save = time.strftime("%Y%m%d_%H%M%S", timeArray_save)
            result_file = os.getcwd() + '/' + 'values_' + otherStyleTime_save + '.txt'
            file = open(result_file, 'a')
            file.write('blocksize：' + blocksize)
            file.write('\n')
            file.write('c：' + c)
            file.close()

    def start_tool(self):
        global pic_name
        global threshold
        state_size = self.comboBox.currentText()
        if state_size == 'please_set_size' or '':
            size = str(1)
        else:
            size = str(state_size)
        state_pretreatment = self.comboBox_2.currentText()
        if state_pretreatment == "please_choose_method" or '':
            pretreatment = 'None'
        else:
            pretreatment = str(state_pretreatment)
        state_threshold = self.comboBox_3.currentText()
        if state_threshold == "please_choose_method" or '':
            threshold = 'global'
        else:
            threshold = str(state_threshold)
        try:
            with open('./paraments/tool_paraments.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            data['size'] = str(size)
            data['pretreatment'] = str(pretreatment)
            data['threshold'] = str(threshold)
            with open('./paraments/tool_paraments.json', 'w') as json_file:
                json.dump(data, json_file, ensure_ascii=False)
            if pretreatment == 'None':
                img = cv2.imread(pic_name[0])


                cv2.imwrite('./paraments/result.jpg', img)
            if pretreatment == 'Black_hat':
                img = cv2.imread(pic_name[0])
                dst_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                k = np.ones((9, 9), np.uint8)
                img_black = cv2.morphologyEx(dst_gray, cv2.MORPH_BLACKHAT, k)
                cv2.imwrite('./paraments/result.jpg', img_black)
            if pretreatment == 'Fourier_transform':
                img = cv2.imread(pic_name[0])
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                f = np.fft.fft2(img)
                fshift = np.fft.fftshift(f)
                rows, cols = img.shape
                crow, ccol = int(rows / 2), int(cols / 2)
                fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0  # 设置高通滤波器
                ishift = np.fft.ifftshift(fshift)
                iimg = np.fft.ifft2(ishift)
                iimg = np.abs(iimg)
                iimg = np.array(iimg, dtype='uint8')
                iimg1 = cv2.cvtColor(iimg, cv2.COLOR_GRAY2RGB)
                img_fly = iimg1
                cv2.imwrite('./paraments/result.jpg', iimg1)
            if pretreatment == 'Light_compensation':
                blockSize = 16
                img = cv2.imread(pic_name[0])
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                average = np.mean(gray)
                rows_new = int(np.ceil(gray.shape[0] / blockSize))
                cols_new = int(np.ceil(gray.shape[1] / blockSize))
                blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
                for r in range(rows_new):
                    for c in range(cols_new):
                        rowmin = r * blockSize
                        rowmax = (r + 1) * blockSize
                        if (rowmax > gray.shape[0]):
                            rowmax = gray.shape[0]
                        colmin = c * blockSize
                        colmax = (c + 1) * blockSize
                        if (colmax > gray.shape[1]):
                            colmax = gray.shape[1]
                        imageROI = gray[rowmin:rowmax, colmin:colmax]
                        temaver = np.mean(imageROI)
                        blockImage[r, c] = temaver
                blockImage = blockImage - average
                blockImage2 = cv2.resize(blockImage, (gray.shape[1], gray.shape[0]), interpolation=cv2.INTER_CUBIC)
                gray2 = gray.astype(np.float32)
                dst = gray2 - blockImage2
                dst = dst.astype(np.uint8)
                dst = cv2.GaussianBlur(dst, (3, 3), 0)
                dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
                img_fly = dst
                cv2.imwrite('./paraments/result.jpg', dst)
            self.th = Start_Do()
            self.th.start()
        except json.decoder.JSONDecodeError:
            QMessageBox.critical(self, '错误', '请打开图片', QMessageBox.Yes)


    def open_pic(self):
        global pic_name
        pic_name = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "All Files(*);;JPG Files(*.jpg);;"
                                                                          "BMP Files(*.bmp);;PNG Files(*.png)")
        filename = pic_name[0]
        self.textBrowser.setText(filename)
        dicts = {'filename': str(filename),
                 'size': ''}
        json_str = json.dumps(dicts)
        with open('./paraments/tool_paraments.json', 'w') as json_file:
            json_file.write(json_str)
        return pic_name

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "选 择 图 片 路径："))
        self.pushButton.setText(_translate("Dialog", "打开"))
        self.label_4.setText(_translate("Dialog", "设置图片缩小倍数："))
        self.comboBox.setItemText(0, _translate("Dialog", "please_set_size"))
        self.comboBox.setItemText(1, _translate("Dialog", "1"))
        self.comboBox.setItemText(2, _translate("Dialog", "2"))
        self.comboBox.setItemText(3, _translate("Dialog", "3"))
        self.comboBox.setItemText(4, _translate("Dialog", "4"))
        self.comboBox.setItemText(5, _translate("Dialog", "0.5"))
        self.comboBox.setItemText(6, _translate("Dialog", "0.2"))
        self.label_2.setText(_translate("Dialog", "预处理方法："))
        self.label_3.setText(_translate("Dialog", "阈值分割方法："))
        self.pushButton_2.setText(_translate("Dialog", "开始调试"))
        self.pushButton_3.setText(_translate("Dialog", "记录参数"))
        self.pushButton_4.setText(_translate("Dialog", "传递端面参数"))
        self.pushButton_5.setText(_translate("Dialog", "传递侧面参数"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "please_choose_method"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "None"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Black_hat"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Fourier_transform"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Light_compensation"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "please_choose_method"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "global"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "adaptive"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "local"))

class Start_Do(QThread):

    def __init__(self, parent=None):
        super(Start_Do, self).__init__(parent)

    def run(self):
        os.system('python for_test.py')


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