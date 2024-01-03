# -*- coding: utf-8 -*-
"""
@author:wzp1216@163.com 
@file: appstart.py
ver-0.1
"""

import sys
import time
import matplotlib 
matplotlib.use("TkAgg")

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QProgressBar,QDesktopWidget
from PyQt5.QtCore import QThread,QBasicTimer,pyqtSignal
from PyQt5.Qt import Qt, QRect
from time import sleep

from loadui import  Ui_load
# load界面类 -----------
from mainwin import my_main_win
# 主页界面类 -----------

class LoadWin(QWidget,Ui_load):  # 启动画面类 -----------
    def __init__(self):
        super(LoadWin, self).__init__()
        self.setupUi(self)
        screen = QDesktopWidget().screenGeometry()
        high = screen.height()
        width = screen.width()
        print(width,high)
        self.resize(width * 1 // 2, high * 1 // 2)
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.timer = QBasicTimer()  # 定时器对象
        self.step = 0  # 进度值
        self.status=0
        self.proess_run()


    def proess_run(self):  # 启动进度线程
        self.cal = LoadThread()  # 线程对象
        self.cal.part_signal.connect(self.process_set)
        self.cal.data_signal.connect(self.show_main)
        self.cal.start()  # 调用线程run

    def process_set(self):
        self.progressBar.setValue(self.step)
        if self.status== 0:
            self.timer.start(10, self)  # 启动QBasicTimer, 每20毫秒调用一次回调函数

        self.label_hit.setText("正在加载系统资源...")
            
        if self.step == 100:
            self.timer.stop()  # 重启，调整进度条增值速度
            self.label_hit.setText("加载完成，欢迎使用本系统...")
            self.status=1

    def timerEvent(self, *args, **kwargs):  # QBasicTimer的事件回调函数
        self.progressBar.setValue(self.step)  # 设置进度条的值
        if self.step < 100:
            self.step += 1

    def show_main(self):
        self.main_win = my_main_win()  # 进度结束后要显示的主页
        screen = QDesktopWidget().screenGeometry()
        h = screen.height()
        w = screen.width()
        '''
        screen=app.primaryScreen();
        s=screen.size()
        w=s.width();h=s.height()
        print(w,h)
        '''
        self.main_win.resize(w,h)
        self.main_win.move(0,0)
        self.main_win.showMaximized()
        self.close()


class LoadThread(QThread):  # 自定义计算线程类 -----------
    part_signal = pyqtSignal(int)  # 进度环节信号
    data_signal = pyqtSignal(str)  # 数据传递信号

    def __init__(self):
        super().__init__()

    def run(self):
        self.part_signal.emit(0)
        self.fun_part_one()
        self.part_signal.emit(1)
        sleep(1)  # 模拟加载耗时
        self.data_signal.emit(" ")

    def fun_part_one(self):
        sleep(3)  # 模拟计算耗时




if __name__ == '__main__':
    app= QApplication(sys.argv)
    w = LoadWin()
    w.show()
    sys.exit(app.exec_())


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     # app.setStyleSheet(qdarkstyle.load_stylesheet())
#     app.setWindowIcon(QIcon('./gui/Icon.png'))
#     myWin = MainWindow()
#     myWin.showMaximized()
#     sys.exit(app.exec())

