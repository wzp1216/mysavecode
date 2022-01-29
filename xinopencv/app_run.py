# -*- coding: utf-8 -*-
"""
@author:wzp1216@163.com 
@file: mainwindow.py.py
ver-0.1
"""

import sys
import time
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QProgressBar
from PyQt5.QtCore import QThread,QBasicTimer,pyqtSignal
from PyQt5.Qt import Qt, QRect
from time import sleep

from mainwin import my_main_win
# 主页界面类 -----------




class LoadWin(QWidget):  # 启动画面类 -----------
    def __init__(self):
        super(LoadWin, self).__init__()
        self.ui_init()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.timer = QBasicTimer()  # 定时器对象
        self.main_win = my_main_win()  # 进度结束后要显示的主页
        self.step = 0  # 进度值
        self.proess_run()

    def ui_init(self):
        self.label_1=QLabel("test.................")
        self.progressBar=QProgressBar()
        lay=QVBoxLayout()
        lay.addChildWidget(self.label_1)
        lay.addChildWidget(self.progressBar)
        self.setLayout(lay)


    def proess_run(self):  # 启动进度线程
        self.cal = LoadThread()  # 线程对象
        self.cal.part_signal.connect(self.process_set_part)
        self.cal.data_signal.connect(self.show_main_win)
        self.cal.start()  # 调用线程run

    def process_set_part(self, num):
        self.step = num  # 进度从num开始
        self.progressBar.setValue(self.step)
        if num == 0:
            self.timer.start(20, self)  # 启动QBasicTimer, 每20毫秒调用一次回调函数
            self.label_1.setText("正在加载系统资源...")
        if num == 1:
            self.timer.stop()  # 重启，调整进度条增值速度
            self.timer.start(10, self)
            self.label_1.setText("加载完成，欢迎使用本系统...")

    def timerEvent(self, *args, **kwargs):  # QBasicTimer的事件回调函数
        self.progressBar.setValue(self.step)  # 设置进度条的值
        if self.step < 100:
            self.step += 1

    def show_main_win(self):
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
    app = QApplication(sys.argv)
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

