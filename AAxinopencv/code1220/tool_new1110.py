# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools1110.ui'
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
        # Dialog.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        Dialog.resize(389, 304)
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
        self.label_4.setGeometry(QtCore.QRect(20, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 140, 221, 31))
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
        self.label_2.setGeometry(QtCore.QRect(20, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 260, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 260, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 180, 221, 31))
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
        self.comboBox_3.setGeometry(QtCore.QRect(150, 220, 221, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(150, 100, 221, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(150, 60, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.open_pic)
        self.pushButton_6.clicked.connect(Dialog.open_temp)
        self.pushButton_2.clicked.connect(Dialog.start_tool_duan)
        self.pushButton_3.clicked.connect(Dialog.start_tool_ce)
        # self.pushButton_4.clicked.connect(Dialog.send_duan)
        # self.pushButton_5.clicked.connect(Dialog.send_ce)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def start_tool_ce(self):
        global pic_name
        global threshold
        global temp_name
        state_size = self.comboBox.currentText()
        if state_size == 'please_set_size' or '':
            size = str(1)
        else:
            size = str(state_size)
        state_pretreatment = self.comboBox_2.currentText()
        if state_pretreatment == "please_choose_method" or '':
            pretreatment = 'none'
        else:
            pretreatment = str(state_pretreatment)
        state_threshold = self.comboBox_3.currentText()
        if state_threshold == "please_choose_method" or '':
            threshold = 'global'
        else:
            threshold = str(state_threshold)
        state_sample = self.comboBox_4.currentText()
        sample = str(state_sample)
        logo = os.getcwd() + '/paraments/' + 'label' + '.txt'
        file = open(logo, 'w')
        file.write(str(1))
        file.close()
        try:
            with open('./paraments/tool_paraments.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            data['size'] = str(size)
            data['pretreatment'] = str(pretreatment)
            data['threshold'] = str(threshold)
            data['sample'] = str(sample)
            with open('./paraments/tool_paraments.json', 'w') as json_file:
                json.dump(data, json_file, ensure_ascii=False)
            json_file.close()
            print('#####################################################')
            if sample == 'sample1' or sample == 'sample2' or sample == 'sample3' or sample == 'sample4':
                if pretreatment == 'none' or pretreatment == '':
                    img = cv2.imread(pic_name[0])
                    temp = cv2.imread(temp_name[0])
                    img_roi, img_temp, min_loc, temp_w, temp_h = cylinder_side.get_roi(img, temp)
                    cv2.imwrite('./paraments/result.jpg', img_roi)
                    cv2.imwrite('./paraments/original.jpg', img)
                    print(19961996)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Black_hat':
                    img = cv2.imread(pic_name[0])
                    temp = cv2.imread(temp_name[0])
                    img_roi, img_temp, min_loc, temp_w, temp_h = cylinder_side.get_roi(img, temp)
                    dst_gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
                    k = np.ones((9, 9), np.uint8)
                    img_black = cv2.morphologyEx(dst_gray, cv2.MORPH_BLACKHAT, k)
                    cv2.imwrite('./paraments/result.jpg', img_black)
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Fourier_transform':
                    img0 = cv2.imread(pic_name[0])
                    temp = cv2.imread(temp_name[0])
                    img_roi, img_temp, min_loc, temp_w, temp_h = cylinder_side.get_roi(img0, temp)
                    img_roi = cv2.cvtColor(img_roi, cv2.COLOR_RGB2GRAY)
                    img = img_roi
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
                    cv2.imwrite('./paraments/result.jpg', iimg1)
                    cv2.imwrite('./paraments/original.jpg', img0)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Light_compensation':
                    blockSize = 16
                    img = cv2.imread(pic_name[0])
                    temp = cv2.imread(temp_name[0])
                    img_roi, img_temp, min_loc, temp_w, temp_h = cylinder_side.get_roi(img, temp)
                    gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
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
                    cv2.imwrite('./paraments/result.jpg', dst)
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
        except json.decoder.JSONDecodeError:
            QMessageBox.critical(self, '错误', '请打开图片', QMessageBox.Yes)


    def start_tool_duan(self):
        global pic_name
        global threshold
        state_size = self.comboBox.currentText()
        if state_size == 'please_set_size' or '':
            size = str(1)
        else:
            size = str(state_size)
        state_pretreatment = self.comboBox_2.currentText()
        if state_pretreatment == "please_choose_method" or '':
            pretreatment = 'none'
        else:
            pretreatment = str(state_pretreatment)
        state_threshold = self.comboBox_3.currentText()
        if state_threshold == "please_choose_method" or '':
            threshold = 'global'
        else:
            threshold = str(state_threshold)
        state_sample = self.comboBox_4.currentText()
        sample = str(state_sample)
        logo = os.getcwd() + '/paraments/' + 'label' + '.txt'
        file = open(logo, 'w')
        file.write(str(0))
        file.close()
        try:
            with open('./paraments/tool_paraments.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            data['size'] = str(size)
            data['pretreatment'] = str(pretreatment)
            data['threshold'] = str(threshold)
            data['sample'] = str(sample)
            with open('./paraments/tool_paraments.json', 'w') as json_file:
                json.dump(data, json_file, ensure_ascii=False)
            json_file.close()
            if sample == 'sample1' or sample == 'sample2':
                if pretreatment == 'none':
                    img = cv2.imread(pic_name[0])
                    img_roi = large_cylinder_top.get_roi_large_cylinder(img)
                    cv2.imwrite('./paraments/result.jpg', img_roi)
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Black_hat':
                    img = cv2.imread(pic_name[0])
                    img_roi = large_cylinder_top.get_roi_large_cylinder(img)
                    dst_gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
                    k = np.ones((9, 9), np.uint8)
                    img_black = cv2.morphologyEx(dst_gray, cv2.MORPH_BLACKHAT, k)
                    cv2.imwrite('./paraments/result.jpg', img_black)
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Fourier_transform':
                    img0 = cv2.imread(pic_name[0])
                    img_roi = large_cylinder_top.get_roi_large_cylinder(img0)
                    img = img_roi
                    f = np.fft.fft2(img)
                    fshift = np.fft.fftshift(f)
                    rows, cols = img.shape[0:2]
                    crow, ccol = int(rows / 2), int(cols / 2)
                    fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0  # 设置高通滤波器
                    ishift = np.fft.ifftshift(fshift)
                    iimg = np.fft.ifft2(ishift)
                    iimg = np.abs(iimg)
                    iimg = np.array(iimg, dtype='uint8')
                    iimg1 = iimg
                    cv2.imwrite('./paraments/result.jpg', iimg1)
                    cv2.imwrite('./paraments/original.jpg', img0)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Light_compensation':
                    blockSize = 16
                    img = cv2.imread(pic_name[0])
                    img_roi = large_cylinder_top.get_roi_large_cylinder(img)
                    gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
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
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
            if sample == 'sample3':
                if pretreatment == 'none':
                    img = cv2.imread(pic_name[0])
                    img_roi1, img_roi2 = concentric_cylinder_top.get_roi_concentric(img)
                    cv2.imwrite('./paraments/result1.jpg', img_roi1)
                    cv2.imwrite('./paraments/result2.jpg', img_roi2)
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Black_hat':
                    img = cv2.imread(pic_name[0])
                    img_roi1, img_roi2 = concentric_cylinder_top.get_roi_concentric(img)
                    dst_gray1 = cv2.cvtColor(img_roi1, cv2.COLOR_BGR2GRAY)
                    dst_gray2 = cv2.cvtColor(img_roi2, cv2.COLOR_BGR2GRAY)
                    k = np.ones((9, 9), np.uint8)
                    img_black1 = cv2.morphologyEx(dst_gray1, cv2.MORPH_BLACKHAT, k)
                    img_black2 = cv2.morphologyEx(dst_gray2, cv2.MORPH_BLACKHAT, k)
                    cv2.imwrite('./paraments/result1.jpg', img_black1)
                    cv2.imwrite('./paraments/result2.jpg', img_black2)
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Fourier_transform':
                    img0 = cv2.imread(pic_name[0])
                    img_roi1, img_roi2 = concentric_cylinder_top.get_roi_concentric(img0)
                    img1 = cv2.cvtColor(img_roi1, cv2.COLOR_BGR2GRAY)
                    f = np.fft.fft2(img1)
                    fshift = np.fft.fftshift(f)
                    rows, cols = img1.shape
                    crow, ccol = int(rows / 2), int(cols / 2)
                    fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0  # 设置高通滤波器
                    ishift = np.fft.ifftshift(fshift)
                    iimg = np.fft.ifft2(ishift)
                    iimg = np.abs(iimg)
                    iimg = np.array(iimg, dtype='uint8')
                    iimg1 = cv2.cvtColor(iimg, cv2.COLOR_GRAY2RGB)
                    img2 = cv2.cvtColor(img_roi2, cv2.COLOR_BGR2GRAY)
                    f = np.fft.fft2(img2)
                    fshift = np.fft.fftshift(f)
                    rows, cols = img2.shape
                    crow, ccol = int(rows / 2), int(cols / 2)
                    fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0  # 设置高通滤波器
                    ishift = np.fft.ifftshift(fshift)
                    iimg = np.fft.ifft2(ishift)
                    iimg = np.abs(iimg)
                    iimg = np.array(iimg, dtype='uint8')
                    iimg2 = cv2.cvtColor(iimg, cv2.COLOR_GRAY2RGB)
                    cv2.imwrite('./paraments/result1.jpg', iimg1)
                    cv2.imwrite('./paraments/result2.jpg', iimg2)
                    cv2.imwrite('./paraments/original.jpg', img0)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Light_compensation':
                    blockSize = 16
                    img = cv2.imread(pic_name[0])
                    img_roi1, img_roi2 = concentric_cylinder_top.get_roi_concentric(img)
                    gray1 = cv2.cvtColor(img_roi1, cv2.COLOR_BGR2GRAY)
                    average = np.mean(gray1)
                    rows_new = int(np.ceil(gray1.shape[0] / blockSize))
                    cols_new = int(np.ceil(gray1.shape[1] / blockSize))
                    blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
                    for r in range(rows_new):
                        for c in range(cols_new):
                            rowmin = r * blockSize
                            rowmax = (r + 1) * blockSize
                            if (rowmax > gray1.shape[0]):
                                rowmax = gray1.shape[0]
                            colmin = c * blockSize
                            colmax = (c + 1) * blockSize
                            if (colmax > gray1.shape[1]):
                                colmax = gray1.shape[1]
                            imageROI = gray1[rowmin:rowmax, colmin:colmax]
                            temaver = np.mean(imageROI)
                            blockImage[r, c] = temaver
                    blockImage = blockImage - average
                    blockImage2 = cv2.resize(blockImage, (gray1.shape[1], gray1.shape[0]),
                                             interpolation=cv2.INTER_CUBIC)
                    gray2 = gray1.astype(np.float32)
                    dst_gzbc = gray2 - blockImage2
                    dst_gzbc = dst_gzbc.astype(np.uint8)
                    dst_gzbc = cv2.GaussianBlur(dst_gzbc, (3, 3), 0)
                    dst_gzbc1 = cv2.cvtColor(dst_gzbc, cv2.COLOR_GRAY2BGR)
                    gray2 = cv2.cvtColor(img_roi2, cv2.COLOR_BGR2GRAY)
                    average = np.mean(gray2)
                    rows_new = int(np.ceil(gray2.shape[0] / blockSize))
                    cols_new = int(np.ceil(gray2.shape[1] / blockSize))
                    blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
                    for r in range(rows_new):
                        for c in range(cols_new):
                            rowmin = r * blockSize
                            rowmax = (r + 1) * blockSize
                            if (rowmax > gray2.shape[0]):
                                rowmax = gray2.shape[0]
                            colmin = c * blockSize
                            colmax = (c + 1) * blockSize
                            if (colmax > gray2.shape[1]):
                                colmax = gray2.shape[1]
                            imageROI = gray2[rowmin:rowmax, colmin:colmax]
                            temaver = np.mean(imageROI)
                            blockImage[r, c] = temaver
                    blockImage = blockImage - average
                    blockImage2 = cv2.resize(blockImage, (gray2.shape[1], gray2.shape[0]),
                                             interpolation=cv2.INTER_CUBIC)
                    gray2 = gray2.astype(np.float32)
                    dst_gzbc = gray2 - blockImage2
                    dst_gzbc = dst_gzbc.astype(np.uint8)
                    dst_gzbc = cv2.GaussianBlur(dst_gzbc, (3, 3), 0)
                    dst_gzbc2 = cv2.cvtColor(dst_gzbc, cv2.COLOR_GRAY2BGR)
                    cv2.imwrite('./paraments/result1.jpg', dst_gzbc1)
                    cv2.imwrite('./paraments/result2.jpg', dst_gzbc2)
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
            if sample == 'sample4':
                if pretreatment == 'none':
                    img = cv2.imread(pic_name[0])
                    temp = cv2.imread('./paraments/lid_cylinder_template.jpg')
                    dst = lid_cylinder_top.trans2binary(img)
                    img_roi1, img_roi2 = lid_cylinder_top.get_roi_lid(img, temp, dst)
                    cv2.imwrite('./paraments/result1.jpg', img_roi1)
                    cv2.imwrite('./paraments/result2.jpg', img_roi2)
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Black_hat':
                    img = cv2.imread(pic_name[0])
                    temp = cv2.imread('./paraments/lid_cylinder_template.jpg')
                    dst = lid_cylinder_top.trans2binary(img)
                    img_roi1, img_roi2 = lid_cylinder_top.get_roi_lid(img, temp, dst)
                    dst_gray1 = cv2.cvtColor(img_roi1, cv2.COLOR_BGR2GRAY)
                    dst_gray2 = cv2.cvtColor(img_roi2, cv2.COLOR_BGR2GRAY)
                    k = np.ones((9, 9), np.uint8)
                    img_black1 = cv2.morphologyEx(dst_gray1, cv2.MORPH_BLACKHAT, k)
                    img_black2 = cv2.morphologyEx(dst_gray2, cv2.MORPH_BLACKHAT, k)
                    cv2.imwrite('./paraments/result1.jpg', img_black1)
                    cv2.imwrite('./paraments/result2.jpg', img_black2)
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Fourier_transform':
                    img0 = cv2.imread(pic_name[0])
                    temp = cv2.imread('./paraments/lid_cylinder_template.jpg')
                    dst = lid_cylinder_top.trans2binary(img0)
                    img_roi1, img_roi2 = lid_cylinder_top.get_roi_lid(img0, temp, dst)
                    img1 = cv2.cvtColor(img_roi1, cv2.COLOR_BGR2GRAY)
                    f = np.fft.fft2(img1)
                    fshift = np.fft.fftshift(f)
                    rows, cols = img1.shape
                    crow, ccol = int(rows / 2), int(cols / 2)
                    fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0  # 设置高通滤波器
                    ishift = np.fft.ifftshift(fshift)
                    iimg = np.fft.ifft2(ishift)
                    iimg = np.abs(iimg)
                    iimg = np.array(iimg, dtype='uint8')
                    iimg1 = cv2.cvtColor(iimg, cv2.COLOR_GRAY2RGB)
                    img2 = cv2.cvtColor(img_roi2, cv2.COLOR_BGR2GRAY)
                    f = np.fft.fft2(img2)
                    fshift = np.fft.fftshift(f)
                    rows, cols = img2.shape
                    crow, ccol = int(rows / 2), int(cols / 2)
                    fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0  # 设置高通滤波器
                    ishift = np.fft.ifftshift(fshift)
                    iimg = np.fft.ifft2(ishift)
                    iimg = np.abs(iimg)
                    iimg = np.array(iimg, dtype='uint8')
                    iimg2 = cv2.cvtColor(iimg, cv2.COLOR_GRAY2RGB)
                    cv2.imwrite('./paraments/result1.jpg', iimg1)
                    cv2.imwrite('./paraments/result2.jpg', iimg2)
                    cv2.imwrite('./paraments/original.jpg', img0)
                    self.th = Start_Do()
                    self.th.start()
                if pretreatment == 'Light_compensation':
                    blockSize = 16
                    img = cv2.imread(pic_name[0])
                    temp = cv2.imread('./paraments/lid_cylinder_template.jpg')
                    dst = lid_cylinder_top.trans2binary(img)
                    img_roi1, img_roi2 = lid_cylinder_top.get_roi_lid(img, temp, dst)
                    gray1 = cv2.cvtColor(img_roi1, cv2.COLOR_BGR2GRAY)
                    average = np.mean(gray1)
                    rows_new = int(np.ceil(gray1.shape[0] / blockSize))
                    cols_new = int(np.ceil(gray1.shape[1] / blockSize))
                    blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
                    for r in range(rows_new):
                        for c in range(cols_new):
                            rowmin = r * blockSize
                            rowmax = (r + 1) * blockSize
                            if (rowmax > gray1.shape[0]):
                                rowmax = gray1.shape[0]
                            colmin = c * blockSize
                            colmax = (c + 1) * blockSize
                            if (colmax > gray1.shape[1]):
                                colmax = gray1.shape[1]
                            imageROI = gray1[rowmin:rowmax, colmin:colmax]
                            temaver = np.mean(imageROI)
                            blockImage[r, c] = temaver
                    blockImage = blockImage - average
                    blockImage2 = cv2.resize(blockImage, (gray1.shape[1], gray1.shape[0]),
                                             interpolation=cv2.INTER_CUBIC)
                    gray2 = gray1.astype(np.float32)
                    dst_gzbc = gray2 - blockImage2
                    dst_gzbc = dst_gzbc.astype(np.uint8)
                    dst_gzbc = cv2.GaussianBlur(dst_gzbc, (3, 3), 0)
                    dst_gzbc1 = cv2.cvtColor(dst_gzbc, cv2.COLOR_GRAY2BGR)
                    gray2 = cv2.cvtColor(img_roi2, cv2.COLOR_BGR2GRAY)
                    average = np.mean(gray2)
                    rows_new = int(np.ceil(gray2.shape[0] / blockSize))
                    cols_new = int(np.ceil(gray2.shape[1] / blockSize))
                    blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
                    for r in range(rows_new):
                        for c in range(cols_new):
                            rowmin = r * blockSize
                            rowmax = (r + 1) * blockSize
                            if (rowmax > gray2.shape[0]):
                                rowmax = gray2.shape[0]
                            colmin = c * blockSize
                            colmax = (c + 1) * blockSize
                            if (colmax > gray2.shape[1]):
                                colmax = gray2.shape[1]
                            imageROI = gray2[rowmin:rowmax, colmin:colmax]
                            temaver = np.mean(imageROI)
                            blockImage[r, c] = temaver
                    blockImage = blockImage - average
                    blockImage2 = cv2.resize(blockImage, (gray2.shape[1], gray2.shape[0]),
                                             interpolation=cv2.INTER_CUBIC)
                    gray2 = gray2.astype(np.float32)
                    dst_gzbc = gray2 - blockImage2
                    dst_gzbc = dst_gzbc.astype(np.uint8)
                    dst_gzbc = cv2.GaussianBlur(dst_gzbc, (3, 3), 0)
                    dst_gzbc2 = cv2.cvtColor(dst_gzbc, cv2.COLOR_GRAY2BGR)
                    cv2.imwrite('./paraments/result1.jpg', dst_gzbc1)
                    cv2.imwrite('./paraments/result2.jpg', dst_gzbc2)
                    cv2.imwrite('./paraments/original.jpg', img)
                    self.th = Start_Do()
                    self.th.start()
        except json.decoder.JSONDecodeError:
            QMessageBox.critical(self, '错误', '请打开图片', QMessageBox.Yes)


    def open_pic(self):
        global pic_name
        global tempname
        tempname = 'none'
        pic_name = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "All Files(*);;JPG Files(*.jpg);;"
                                                                          "BMP Files(*.bmp);;PNG Files(*.png)")
        filename = pic_name[0]
        self.textBrowser.setText(filename)
        dicts = {'filename': str(filename),
                 'size': '',
                 'tempname': str(tempname)}
        json_str = json.dumps(dicts)
        with open('./paraments/tool_paraments.json', 'w') as json_file:
            json_file.write(json_str)
        return pic_name

    def open_temp(self):
        global temp_name
        temp_name = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "All Files(*);;JPG Files(*.jpg);;"
                                                                          "BMP Files(*.bmp);;PNG Files(*.png)")
        filename = temp_name[0]
        self.textBrowser_2.setText(filename)
        with open('./paraments/tool_paraments.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        data['tempname'] = str(filename)
        with open('./paraments/paraments.json', "w") as jsonFile:
            json.dump(data, jsonFile, ensure_ascii=False)
        jsonFile.close()
        return temp_name

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "调试工具"))
        self.label.setText(_translate("Dialog", "选 择 图 片 路 径："))
        self.pushButton.setText(_translate("Dialog", "打开"))
        self.pushButton_6.setText(_translate("Dialog", "打开"))
        self.label_4.setText(_translate("Dialog", "图 片 缩 小 倍 数："))
        self.comboBox.setItemText(0, _translate("Dialog", "1"))
        self.comboBox.setItemText(1, _translate("Dialog", "2"))
        self.comboBox.setItemText(2, _translate("Dialog", "3"))
        self.comboBox.setItemText(3, _translate("Dialog", "4"))
        self.comboBox.setItemText(4, _translate("Dialog", "5"))
        self.comboBox.setItemText(5, _translate("Dialog", "6"))
        self.comboBox.setItemText(6, _translate("Dialog", "0.5"))
        self.comboBox.setItemText(7, _translate("Dialog", "0.2"))
        self.label_2.setText(_translate("Dialog", "预  处  理  方  法："))
        self.label_3.setText(_translate("Dialog", "阈 值 分 割 方 法："))
        self.pushButton_2.setText(_translate("Dialog", "调试端面"))
        self.pushButton_3.setText(_translate("Dialog", "调试侧面"))
        self.pushButton_4.setText(_translate("Dialog", "传递端面参数"))
        self.pushButton_5.setText(_translate("Dialog", "传递侧面参数"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "please choose method"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "none"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Black_hat"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Fourier_transform"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Light_compensation"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "please choose method"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "global"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "adaptive"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "local"))
        self.label_5.setText(_translate("Dialog", "图 片 所 属 类 型："))
        self.label_6.setText(_translate("Dialog", "选 择 模 板 图 片："))
        self.comboBox_4.setItemText(0, _translate("Dialog", "sample1"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "sample2"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "sample3"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "sample4"))


class Start_Do(QThread):

    def __init__(self, parent=None):
        super(Start_Do, self).__init__(parent)

    def run(self):
        os.system('for_test.exe')


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