# -*- coding: utf-8 -*-
"""
@author: Tu Qiuping
@software: PyCharm
@file: mainwindow.py.py
@time: 10/9/2021 10:51 PM
"""
import json
import os
import cv2
import time
import webbrowser
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
from PyQt5.Qt import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from ui_mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QGraphicsScene, QGraphicsPixmapItem, qApp
from functions import large_cylinder_top, concentric_cylinder_top, lid_cylinder_top, cylinder_side

global directory
directory = "C:/"
global template
template = "C:/"
global save_path
save_path = "C:/"
global value_duan
value_duan = 15
global value_ce
value_ce = 15
global min_duan
min_duan = 0
global min_ce
min_ce = 0
global remove_ce
remove_ce = 0
global sample
sample = 0
global duan_contours
duan_contours = 0
global ce_contours1
ce_contours1 = 0
global ce_contours2
ce_contours2 = 0
global ce_contours3
ce_contours3 = 0
global ce_contours4
ce_contours4 = 0
global stopflag
stopflag = 0
global total_num
total_num = 0
global unqualified
unqualified = 0
global unqualified_duan
unqualified_duan = 0
global unqualified_ce
unqualified_ce = 0
global good_rate
good_rate = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        MainWindow.setWindowIcon(self, QIcon('./gui/Icon.png'))
        self.actionstart.triggered.connect(self.start_system)
        self.actionabout_2.triggered.connect(self.about)
        self.actionchooseTemplate.triggered.connect(self.get_template)
        self.actionexit.triggered.connect(qApp.quit)
        self.actionhelp_2.triggered.connect(self.help)
        self.actionipconfig.triggered.connect(self.find_plc)
        # self.actionmax.triggered.connect(self.max)
        # self.actionmin_2.triggered.connect(self.max)
        self.actionsave.triggered.connect(self.save_computer_result)
        self.actionsetSavePath.triggered.connect(self.set_save_path)
        self.actionsetPicPath.triggered.connect(self.set_pic_path)
        self.actionsetParaments.triggered.connect(self.set_paraments)
        self.actionstop.triggered.connect(self.stop_system)
        # self.actionsetValue.triggered.connect(self.set_Value)
        self.actiondelay_time.triggered.connect(self.set_delay_time)
        # self.actionmethod_side.triggered.connect(self.set_side_method)
        self.actiontools.triggered.connect(self.showtools)
        self.actionset_yzFf_duan.triggered.connect(self.set_methodAndthreshold_duan)
        self.actionset_yzFf_ce.triggered.connect(self.set_methodAndthreshold_ce)
        self.pushButton_16.clicked.connect(self.openpic_tool)
        self.pushButton_18.clicked.connect(self.rgb2gray)
        self.pushButton_13.clicked.connect(self.threshold_seg_OSTU)
        self.pushButton_14.clicked.connect(self.morphology_processing)
        self.pushButton_15.clicked.connect(self.feature_extraction)
        self.pushButton_2.clicked.connect(self.H_pass_filter)
        self.pushButton_3.clicked.connect(self.L_pass_filter)
        self.pushButton_4.clicked.connect(self.smoothing_filter)
        self.pushButton_5.clicked.connect(self.sharpening_filter)
        self.pushButton_6.clicked.connect(self.R_Histogram)
        self.pushButton_7.clicked.connect(self.G_Histogram)
        self.pushButton_8.clicked.connect(self.B_Histogram)
        self.pushButton_9.clicked.connect(self.false_color_enhancement)
        self.pushButton_10.clicked.connect(self.true_color_enhancement)
        self.pushButton_11.clicked.connect(self.histogram_equalization)
        self.pushButton_12.clicked.connect(self.HSV_color_model)
        # self.pushButton_17.clicked.connect(self.save_pic_tool)
        self.pushButton.clicked.connect(self.clear_pic_tool)

    def clear_pic_tool(self):
        result = cv2.imread('./gui/white.jpg')
        frame = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        self.graphicsView_3.setScene(self.scene)
        self.graphicsView_3.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        self.graphicsView_4.setScene(self.scene)
        self.graphicsView_4.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        self.graphicsView_5.setScene(self.scene)
        self.graphicsView_5.fitInView(QGraphicsPixmapItem(QPixmap(frame)))

    def HSV_color_model(self):
        global pic_name
        img = cv2.imread(pic_name)
        result_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.putText(result_hsv, 'HSV', (10, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        cv2.imwrite('hsv.jpg', result_hsv)
        result = cv2.imread('hsv.jpg')
        frame = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_4.setScene(self.scene)
        self.graphicsView_4.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        os.remove('hsv.jpg')

    def histogram_equalization(self):
        global pic_name
        img = cv2.imread(pic_name, cv2.IMREAD_GRAYSCALE)
        result_equ = cv2.equalizeHist(img)
        result_equ = cv2.cvtColor(result_equ, cv2.COLOR_GRAY2BGR)
        cv2.putText(result_equ, 'equalization', (10, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        frame = cv2.cvtColor(result_equ, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_4.setScene(self.scene)
        self.graphicsView_4.fitInView(QGraphicsPixmapItem(QPixmap(frame)))

    def true_color_enhancement(self):
        global pic_name
        img = cv2.imread(pic_name)
        lut = np.zeros(256, dtype=np.float32)
        for i in range(256):
            lut[i] = 0.00000005 * i ** 4.0
        result_true = cv2.LUT(img, lut)
        result_true = np.uint8(result_true + 0.5)
        cv2.putText(result_true, 'gamma', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        frame = cv2.cvtColor(result_true, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_3.setScene(self.scene)
        self.graphicsView_3.fitInView(QGraphicsPixmapItem(QPixmap(frame)))

    def false_color_enhancement(self):
        global pic_name
        # img = cv2.imread(pic_name, 2)
        im_gray = cv2.imread(pic_name, cv2.IMREAD_GRAYSCALE)
        result_false = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
        cv2.putText(result_false, 'false_color', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        frame = cv2.cvtColor(result_false, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(QGraphicsPixmapItem(QPixmap(frame)))

    def B_Histogram(self):
        global pic_name
        img = cv2.imread(pic_name)
        hist_B = cv2.calcHist([img], [0], None, [256], [0, 255])
        plt.plot(hist_B, color='b')
        plt.xlim([0, 256])
        plt.savefig('hist_b.jpg')
        result_b = cv2.imread('hist_b.jpg')
        cv2.putText(result_b, 'hist_b picture', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        frame = cv2.cvtColor(result_b, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_4.setScene(self.scene)
        self.graphicsView_4.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        os.remove('hist_b.jpg')

    def G_Histogram(self):
        global pic_name
        img = cv2.imread(pic_name)
        hist_G = cv2.calcHist([img], [1], None, [256], [0, 255])
        plt.plot(hist_G, color='g')
        plt.xlim([0, 256])
        plt.savefig('hist_g.jpg')
        result_g = cv2.imread('hist_g.jpg')
        cv2.putText(result_g, 'hist_g picture', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        frame = cv2.cvtColor(result_g, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_3.setScene(self.scene)
        self.graphicsView_3.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        os.remove('hist_g.jpg')

    def R_Histogram(self):
        global pic_name
        img = cv2.imread(pic_name)
        hist_R = cv2.calcHist([img], [2], None, [256], [0, 255])
        plt.plot(hist_R, color='r')
        plt.xlim([0, 256])
        plt.savefig('hist_r.jpg')
        result_r = cv2.imread('hist_r.jpg')
        cv2.putText(result_r, 'hist_r picture', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        frame = cv2.cvtColor(result_r, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        os.remove('hist_r.jpg')

    def sharpening_filter(self):
        global pic_name
        img = cv2.imread(pic_name, 0)
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
        dst = cv2.filter2D(img, -1, kernel=kernel)
        dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
        cv2.putText(dst, 'sharpening picture', (10, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        frame = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_5.setScene(self.scene)
        self.graphicsView_5.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        return dst

    def smoothing_filter(self):
        global pic_name
        img = cv2.imread(pic_name, 0)
        img = cv2.blur(img, (5, 5))
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        cv2.putText(img, 'smoothing picture', (10, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_4.setScene(self.scene)
        self.graphicsView_4.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        return img

    def L_pass_filter(self):
        global pic_name
        img = cv2.imread(pic_name, 0)
        dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
        dftshift = np.fft.fftshift(dft)
        rows, cols = img.shape
        crow, ccol = int(rows / 2), int(cols / 2)
        mask = np.zeros((rows, cols, 2), np.uint8)
        mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1
        fshit = dftshift * mask
        ishit = np.fft.ifftshift(fshit)
        iImg = cv2.idft(ishit)
        iImg = cv2.magnitude(iImg[:, :, 0], iImg[:, :, 1])
        iImg = np.array(iImg, dtype='uint8')
        iImg = cv2.cvtColor(iImg, cv2.COLOR_GRAY2BGR)
        cv2.putText(iImg, 'LPF picture', (10, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        frame = cv2.cvtColor(iImg, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_3.setScene(self.scene)
        self.graphicsView_3.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        return iImg

    def H_pass_filter(self):
        global pic_name
        img = cv2.imread(pic_name)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        f = np.fft.fft2(img_gray)
        fshift = np.fft.fftshift(f)
        rows, cols = img_gray.shape
        crow, ccol = int(rows / 2), int(cols / 2)
        fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0  # 设置高通滤波器
        ishift = np.fft.ifftshift(fshift)
        iimg = np.fft.ifft2(ishift)
        iimg = np.abs(iimg)
        iimg = np.array(iimg, dtype='uint8')
        iimg1 = cv2.cvtColor(iimg, cv2.COLOR_GRAY2BGR)  # 傅里叶逆变换
        cv2.putText(iimg1, 'HPF picture', (10, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        frame = cv2.cvtColor(iimg1, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        return iimg1

    def feature_extraction(self):
        global pic_name
        img = cv2.imread(pic_name)
        img_copy = img.copy()
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        t, dst = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        result = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)
        _, contour, _ = cv2.findContours(result, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(img_copy, contour, -1, [0, 0, 255], 2)
        cv2.putText(img_copy, 'feature picture', (10, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        frame = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_5.setScene(self.scene)
        self.graphicsView_5.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        return img_copy

    def morphology_processing(self):
        global pic_name
        img = cv2.imread(pic_name)
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        t, dst = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        result = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)
        result_rgb = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
        cv2.putText(result_rgb, 'morphology picture', (10, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        frame = cv2.cvtColor(result_rgb, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_4.setScene(self.scene)
        self.graphicsView_4.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        return result_rgb

    def threshold_seg_OSTU(self):
        global pic_name
        img = cv2.imread(pic_name)
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        t, dst = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        dst_rgb = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
        cv2.putText(dst_rgb, 'threshold picture', (10, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        frame = cv2.cvtColor(dst_rgb, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_3.setScene(self.scene)
        self.graphicsView_3.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        return dst

    def rgb2gray(self):
        global pic_name
        img = cv2.imread(pic_name)
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cv2.putText(img_gray, 'gray picture', (10, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        frame = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
        h, w, c = frame.shape
        frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.scene.clearSelection()
        self.item.setSelected(True)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
        return img_gray

    def openpic_tool(self):
        global pic_name
        pic_name, imgtype = QFileDialog.getOpenFileName(self, '打开图片(不要选择中文路径)', '', "*.jpg;;*.png;;*.bmp;;*.tiff;;All Files(*)")
        self.textBrowser_2.setText(pic_name)
        print(pic_name)
        if pic_name == '':
            pass
        else:
            origin_pic = cv2.imread(pic_name)
            cv2.putText(origin_pic, 'original picture', (10, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
            frame = cv2.cvtColor(origin_pic, cv2.COLOR_BGR2RGB)
            h, w, c = frame.shape
            frame = QImage(frame, w, h, 3 * w, QImage.Format_RGB888)  # 处理图片虚影问题**
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.scene.clearSelection()
            self.item.setSelected(True)
            self.graphicsView.setScene(self.scene)
            self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(frame)))
            return pic_name

    def showtools(self):
        self.tools = Show_Tools()
        self.tools.start()

    def set_methodAndthreshold_ce(self):
        self.side_methodandthreshold = Side_Methodthreshold()
        self.side_methodandthreshold.start()

    def save_computer_result(self):
        global stopflag
        global save_path
        time_save = time.time()
        timeArray_save = time.localtime(time_save)
        otherStyleTime_save = time.strftime("%Y%m%d_%H%M%S", timeArray_save)
        otherStyleTime_save_show = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_save)
        if stopflag == 1:
            all_num = self.textBrowser.toPlainText()
            ng_num = self.textBrowser_4.toPlainText()
            duan_ng_num = self.textBrowser_6.toPlainText()
            ce_ng_num = self.textBrowser_7.toPlainText()
            rate = self.textBrowser_5.toPlainText()
            result_file = save_path + '/' + 'result_' + otherStyleTime_save + '.txt'
            file = open(result_file, 'a')
            file.write('检测总数：' + all_num)
            file.write('\n')
            file.write('不合格数：' + ng_num)
            file.write('\n')
            file.write('端面不合格数：' + duan_ng_num)
            file.write('\n')
            file.write('侧面不合格数：' + ce_ng_num)
            file.write('\n')
            file.write('良品率：' + rate)
            file.write('\n')
            file.close()
            self.textBrowser_2.append(otherStyleTime_save_show + '：已保存检测结果，保存路径为：' + result_file)
        else:
            QMessageBox.warning(self, '警告', '保存前请确保已经检测完成或已暂停检测！', QMessageBox.Yes)

    def set_methodAndthreshold_duan(self):
        self.set_valueandmethod = Valueandmethod_duan()
        self.set_valueandmethod.start()

    def find_plc(self):
        self.ip_plc = Ip_Plc()
        self.ip_plc.start()

    def stop_system(self):
        global stopflag
        if stopflag == 0:
            stopflag = 1
        else:
            stopflag = 0
            self.actionstart.setEnabled(True)
        return stopflag

    def start_system(self):
        self.actionstart.setEnabled(False)
        with open('./paraments/paraments.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        sample = data['sample']
        if int(sample) == 1:
            self.textBrowser_9.setText('样品一')
        if int(sample) == 2:
            self.textBrowser_9.setText('样品二')
        if int(sample) == 3:
            self.textBrowser_9.setText('样品三')
        if int(sample) == 4:
            self.textBrowser_9.setText('样品四')
        detect_model = data['detect_model']
        if detect_model == 'on_line':
            with open('./paraments/communication.json', 'r', encoding='utf-8') as json_file2:
                data2 = json.load(json_file2)
            ip = data2['ip']
            port = data2['port']
            json_file2.close()
            print('我是启动按钮开始执行的地方')
            self.th = Trigger(ip_adress=str(ip), port_adress=int(port))
            self.th.finishSignal.connect(self.start_system_online)
            self.th.start()
            print('启动系统按钮显示触发多线程已启动')
        if detect_model == 'off_line':
            self.start_system_offline(1)
            pix = QPixmap('./gui/red_circle_32.png')
            self.label_5.setPixmap(pix)
            self.label_5.setScaledContents(True)
            self.show()
            self.actionstart.setEnabled(True)

    def start_system_offline(self, msg):
        global ip
        global port
        global duan_contours
        global ce_contours1
        global ce_contours2
        global ce_contours3
        global ce_contours4
        global side1_result
        global side2_result
        global side3_result
        global side4_result
        global top_result
        global total_num
        global unqualified
        global unqualified_duan
        global unqualified_ce
        global good_rate

        print('我是msg：', msg)
        if msg == 1:
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_7.setPixmap(pix)
            self.label_7.setScaledContents(True)
            self.show()
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_8.setPixmap(pix)
            self.label_8.setScaledContents(True)
            self.show()
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_9.setPixmap(pix)
            self.label_9.setScaledContents(True)
            self.show()
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_10.setPixmap(pix)
            self.label_10.setScaledContents(True)
            self.show()
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_11.setPixmap(pix)
            self.label_11.setScaledContents(True)
            self.show()
            with open('./paraments/paraments.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            directory = data['directory']
            template = data['template']
            value_duan = data['value_duan']
            value_ce = data['value_ce']
            c_duan = data['c_duan']
            c_ce = data['c_ce']
            min_duan = data['min_duan']
            min_ce = data['min_ce']
            block = data['block']
            method_duan = data['method_duan']
            method_ce = data['method_ce']
            yzfg_duan = data['yzfg_duan']
            yzfg_ce = data['yzfg_ce']
            sample = data['sample']
            json_file.close()
            print(type(sample))
            d1 = os.listdir(directory)[1]
            d2 = os.listdir(directory)[2]
            d3 = os.listdir(directory)[3]
            d4 = os.listdir(directory)[4]
            d5 = os.listdir(directory)[0]
            file1 = glob(directory + '/' + str(d1) + '/*jpg')[0]
            file2 = glob(directory + '/' + str(d2) + '/*jpg')[0]
            file3 = glob(directory + '/' + str(d3) + '/*jpg')[0]
            file4 = glob(directory + '/' + str(d4) + '/*jpg')[0]
            file5 = glob(directory + '/' + str(d5) + '/*jpg')[0]
            template_file1 = glob(template + '/*jpg')[0]
            template_file2 = glob(template + '/*jpg')[1]
            template_file3 = glob(template + '/*jpg')[2]
            template_file4 = glob(template + '/*jpg')[3]

            if stopflag == 0:
                total_num = total_num + 1
                self.textBrowser_3.setText(str(total_num))
                time1 = time.time()
                timeArray = time.localtime(time1)
                otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                self.textBrowser.append(otherStyleTime + '：开始加载json文件参数和图片进行检测')
                print('开始加载json文件参数进行检测')
                # 根据样品型号进行检测，首先是样品一（大圆柱）
                if sample == '1':
                    # 这个是端面检测
                    img0 = cv2.imread(file5)
                    img0_copy = img0.copy()
                    img0_roi = large_cylinder_top.get_roi_large_cylinder(img0_copy)
                    top_result, countor0 = large_cylinder_top.detect_large_cylinder_result(img0_copy, img0_roi,
                                            int(value_duan), float(c_duan), str(method_duan), str(yzfg_duan),
                                            float(min_duan), int(block))
                    # 这个是侧面检测
                    template_img1 = cv2.imread(template_file1)
                    template_img2 = cv2.imread(template_file2)
                    template_img3 = cv2.imread(template_file3)
                    template_img4 = cv2.imread(template_file4)
                    img1 = cv2.imread(file1)
                    img2 = cv2.imread(file2)
                    img3 = cv2.imread(file3)
                    img4 = cv2.imread(file4)
                    img1_roi, img1_temp, min1_loc, temp1_w, temp1_h = cylinder_side.get_roi(img1, template_img1)
                    side1_result, countor1 = cylinder_side.detect_concentric_side(img1, img1_roi, img1_temp, min1_loc,
                                            temp1_w, temp1_h, str(method_ce), str(yzfg_ce), int(value_ce), float(c_ce),
                                            float(min_ce), int(block))
                    img2_roi, img2_temp, min2_loc, temp2_w, temp2_h = cylinder_side.get_roi(img2, template_img2)
                    side2_result, countor2 = cylinder_side.detect_concentric_side(img2, img2_roi, img2_temp, min2_loc,
                                            temp2_w, temp2_h, str(method_ce), str(yzfg_ce), int(value_ce), float(c_ce),
                                            float(min_ce), int(block))
                    img3_roi, img3_temp, min3_loc, temp3_w, temp3_h = cylinder_side.get_roi(img3, template_img3)
                    side3_result, countor3 = cylinder_side.detect_concentric_side(img3, img3_roi, img3_temp, min3_loc,
                                            temp3_w, temp3_h, str(method_ce), str(yzfg_ce), int(value_ce), float(c_ce),
                                            float(min_ce), int(block))
                    img4_roi, img4_temp, min4_loc, temp4_w, temp4_h = cylinder_side.get_roi(img4, template_img4)
                    side4_result, countor4 = cylinder_side.detect_concentric_side(img4, img4_roi, img4_temp, min4_loc,
                                            temp4_w, temp4_h, str(method_ce), str(yzfg_ce), int(value_ce), float(c_ce),
                                            float(min_ce), int(block))
                # 根据样品型号进行检测，样品二（小圆柱）
                if sample == '2':
                    # 这个是端面检测
                    img0 = cv2.imread(file5)
                    img0_copy = img0.copy()
                    img0_roi = large_cylinder_top.get_roi_large_cylinder(img0_copy)
                    top_result, countor0 = large_cylinder_top.detect_large_cylinder_result(img0_copy, img0_roi,
                                                        int(value_duan), float(c_duan), str(method_duan), str(yzfg_duan),
                                                                                           float(min_duan), int(block))
                    # 这个是侧面检测
                    template_img1 = cv2.imread(template_file1)
                    template_img2 = cv2.imread(template_file2)
                    template_img3 = cv2.imread(template_file3)
                    template_img4 = cv2.imread(template_file4)
                    img1 = cv2.imread(file1)
                    img2 = cv2.imread(file2)
                    img3 = cv2.imread(file3)
                    img4 = cv2.imread(file4)
                    img1_roi, img1_temp, min1_loc, temp1_w, temp1_h = cylinder_side.get_roi(img1, template_img1)
                    side1_result, countor1 = cylinder_side.detect_concentric_side(img1, img1_roi, img1_temp, min1_loc,
                                                                                  temp1_w, temp1_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                    img2_roi, img2_temp, min2_loc, temp2_w, temp2_h = cylinder_side.get_roi(img2, template_img2)
                    side2_result, countor2 = cylinder_side.detect_concentric_side(img2, img2_roi, img2_temp, min2_loc,
                                                                                  temp2_w, temp2_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                    img3_roi, img3_temp, min3_loc, temp3_w, temp3_h = cylinder_side.get_roi(img3, template_img3)
                    side3_result, countor3 = cylinder_side.detect_concentric_side(img3, img3_roi, img3_temp, min3_loc,
                                                                                  temp3_w, temp3_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                    img4_roi, img4_temp, min4_loc, temp4_w, temp4_h = cylinder_side.get_roi(img4, template_img4)
                    side4_result, countor4 = cylinder_side.detect_concentric_side(img4, img4_roi, img4_temp, min4_loc,
                                                                                  temp4_w, temp4_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                # 根据样品型号进行检测，样品三（同心圆圆柱）
                if sample == '3':
                    # 这是端面检测
                    img0 = cv2.imread(file5)
                    # img0 = cv2.resize(img0, (int(img0.shape[1] / 2), int(img0.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
                    dst1, dst2 = concentric_cylinder_top.get_roi_concentric(img0)
                    top_result, countor0 = concentric_cylinder_top.detect_concentric_result(img0, dst1, dst2,
                                           int(value_duan), float(c_duan), str(method_duan), str(yzfg_duan),
                                                                                            float(min_duan), int(block))
                    # 这次侧面检测
                    template_img1 = cv2.imread(template_file1)
                    template_img2 = cv2.imread(template_file2)
                    template_img3 = cv2.imread(template_file3)
                    template_img4 = cv2.imread(template_file4)
                    img1 = cv2.imread(file1)
                    img2 = cv2.imread(file2)
                    img3 = cv2.imread(file3)
                    img4 = cv2.imread(file4)
                    img1_roi, img1_temp, min1_loc, temp1_w, temp1_h = cylinder_side.get_roi(img1, template_img1)
                    side1_result, countor1 = cylinder_side.detect_concentric_side(img1, img1_roi, img1_temp, min1_loc,
                                                                                  temp1_w, temp1_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                    img2_roi, img2_temp, min2_loc, temp2_w, temp2_h = cylinder_side.get_roi(img2, template_img2)
                    side2_result, countor2 = cylinder_side.detect_concentric_side(img2, img2_roi, img2_temp, min2_loc,
                                                                                  temp2_w, temp2_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                    img3_roi, img3_temp, min3_loc, temp3_w, temp3_h = cylinder_side.get_roi(img3, template_img3)
                    side3_result, countor3 = cylinder_side.detect_concentric_side(img3, img3_roi, img3_temp, min3_loc,
                                                                                  temp3_w, temp3_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                    img4_roi, img4_temp, min4_loc, temp4_w, temp4_h = cylinder_side.get_roi(img4, template_img4)
                    side4_result, countor4 = cylinder_side.detect_concentric_side(img4, img4_roi, img4_temp, min4_loc,
                                                                                  temp4_w, temp4_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                # 根据样品型号进行检测，样品四（穹顶圆柱零件）
                if sample == '4':
                    # 这是端面检测
                    img0 = cv2.imread(file5)
                    img0 = cv2.resize(img0, (int(img0.shape[1] / 2), int(img0.shape[0] / 2)),
                                      interpolation=cv2.INTER_CUBIC)
                    temp_lid = cv2.imread('./paraments/lid_cylinder_template.jpg')
                    temp_lid = cv2.resize(temp_lid, (int(temp_lid.shape[1] / 2), int(temp_lid.shape[0] / 2)),
                                      interpolation=cv2.INTER_CUBIC)
                    dst = lid_cylinder_top.trans2binary(img0)
                    img0_circle0, img0_circle1 = lid_cylinder_top.get_roi_lid(img0, dst, temp_lid)
                    top_result, countor0 = lid_cylinder_top.detect_lid_result(img0, img0_circle0, img0_circle1,
                                                                              int(value_duan), float(c_duan),
                                                                              str(method_duan), str(yzfg_duan),
                                                                              float(min_duan), int(block))
                    # 接下来是侧面检测
                    template_img1 = cv2.imread(template_file1)
                    template_img2 = cv2.imread(template_file2)
                    template_img3 = cv2.imread(template_file3)
                    template_img4 = cv2.imread(template_file4)
                    img1 = cv2.imread(file1)
                    img2 = cv2.imread(file2)
                    img3 = cv2.imread(file3)
                    img4 = cv2.imread(file4)
                    img1_roi, img1_temp, min1_loc, temp1_w, temp1_h = cylinder_side.get_roi(img1, template_img1)
                    side1_result, countor1 = cylinder_side.detect_concentric_side(img1, img1_roi, img1_temp, min1_loc,
                                                                                  temp1_w, temp1_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                    img2_roi, img2_temp, min2_loc, temp2_w, temp2_h = cylinder_side.get_roi(img2, template_img2)
                    side2_result, countor2 = cylinder_side.detect_concentric_side(img2, img2_roi, img2_temp, min2_loc,
                                                                                  temp2_w, temp2_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                    img3_roi, img3_temp, min3_loc, temp3_w, temp3_h = cylinder_side.get_roi(img3, template_img3)
                    side3_result, countor3 = cylinder_side.detect_concentric_side(img3, img3_roi, img3_temp, min3_loc,
                                                                                  temp3_w, temp3_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                    img4_roi, img4_temp, min4_loc, temp4_w, temp4_h = cylinder_side.get_roi(img4, template_img4)
                    side4_result, countor4 = cylinder_side.detect_concentric_side(img4, img4_roi, img4_temp, min4_loc,
                                                                                  temp4_w, temp4_h, str(method_ce),
                                                                                  str(yzfg_ce), int(value_ce),
                                                                                  float(c_ce),
                                                                                  float(min_ce), int(block))
                img1, img2, img3, img4, img5 = side1_result, side2_result, side3_result, side4_result, top_result
                # frame1 = cv2.resize(img1, (381, 301))
                frame1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
                h1, w1, c1 = frame1.shape
                frame1 = QImage(frame1, w1, h1, 3 * w1, QImage.Format_RGB888)  # 处理图片虚影问题**
                pix1 = QPixmap.fromImage(frame1)
                self.item = QGraphicsPixmapItem(pix1)  # 创建像素图元
                self.scene = QGraphicsScene()  # 创建场景
                self.scene.addItem(self.item)
                self.scene.clearSelection()
                self.item.setSelected(True)
                self.graphicsView.setScene(self.scene)
                self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(frame1)))

                # frame2 = cv2.resize(img2, (381, 301))
                frame2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
                h2, w2, c2 = frame2.shape
                frame2 = QImage(frame2, w2, h2, 3 * w2, QImage.Format_RGB888)  # 处理图片虚影问题**
                pix2 = QPixmap.fromImage(frame2)
                self.item = QGraphicsPixmapItem(pix2)  # 创建像素图元
                self.scene = QGraphicsScene()  # 创建场景
                self.scene.addItem(self.item)
                self.scene.clearSelection()
                self.item.setSelected(True)
                self.graphicsView_2.setScene(self.scene)
                self.graphicsView_2.fitInView(QGraphicsPixmapItem(QPixmap(frame2)))

                # frame3 = cv2.resize(img3, (381, 301))
                frame3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
                h3, w3, c3 = frame3.shape
                frame3 = QImage(frame3, w3, h3, 3 * w3, QImage.Format_RGB888)  # 处理图片虚影问题**
                pix3 = QPixmap.fromImage(frame3)
                self.item = QGraphicsPixmapItem(pix3)  # 创建像素图元
                self.scene = QGraphicsScene()  # 创建场景
                self.scene.addItem(self.item)
                self.scene.clearSelection()
                self.item.setSelected(True)
                self.graphicsView_3.setScene(self.scene)
                self.graphicsView_3.fitInView(QGraphicsPixmapItem(QPixmap(frame3)))

                # frame4 = cv2.resize(img4, (381, 301))
                frame4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
                h4, w4, c4 = frame4.shape
                frame4 = QImage(frame4, w4, h4, 3 * w4, QImage.Format_RGB888)  # 处理图片虚影问题**
                pix4 = QPixmap.fromImage(frame4)
                self.item = QGraphicsPixmapItem(pix4)  # 创建像素图元
                self.scene = QGraphicsScene()  # 创建场景
                self.scene.addItem(self.item)
                self.scene.clearSelection()
                self.item.setSelected(True)
                self.graphicsView_4.setScene(self.scene)
                self.graphicsView_4.fitInView(QGraphicsPixmapItem(QPixmap(frame4)))

                # frame5 = cv2.resize(img5, (431, 323))
                frame5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
                h5, w5, c5 = frame5.shape
                frame5 = QImage(frame5, w5, h5, 3 * w5, QImage.Format_RGB888)  # 处理图片虚影问题**
                pix5 = QPixmap.fromImage(frame5)
                self.item = QGraphicsPixmapItem(pix5)  # 创建像素图元
                self.scene = QGraphicsScene()  # 创建场景
                self.scene.addItem(self.item)
                self.scene.clearSelection()
                self.item.setSelected(True)
                self.graphicsView_5.setScene(self.scene)
                self.graphicsView_5.fitInView(QGraphicsPixmapItem(QPixmap(frame5)))

                duan_contours, ce_contours1, ce_contours2, ce_contours3, ce_contours4 = countor0, len(countor1), len(countor2), len(countor3), len(countor4)

                time2 = time.time()
                timeArray2 = time.localtime(time2)
                otherStyleTime2 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray2)
                self.textBrowser.append(otherStyleTime2 + '：检测完成！耗时' + str(time2 - time1) + 's')
                self.textBrowser_7.setText(str(round((time2 - time1), 4)))
                print(otherStyleTime2 + '：检测完成！耗时' + str(time2 - time1) + 's')

                if duan_contours > 0 or ce_contours1 > 0 or ce_contours2 > 0 or ce_contours3 > 0 or ce_contours4 > 0:
                    unqualified = unqualified + 1
                    self.textBrowser_4.setText(str(unqualified))
                    time3 = time.time()
                    timeArray3 = time.localtime(time3)
                    otherStyleTime3 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray3)
                    self.textBrowser.append(otherStyleTime3 + '：开始检测到信号传递完成共耗时：' + str(time3 - time1) + 's')
                    if duan_contours > 0:
                        unqualified_duan = unqualified_duan + 1
                        self.textBrowser_6.setText(str(unqualified_duan))
                    else:
                        self.textBrowser_6.setText(str(unqualified_duan))
                    if ce_contours1 > 0 or ce_contours2 > 0 or ce_contours3 > 0 or ce_contours4 > 0:
                        unqualified_ce = unqualified_ce + 1
                        self.textBrowser_8.setText(str(unqualified_ce))
                    else:
                        self.textBrowser_8.setText(str(unqualified_ce))
                else:
                    unqualified = unqualified + 0
                good_rate = (total_num - unqualified) / total_num
                self.textBrowser_5.setText(str(good_rate))
            else:
                time_stop = time.time()
                timeArray_stop = time.localtime(time_stop)
                otherStyleTime_stop = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_stop)
                self.textBrowser.append(otherStyleTime_stop + '：系统已暂停，请重新启动系统再开始检测。')
                # QMessageBox.critical(self, '错误', '已暂停系统，请点击启动系统按钮再检测', QMessageBox.Yes)

    def start_system_online(self, msg):
        global ip
        global port
        global duan_contours
        global ce_contours1
        global ce_contours2
        global ce_contours3
        global ce_contours4
        global total_num
        global unqualified
        global unqualified_duan
        global unqualified_ce
        global good_rate

        print('我是msg：', msg)
        if msg == 1:
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_7.setPixmap(pix)
            self.label_7.setScaledContents(True)
            self.show()
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_8.setPixmap(pix)
            self.label_8.setScaledContents(True)
            self.show()
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_9.setPixmap(pix)
            self.label_9.setScaledContents(True)
            self.show()
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_10.setPixmap(pix)
            self.label_10.setScaledContents(True)
            self.show()
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_11.setPixmap(pix)
            self.label_11.setScaledContents(True)
            self.show()
            with open('./paraments/paraments.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            directory = data['directory']
            template = data['template']
            value_duan = data['value_duan']
            value_ce = data['value_ce']
            c_duan = data['c_duan']
            c_ce = data['c_ce']
            min_duan = data['min_duan']
            min_ce = data['min_ce']
            block = data['block']
            method_duan = data['method_duan']
            method_ce = data['method_ce']
            yzfg_duan = data['yzfg_duan']
            yzfg_ce = data['yzfg_ce']
            sample = data['sample']
            json_file.close()

            d1 = os.listdir(directory)[0]
            d2 = os.listdir(directory)[1]
            d3 = os.listdir(directory)[2]
            d4 = os.listdir(directory)[3]
            d5 = os.listdir(directory)[4]
            print(1111111111111111111111111111111111111111111111111111)
            print(d1)
            target_dir1 = directory + '/' + str(d1)
            target_dir2 = directory + '/' + str(d2)
            target_dir3 = directory + '/' + str(d3)
            target_dir4 = directory + '/' + str(d4)
            target_dir5 = directory + '/' + str(d5)

            l1, l2, l3, l4, l5 = len(os.listdir(target_dir1)), len(os.listdir(target_dir2)), len(
                os.listdir(target_dir3)), len(os.listdir(target_dir4)), len(os.listdir(target_dir5))
            flag = [l1 != 0, l2 != 0, l3 != 0, l4 != 0, l5 != 0]
            if False not in flag:
                file1 = glob(directory + '/' + str(d1) + '/*jpg')[0]
                file2 = glob(directory + '/' + str(d2) + '/*jpg')[0]
                file3 = glob(directory + '/' + str(d3) + '/*jpg')[0]
                file4 = glob(directory + '/' + str(d4) + '/*jpg')[0]
                file5 = glob(directory + '/' + str(d5) + '/*jpg')[0]
                print("#########################################", file5)
                template_file1 = glob(template + '/*jpg')[0]
                template_file2 = glob(template + '/*jpg')[1]
                template_file3 = glob(template + '/*jpg')[2]
                template_file4 = glob(template + '/*jpg')[3]

                template_img1 = cv2.imread(template_file1)
                template_img2 = cv2.imread(template_file2)
                template_img3 = cv2.imread(template_file3)
                template_img4 = cv2.imread(template_file4)
                img1 = cv2.imread(file1)
                img2 = cv2.imread(file2)
                img3 = cv2.imread(file3)
                img4 = cv2.imread(file4)
                img1 = cv2.resize(img1, (int(img1.shape[1] / 2), int(img1.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
                img2 = cv2.resize(img2, (int(img2.shape[1] / 2), int(img2.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
                img3 = cv2.resize(img3, (int(img3.shape[1] / 2), int(img3.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
                img4 = cv2.resize(img4, (int(img4.shape[1] / 2), int(img4.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
                template_img1 = cv2.resize(template_img1,
                                           (int(template_img1.shape[1] / 2), int(template_img1.shape[0] / 2)),
                                           interpolation=cv2.INTER_CUBIC)
                template_img1 = cv2.resize(template_img1,
                                           (int(template_img2.shape[1] / 2), int(template_img2.shape[0] / 2)),
                                           interpolation=cv2.INTER_CUBIC)
                template_img2 = cv2.resize(template_img2,
                                           (int(template_img3.shape[1] / 2), int(template_img3.shape[0] / 2)),
                                           interpolation=cv2.INTER_CUBIC)
                template_img3 = cv2.resize(template_img3,
                                           (int(template_img4.shape[1] / 2), int(template_img4.shape[0] / 2)),
                                           interpolation=cv2.INTER_CUBIC)
                template_img4 = cv2.resize(template_img4,
                                           (int(template_img4.shape[1] / 2), int(template_img4.shape[0] / 2)),
                                           interpolation=cv2.INTER_CUBIC)

                if stopflag == 0:
                    total_num = total_num + 1
                    self.textBrowser_3.setText(str(total_num))
                    time1 = time.time()
                    timeArray = time.localtime(time1)
                    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    self.textBrowser.append(otherStyleTime + ': 开始加载json文件参数和图片进行检测')
                    print('开始加载json文件参数进行检测')
                    # 根据样品型号进行检测，首先是样品一（大圆柱）
                    time.sleep(0.5)
                    if sample == '1':
                        # 这个是端面检测
                        img0 = cv2.imread(file5)
                        # img0 = cv2.resize(img0, (int(img0.shape[1] / 2), int(img0.shape[0] / 2)),
                        #                    interpolation=cv2.INTER_CUBIC)
                        img0_copy = img0.copy()
                        img0_roi = large_cylinder_top.get_roi_large_cylinder(img0_copy)
                        top_result, countor0 = large_cylinder_top.detect_large_cylinder_result(img0_copy, img0_roi,
                                                                                               int(value_duan), float(c_duan),
                                                                                               str(method_duan),
                                                                                               str(yzfg_duan),
                                                                                               float(min_duan), int(block))
                        # 这个是侧面检测
                        img1_roi, img1_temp, min1_loc, temp1_w, temp1_h = cylinder_side.get_roi(img1, template_img1)
                        side1_result, countor1 = cylinder_side.detect_concentric_side(img1, img1_roi, img1_temp, min1_loc,
                                                                                      temp1_w, temp1_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img2_roi, img2_temp, min2_loc, temp2_w, temp2_h = cylinder_side.get_roi(img2, template_img2)
                        side2_result, countor2 = cylinder_side.detect_concentric_side(img2, img2_roi, img2_temp, min2_loc,
                                                                                      temp2_w, temp2_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img3_roi, img3_temp, min3_loc, temp3_w, temp3_h = cylinder_side.get_roi(img3, template_img3)
                        side3_result, countor3 = cylinder_side.detect_concentric_side(img3, img3_roi, img3_temp, min3_loc,
                                                                                      temp3_w, temp3_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img4_roi, img4_temp, min4_loc, temp4_w, temp4_h = cylinder_side.get_roi(img4, template_img4)
                        side4_result, countor4 = cylinder_side.detect_concentric_side(img4, img4_roi, img4_temp, min4_loc,
                                                                                      temp4_w, temp4_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                    # 根据样品型号进行检测，样品二（小圆柱）
                    if sample == '2':
                        # 这个是端面检测
                        img0 = cv2.imread(file5)
                        # img0 = cv2.resize(img0, (int(img0.shape[1] / 2), int(img0.shape[0] / 2)),
                        #                   interpolation=cv2.INTER_CUBIC)
                        img0_copy = img0.copy()
                        img0_roi = large_cylinder_top.get_roi_large_cylinder(img0_copy)
                        top_result, countor0 = large_cylinder_top.detect_large_cylinder_result(img0_copy, img0_roi,
                                                                                               int(value_duan),
                                                                                               float(c_duan),
                                                                                               str(method_duan),
                                                                                               str(yzfg_duan),
                                                                                               float(min_duan),
                                                                                               int(block))
                        # 这个是侧面检测
                        img1_roi, img1_temp, min1_loc, temp1_w, temp1_h = cylinder_side.get_roi(img1, template_img1)
                        side1_result, countor1 = cylinder_side.detect_concentric_side(img1, img1_roi, img1_temp,
                                                                                      min1_loc,
                                                                                      temp1_w, temp1_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img2_roi, img2_temp, min2_loc, temp2_w, temp2_h = cylinder_side.get_roi(img2, template_img2)
                        side2_result, countor2 = cylinder_side.detect_concentric_side(img2, img2_roi, img2_temp,
                                                                                      min2_loc,
                                                                                      temp2_w, temp2_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img3_roi, img3_temp, min3_loc, temp3_w, temp3_h = cylinder_side.get_roi(img3, template_img3)
                        side3_result, countor3 = cylinder_side.detect_concentric_side(img3, img3_roi, img3_temp,
                                                                                      min3_loc,
                                                                                      temp3_w, temp3_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img4_roi, img4_temp, min4_loc, temp4_w, temp4_h = cylinder_side.get_roi(img4, template_img4)
                        side4_result, countor4 = cylinder_side.detect_concentric_side(img4, img4_roi, img4_temp,
                                                                                      min4_loc,
                                                                                      temp4_w, temp4_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                    # 根据样品型号进行检测，样品三（同心圆圆柱）
                    if sample == '3':
                        # 这是端面检测
                        img0 = cv2.imread(file5)
                        # img0 = cv2.resize(img0, (int(img0.shape[1] / 2), int(img0.shape[0] / 2)),
                        #                   interpolation=cv2.INTER_CUBIC)
                        print(img0.shape)
                        dst1, dst2 = concentric_cylinder_top.get_roi_concentric(img0)
                        cv2.imshow('', dst1)
                        cv2.waitKey()
                        top_result, countor0 = concentric_cylinder_top.detect_concentric_result(img0, dst1, dst2, int(value_duan), float(c_duan), str(method_duan),str(yzfg_duan),float(min_duan), int(block))
                        # 这次侧面检测
                        img1_roi, img1_temp, min1_loc, temp1_w, temp1_h = cylinder_side.get_roi(img1, template_img1)
                        side1_result, countor1 = cylinder_side.detect_concentric_side(img1, img1_roi, img1_temp, min1_loc,
                                                                                      temp1_w, temp1_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img2_roi, img2_temp, min2_loc, temp2_w, temp2_h = cylinder_side.get_roi(img2, template_img2)
                        side2_result, countor2 = cylinder_side.detect_concentric_side(img2, img2_roi, img2_temp, min2_loc,
                                                                                      temp2_w, temp2_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img3_roi, img3_temp, min3_loc, temp3_w, temp3_h = cylinder_side.get_roi(img3, template_img3)
                        side3_result, countor3 = cylinder_side.detect_concentric_side(img3, img3_roi, img3_temp, min3_loc,
                                                                                      temp3_w, temp3_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img4_roi, img4_temp, min4_loc, temp4_w, temp4_h = cylinder_side.get_roi(img4, template_img4)
                        side4_result, countor4 = cylinder_side.detect_concentric_side(img4, img4_roi, img4_temp, min4_loc,
                                                                                      temp4_w, temp4_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                    # 根据样品型号进行检测，样品四（穹顶圆柱零件）
                    if sample == '4':
                        # 这是端面检测
                        img0 = cv2.imread(file5)
                        img0 = cv2.resize(img0, (int(img0.shape[1] / 2), int(img0.shape[0] / 2)),
                                          interpolation=cv2.INTER_CUBIC)
                        temp_lid = cv2.imread('./paraments/lid_cylinder_template.jpg')
                        temp_lid = cv2.resize(temp_lid, (int(temp_lid.shape[1] / 2), int(temp_lid.shape[0] / 2)),
                                              interpolation=cv2.INTER_CUBIC)
                        dst = lid_cylinder_top.trans2binary(img0)
                        img0_circle0, img0_circle1 = lid_cylinder_top.get_roi_lid(img0, dst, temp_lid)
                        top_result, countor0 = lid_cylinder_top.detect_lid_result(img0, img0_circle0, img0_circle1,
                                                                                  int(value_duan), int(c_duan),
                                                                                  str(method_duan), str(yzfg_duan),
                                                                                  float(min_duan), int(block))
                        # 接下来是侧面检测
                        img1_roi, img1_temp, min1_loc, temp1_w, temp1_h = cylinder_side.get_roi(img1, template_img1)
                        side1_result, countor1 = cylinder_side.detect_concentric_side(img1, img1_roi, img1_temp, min1_loc,
                                                                                      temp1_w, temp1_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img2_roi, img2_temp, min2_loc, temp2_w, temp2_h = cylinder_side.get_roi(img2, template_img2)
                        side2_result, countor2 = cylinder_side.detect_concentric_side(img2, img2_roi, img2_temp, min2_loc,
                                                                                      temp2_w, temp2_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img3_roi, img3_temp, min3_loc, temp3_w, temp3_h = cylinder_side.get_roi(img3, template_img3)
                        side3_result, countor3 = cylinder_side.detect_concentric_side(img3, img3_roi, img3_temp, min3_loc,
                                                                                      temp3_w, temp3_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))
                        img4_roi, img4_temp, min4_loc, temp4_w, temp4_h = cylinder_side.get_roi(img4, template_img4)
                        side4_result, countor4 = cylinder_side.detect_concentric_side(img4, img4_roi, img4_temp, min4_loc,
                                                                                      temp4_w, temp4_h, str(method_ce),
                                                                                      str(yzfg_ce), int(value_ce),
                                                                                      float(c_ce),
                                                                                      float(min_ce), int(block))

                    img1, img2, img3, img4, img5 = side1_result, side2_result, side3_result, side4_result, top_result
                    print(333333333333333333333333333333333333333333333333333333333333333)
                    # time.sleep(0.5)
                    # os.remove(file1)
                    # os.remove(file2)
                    # os.remove(file4)
                    # os.remove(file3)
                    # os.remove(file5)
                    frame1 = cv2.resize(img1, (381, 301))
                    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
                    h1, w1, c1 = frame1.shape
                    frame1 = QImage(frame1, w1, h1, 3 * w1, QImage.Format_RGB888)  # 处理图片虚影问题**
                    pix1 = QPixmap.fromImage(frame1)
                    self.item = QGraphicsPixmapItem(pix1)  # 创建像素图元
                    self.scene = QGraphicsScene()  # 创建场景
                    self.scene.addItem(self.item)
                    self.scene.clearSelection()
                    self.item.setSelected(True)
                    self.graphicsView.setScene(self.scene)
                    self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(frame1)))
                    # os.remove(file1)

                    frame2 = cv2.resize(img2, (381, 301))
                    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                    h2, w2, c2 = frame2.shape
                    frame2 = QImage(frame2, w2, h2, 3 * w2, QImage.Format_RGB888)  # 处理图片虚影问题**
                    pix2 = QPixmap.fromImage(frame2)
                    self.item = QGraphicsPixmapItem(pix2)  # 创建像素图元
                    self.scene = QGraphicsScene()  # 创建场景
                    self.scene.addItem(self.item)
                    self.scene.clearSelection()
                    self.item.setSelected(True)
                    self.graphicsView_2.setScene(self.scene)
                    self.graphicsView_2.fitInView(QGraphicsPixmapItem(QPixmap(frame2)))
                    # os.remove(file2)

                    frame3 = cv2.resize(img3, (381, 301))
                    frame3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGB)
                    h3, w3, c3 = frame3.shape
                    frame3 = QImage(frame3, w3, h3, 3 * w3, QImage.Format_RGB888)  # 处理图片虚影问题**
                    pix3 = QPixmap.fromImage(frame3)
                    self.item = QGraphicsPixmapItem(pix3)  # 创建像素图元
                    self.scene = QGraphicsScene()  # 创建场景
                    self.scene.addItem(self.item)
                    self.scene.clearSelection()
                    self.item.setSelected(True)
                    self.graphicsView_3.setScene(self.scene)
                    self.graphicsView_3.fitInView(QGraphicsPixmapItem(QPixmap(frame3)))
                    # os.remove(file3)

                    frame4 = cv2.resize(img4, (381, 301))
                    frame4 = cv2.cvtColor(frame4, cv2.COLOR_BGR2RGB)
                    h4, w4, c4 = frame4.shape
                    frame4 = QImage(frame4, w4, h4, 3 * w4, QImage.Format_RGB888)  # 处理图片虚影问题**
                    pix4 = QPixmap.fromImage(frame4)
                    self.item = QGraphicsPixmapItem(pix4)  # 创建像素图元
                    self.scene = QGraphicsScene()  # 创建场景
                    self.scene.addItem(self.item)
                    self.scene.clearSelection()
                    self.item.setSelected(True)
                    self.graphicsView_4.setScene(self.scene)
                    self.graphicsView_4.fitInView(QGraphicsPixmapItem(QPixmap(frame4)))
                    # os.remove(file4)

                    frame5 = cv2.resize(img5, (431, 323))
                    frame5 = cv2.cvtColor(frame5, cv2.COLOR_BGR2RGB)
                    h5, w5, c5 = frame5.shape
                    frame5 = QImage(frame5, w5, h5, 3 * w5, QImage.Format_RGB888)  # 处理图片虚影问题**
                    pix5 = QPixmap.fromImage(frame5)
                    self.item = QGraphicsPixmapItem(pix5)  # 创建像素图元
                    self.scene = QGraphicsScene()  # 创建场景
                    self.scene.addItem(self.item)
                    self.scene.clearSelection()
                    self.item.setSelected(True)
                    self.graphicsView_5.setScene(self.scene)
                    self.graphicsView_5.fitInView(QGraphicsPixmapItem(QPixmap(frame5)))
                    # os.remove(file5)
                    print(4444444444444444444444444444444444444444444444444444444444444444444444)

                    # time.sleep(0.5)
                    # os.remove(file1)
                    # os.remove(file2)
                    # os.remove(file4)
                    # os.remove(file3)
                    # os.remove(file5)

                    duan_contours, ce_contours1, ce_contours2, ce_contours3, ce_contours4 = countor0, len(countor1), len(countor2), len(countor3), len(countor4)
                    # duan_contours, ce_contours1, ce_contours2, ce_contours3, ce_contours4 = [], 0, 0, 0, 0

                    time2 = time.time()
                    timeArray2 = time.localtime(time2)
                    otherStyleTime2 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray2)
                    self.textBrowser.append(otherStyleTime2 + '：检测完成！耗时' + str(time2 - time1) + 's')
                    self.textBrowser_7.setText(str(round((time2 - time1), 4)))
                    print(otherStyleTime2 + '：检测完成！耗时' + str(time2 - time1) + 's')


                    with open('./paraments/communication.json', 'r', encoding='utf-8') as json_file1:
                        data1 = json.load(json_file1)
                    ip = data1['ip']
                    port = data1['port']
                    value = data1['value']
                    read_model = data1['read_model']
                    write_model = data1['write_model']
                    json_file1.close()
                    print(duan_contours, ce_contours1, ce_contours2, ce_contours3, ce_contours4)

                    if duan_contours > 0 or ce_contours1 > 0 or ce_contours2 > 0 or ce_contours3 > 0 or ce_contours4 >0:
                        unqualified = unqualified + 1
                        self.textBrowser_4.setText(str(unqualified))
                        # t_yan = str(2-time2 + time1)
                        # time.sleep(float(t_yan))
                        self.th = IP2PLC(ip_adress=str(ip), port_adress=int(port), value=int(value), num=int(total_num))
                        self.th.stateSignal.connect(self.show_qibeng)
                        self.th.start()
                        time3 = time.time()
                        timeArray3 = time.localtime(time3)
                        otherStyleTime3 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray3)
                        self.textBrowser.append(otherStyleTime3 + '：开始检测到信号传递完成共耗时：' + str(time3 - time1) + 's')
                        if duan_contours > 0:
                            unqualified_duan = unqualified_duan + 1
                            self.textBrowser_6.setText(str(unqualified_duan))
                        else:
                            self.textBrowser_6.setText(str(unqualified_duan))
                        if ce_contours1 > 0 or ce_contours2 > 0 or ce_contours3 > 0 or ce_contours4 > 0:
                            unqualified_ce = unqualified_ce + 1
                            self.textBrowser_8.setText(str(unqualified_ce))
                        else:
                            self.textBrowser_8.setText(str(unqualified_ce))
                    else:
                        unqualified = unqualified + 0
                        self.th = IP2PLC(ip_adress=str(ip), port_adress=int(port), value=int(2), num=int(total_num))
                        self.th.stateSignal.connect(self.show_qibeng)
                        self.th.start()
                    good_rate = (total_num - unqualified) / total_num
                    self.textBrowser_5.setText(str(good_rate))
                else:
                    time_stop = time.time()
                    timeArray_stop = time.localtime(time_stop)
                    otherStyleTime_stop = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_stop)
                    self.textBrowser.append(otherStyleTime_stop + '：系统已暂停，请重新启动系统再开始检测。')
                    # QMessageBox.critical(self, '错误', '已暂停系统，请点击启动系统按钮再检测', QMessageBox.Yes)
        if msg == 2:
            pix = QPixmap('./gui/red_circle_32.png')
            pix1 = QPixmap('./gui/green_circle_32.png')
            self.label_7.setPixmap(pix)
            self.label_7.setScaledContents(True)
            self.label_8.setPixmap(pix1)
            self.label_8.setScaledContents(True)
            self.label_9.setPixmap(pix1)
            self.label_9.setScaledContents(True)
            self.label_10.setPixmap(pix1)
            self.label_10.setScaledContents(True)
            self.label_11.setPixmap(pix1)
            self.label_11.setScaledContents(True)
            self.show()
            time_stop = time.time()
            timeArray_stop = time.localtime(time_stop)
            otherStyleTime_stop = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_stop)
            self.textBrowser.append(otherStyleTime_stop + '：侧方相机1有问题，请检查好再开始检测。')
        if msg == 3:
            pix = QPixmap('./gui/red_circle_32.png')
            pix1 = QPixmap('./gui/green_circle_32.png')
            self.label_7.setPixmap(pix1)
            self.label_7.setScaledContents(True)
            self.label_11.setPixmap(pix)
            self.label_11.setScaledContents(True)
            self.label_8.setPixmap(pix1)
            self.label_8.setScaledContents(True)
            self.label_9.setPixmap(pix1)
            self.label_9.setScaledContents(True)
            self.label_10.setPixmap(pix1)
            self.label_10.setScaledContents(True)
            self.show()
            time_stop = time.time()
            timeArray_stop = time.localtime(time_stop)
            otherStyleTime_stop = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_stop)
            self.textBrowser.append(otherStyleTime_stop + '：侧方相机2有问题，请检查好再开始检测。')
        if msg == 4:
            pix = QPixmap('./gui/red_circle_32.png')
            pix1 = QPixmap('./gui/green_circle_32.png')
            self.label_7.setPixmap(pix1)
            self.label_7.setScaledContents(True)
            self.label_8.setPixmap(pix1)
            self.label_8.setScaledContents(True)
            self.label_9.setPixmap(pix1)
            self.label_9.setScaledContents(True)
            self.label_10.setPixmap(pix)
            self.label_10.setScaledContents(True)
            self.label_11.setPixmap(pix1)
            self.label_11.setScaledContents(True)
            self.show()
            time_stop = time.time()
            timeArray_stop = time.localtime(time_stop)
            otherStyleTime_stop = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_stop)
            self.textBrowser.append(otherStyleTime_stop + '：侧方相机3有问题，请检查好再开始检测。')
        if msg == 5:
            pix = QPixmap('./gui/red_circle_32.png')
            pix1 = QPixmap('./gui/green_circle_32.png')
            self.label_7.setPixmap(pix1)
            self.label_7.setScaledContents(True)
            self.label_8.setPixmap(pix1)
            self.label_8.setScaledContents(True)
            self.label_9.setPixmap(pix)
            self.label_9.setScaledContents(True)
            self.label_10.setPixmap(pix1)
            self.label_10.setScaledContents(True)
            self.label_11.setPixmap(pix1)
            self.label_11.setScaledContents(True)
            self.show()
            time_stop = time.time()
            timeArray_stop = time.localtime(time_stop)
            otherStyleTime_stop = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_stop)
            self.textBrowser.append(otherStyleTime_stop + '：侧方相机4有问题，请检查好再开始检测。')
        if msg == 6:
            pix = QPixmap('./gui/red_circle_32.png')
            pix1 = QPixmap('./gui/green_circle_32.png')
            self.label_7.setPixmap(pix1)
            self.label_7.setScaledContents(True)
            self.label_9.setPixmap(pix1)
            self.label_9.setScaledContents(True)
            self.label_10.setPixmap(pix1)
            self.label_10.setScaledContents(True)
            self.label_11.setPixmap(pix1)
            self.label_11.setScaledContents(True)
            self.label_8.setPixmap(pix)
            self.label_8.setScaledContents(True)
            self.show()
            time_stop = time.time()
            timeArray_stop = time.localtime(time_stop)
            otherStyleTime_stop = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_stop)
            self.textBrowser.append(otherStyleTime_stop + '：上方相机有问题，请检查好再开始检测。')
        if msg == 7:
            pix = QPixmap('./gui/red_circle_32.png')
            self.label_7.setPixmap(pix)
            self.label_7.setScaledContents(True)
            self.label_8.setPixmap(pix)
            self.label_8.setScaledContents(True)
            self.label_9.setPixmap(pix)
            self.label_9.setScaledContents(True)
            self.label_10.setPixmap(pix)
            self.label_10.setScaledContents(True)
            self.label_11.setPixmap(pix)
            self.label_11.setScaledContents(True)
            self.show()
            time_state = time.time()
            timeArray_state = time.localtime(time_state)
            otherStyleTime_state = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_state)
            self.textBrowser.append(otherStyleTime_state + '：存在两个及以上的相机有问题，请检查！！！')

        # else:
        #     print('收到信号0，不执行任何操作')

    def show_qibeng(self, message):
        if message == 1:
            pix = QPixmap('./gui/green_circle_32.png')
            self.label_4.setPixmap(pix)
            self.label_4.setScaledContents(True)
            self.show()
        else:
            pix = QPixmap('./gui/red_circle_32.png')
            self.label_5.setPixmap(pix)
            self.label_5.setScaledContents(True)
            self.show()

    def set_pic_path(self):
        w2 = Set_Pic_Path()
        w2.show()
        w2.exec_()
        time_set_pic_path = time.time()
        timeArray_set_pic_path = time.localtime(time_set_pic_path)
        otherStyleTime_set_pic_path = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_set_pic_path)
        self.textBrowser.append(otherStyleTime_set_pic_path + '：已重新设置好相机图片保存路径。')

    def get_template(self):
        w1 = Set_Template()
        w1.show()
        w1.exec_()
        time_get_template = time.time()
        timeArray_get_template = time.localtime(time_get_template)
        otherStyleTime_get_template = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_get_template)
        self.textBrowser.append(otherStyleTime_get_template + '：已重新选择好模板图片了。')

    def set_save_path(self):
        global save_path
        save_path = QtWidgets.QFileDialog.getExistingDirectory(None, '选取文件夹', 'C:/')
        time_set_save_path = time.time()
        timeArray_set_save_path = time.localtime(time_set_save_path)
        otherStyleTime_set_save_path = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_set_save_path)
        self.textBrowser.append(otherStyleTime_set_save_path + '：已设置好保存路径为:' + save_path)
        print(save_path)
        return save_path

    def set_delay_time(self):
        self.th = Delay_Time()
        self.th.start()

    def set_paraments(self):
        self.th = Set_Parament()
        self.th.start()
        from detect_settings110702 import value_duan, value_ce, min_duan, min_ce, c_duan, c_ce, block, method_ce, method_duan, yzfg_ce, yzfg_duan, pic_directory, temp_directory, sample, detect_model
        directory, template = pic_directory, temp_directory
        return value_duan, value_ce, min_duan, min_ce, c_duan, c_ce, block, method_ce, method_duan, yzfg_ce, yzfg_duan, pic_directory, temp_directory, sample, detect_model

    def about(self):
        QMessageBox.information(self, '关于', '化妆品瓶身表面缺陷检测系统-Version 1.2\ndesigned by Robot Group', QMessageBox.Yes)

    def help(self):
        path_help = os.getcwd() + '/help/使用手册.pdf'
        webbrowser.open(path_help)


class Set_Parament(QThread):

    def __init__(self, parent=None):
        super(Set_Parament, self).__init__(parent)

    def run(self) -> None:
        #os.system('detect_settings110702.exe')
        os.system('python detect_settings110702.py')


class Show_Tools(QThread):

    def __init__(self, parent=None):
        super(Show_Tools, self).__init__(parent)

    def run(self) -> None:
        #os.system('tool_new1110.exe')
        os.system('python tool_new1110.py')


class Ip_Plc(QThread):
    def __init__(self, parent=None):
        super(Ip_Plc, self).__init__(parent)

    def run(self) -> None:
        #os.system('communication1110.exe')
        os.system('python communication1110.py')


class Delay_Time(QThread):
    def __init__(self, parent=None):
        super(Delay_Time, self).__init__(parent)

    def run(self) -> None:
        #os.system('delay_time.exe')
        os.system('python delay_time.py')


class Side_Methodthreshold(QThread):
    def __init__(self, parent=None):
        super(Side_Methodthreshold, self).__init__(parent)

    def run(self) -> None:
        #os.system('set_methodAndthreshold_ce.exe')
        os.system('python set_methodAndthreshold_ce.py')


class Valueandmethod_duan(QThread):
    def __init__(self, parent=None):
        super(Valueandmethod_duan, self).__init__(parent)

    def run(self) -> None:
        #os.system('set_methodAndthreshold_duan.exe')
        os.system('python set_methodAndthreshold_duan.py')


class IP2PLC(QThread):

    stateSignal = pyqtSignal(int)

    def __init__(self, ip_adress, port_adress, value, num, parent=None):
        super(IP2PLC, self).__init__(parent)
        self.ip_adress = ip_adress
        self.port_adress = port_adress
        self.value = value
        self.num = num

    def run(self) -> None:
        master = mt.TcpMaster(self.ip_adress, self.port_adress)
        master.set_timeout(5)
        print("这是plc链接地方")
        # 写入单个寄存器
        # master.execute(slave=1, function_code=md.WRITE_SINGLE_REGISTER, starting_address=0, output_value=self.value)
        if self.num % 5 == 0 and self.num >= 1:
            master.execute(slave=1, function_code=md.WRITE_SINGLE_REGISTER, starting_address=4, output_value=self.value)
            print("已经连接上，开始写入")
            data = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=4, quantity_of_x=1)
            if int(data[0]) == self.value:
                self.stateSignal.emit(1)
            else:
                self.stateSignal.emit(0)
        if self.num % 5 == 1 and self.num >= 1:
            master.execute(slave=1, function_code=md.WRITE_SINGLE_REGISTER, starting_address=0, output_value=self.value)
            print("已经连接上，开始写入")
            data = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=0, quantity_of_x=1)
            if int(data[0]) == self.value:
                self.stateSignal.emit(1)
            else:
                self.stateSignal.emit(0)
        if self.num % 5 == 2 and self.num >= 1:
            master.execute(slave=1, function_code=md.WRITE_SINGLE_REGISTER, starting_address=1, output_value=self.value)
            print("已经连接上，开始写入")
            data = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=1, quantity_of_x=1)
            if int(data[0]) == self.value:
                self.stateSignal.emit(1)
            else:
                self.stateSignal.emit(0)
        if self.num % 5 == 3 and self.num >= 1:
            master.execute(slave=1, function_code=md.WRITE_SINGLE_REGISTER, starting_address=2, output_value=self.value)
            print("已经连接上，开始写入")
            data = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=2, quantity_of_x=1)
            if int(data[0]) == self.value:
                self.stateSignal.emit(1)
            else:
                self.stateSignal.emit(0)
        if self.num % 5 == 4 and self.num >= 1:
            master.execute(slave=1, function_code=md.WRITE_SINGLE_REGISTER, starting_address=3, output_value=self.value)
            print("已经连接上，开始写入")
            data = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=3, quantity_of_x=1)
            if int(data[0]) == self.value:
                self.stateSignal.emit(1)
            else:
                self.stateSignal.emit(0)
        # time.sleep(0.5)
        # master.execute(slave=2, function_code=md.WRITE_SINGLE_REGISTER, starting_address=0, output_value=0)


class Trigger(QThread):

    finishSignal = pyqtSignal(int)

    def __init__(self, ip_adress, port_adress, parent=None):
        super(Trigger, self).__init__(parent)
        self.ip_adress = ip_adress
        self.port_adress = port_adress

    def run(self) -> None:
        global stopflag
        with open('./paraments/paraments.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        directory = data['directory']
        delay_time = data['delay_time']
        json_file.close()
        if stopflag == 0:
            while True:
                d1, d2, d3, d4, d5 = os.listdir(directory)[0], os.listdir(directory)[1], os.listdir(directory)[2], \
                                     os.listdir(directory)[3], os.listdir(directory)[4]
                target_dir1 = directory + '/' + str(d1)
                target_dir2 = directory + '/' + str(d2)
                target_dir3 = directory + '/' + str(d3)
                target_dir4 = directory + '/' + str(d4)
                target_dir5 = directory + '/' + str(d5)
                l1, l2, l3, l4, l5 = len(os.listdir(target_dir1)), len(os.listdir(target_dir2)), len(
                    os.listdir(target_dir3)), len(os.listdir(target_dir4)), len(os.listdir(target_dir5))
                flag0 = [l1 != 0, l2 != 0, l3 != 0, l4 != 0, l5 != 0]
                if False not in flag0:
                    file1 = glob(directory + '/' + str(d1) + '/*jpg')[0]
                    file2 = glob(directory + '/' + str(d2) + '/*jpg')[0]
                    file3 = glob(directory + '/' + str(d3) + '/*jpg')[0]
                    file4 = glob(directory + '/' + str(d4) + '/*jpg')[0]
                    file5 = glob(directory + '/' + str(d5) + '/*jpg')[0]
                    flag = [os.path.exists(file1), os.path.exists(file2), os.path.exists(file3), os.path.exists(file4),
                            os.path.exists(file5)]

                    if False not in flag:
                        self.finishSignal.emit(1)
                    if flag[0] == False and flag[1] == True and flag[2] == True and flag[3] == True and flag[4] == True:
                        self.finishSignal.emit(2)
                    if flag[0] == True and flag[1] == False and flag[2] == True and flag[3] == True and flag[4] == True:
                        self.finishSignal.emit(3)
                    if flag[0] == True and flag[1] == True and flag[2] == False and flag[3] == True and flag[4] == True:
                        self.finishSignal.emit(4)
                    if flag[0] == True and flag[1] == True and flag[2] == True and flag[3] == False and flag[4] == True:
                        self.finishSignal.emit(5)
                    if flag[0] == True and flag[1] == True and flag[2] == True and flag[3] == True and flag[4] == False:
                        self.finishSignal.emit(6)
                    if flag.count(False) >= 2:
                        self.finishSignal.emit(7)
                    time.sleep(0.8)
                    if stopflag == 1:
                        break
                else:
                    # flag = [l1 != 0, l2 != 0, l3 != 0, l4 != 0, l5 != 0]
                    # if flag[0] == False and flag[1] == True and flag[2] == True and flag[3] == True and flag[4] == True:
                    #     self.finishSignal.emit(2)
                    # if flag[0] == True and flag[1] == False and flag[2] == True and flag[3] == True and flag[4] == True:
                    #     self.finishSignal.emit(3)
                    # if flag[0] == True and flag[1] == True and flag[2] == False and flag[3] == True and flag[4] == True:
                    #     self.finishSignal.emit(4)
                    # if flag[0] == True and flag[1] == True and flag[2] == True and flag[3] == False and flag[4] == True:
                    #     self.finishSignal.emit(5)
                    # if flag[0] == True and flag[1] == True and flag[2] == True and flag[3] == True and flag[4] == False:
                    #     self.finishSignal.emit(6)
                    # if flag.count(False) >= 2:
                    #     self.finishSignal.emit(7)
                    pass
        else:
            pass


class Set_Pic_Path(QDialog):
    def __init__(self, parent=None):
        super(Set_Pic_Path, self).__init__(parent)

        self.label = QLabel(self)
        self.label.setText('图片路径选择')
        self.label.move(230, 30)
        self.textedit = QTextBrowser(self)
        self.textedit.move(130, 22)
        self.btn = QPushButton('浏览')
        self.btn.move(0, 20)

        vb = QVBoxLayout()
        vb.addWidget(self.label)
        vb.addWidget(self.textedit)
        vb.addWidget(self.btn)
        self.setLayout(vb)
        self.setWindowTitle('修改图片路径')

        self.btn.clicked.connect(self.set_picpath)

    def set_picpath(self):
        global directory
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, '选取文件夹', 'C:/')
        self.textedit.setText(directory)
        with open('./paraments/paraments.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        tmp = data['directory']
        data['directory'] = str(directory)
        with open('./paraments/paraments.json', "w") as jsonFile:
            json.dump(data, jsonFile, ensure_ascii=False)
        return directory


class Set_Template(QDialog):
    def __init__(self, parent=None):
        super(Set_Template, self).__init__(parent)

        self.label = QLabel(self)
        self.label.setText('模板文件选择')
        self.label.move(230, 30)
        self.textedit = QTextBrowser(self)
        self.textedit.move(130, 22)
        self.btn = QPushButton('浏览')
        self.btn.move(0, 20)

        vb = QVBoxLayout()
        vb.addWidget(self.label)
        vb.addWidget(self.textedit)
        vb.addWidget(self.btn)
        self.setLayout(vb)
        self.setWindowTitle('更换模板图片')

        self.btn.clicked.connect(self.set_template)

    def set_template(self):
        global template
        template = QtWidgets.QFileDialog.getExistingDirectory(None, '选取文件夹', os.getcwd())
        template = template[0]
        self.textedit.setText(template)
        with open('./paraments/paraments.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        tmp = data['template']
        data['template'] = str(template)
        with open('./paraments/paraments.json', "w") as jsonFile:
            json.dump(data, jsonFile, ensure_ascii=False)
        return template

