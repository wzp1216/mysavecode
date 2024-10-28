# -*- coding: utf-8 -*-
"""
@author: Tu Qiuping
@software: PyCharm
@file: mainwindow.py.py
@time: 7/18/2021 14:48 PM
"""
import sys
import time
import qdarkstyle
from PyQt5 import QtCore
from mainwindows import MainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, qApp
from PyQt5.Qt import QWidget, Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QBrush, QPixmap, QPaintEvent
# 此处firstMainWin依据自己转化的py文件名来更改

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     # app.setStyleSheet(qdarkstyle.load_stylesheet())
#     app.setWindowIcon(QIcon('./gui/Icon.png'))
#     myWin = MainWindow()
#     myWin.showMaximized()
#     sys.exit(app.exec())


from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QBasicTimer
import sys
from time import sleep
import loadwin, mainwindows


class LoadWin(QWidget, loadwin.Ui_Form):  # 启动画面类 -----------
    def __init__(self):
        super(LoadWin, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.timer = QBasicTimer()  # 定时器对象
        self.main_win = MainWin()  # 进度结束后要显示的主页
        self.step = 0  # 进度值
        self.proess_run()

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
            self.label_3.setText("正在加载系统资源...")
        if num == 1:
            self.timer.stop()  # 重启，调整进度条增值速度
            self.timer.start(10, self)
            self.label_3.setText("加载完成，欢迎使用本系统...")

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


class MainWin(mainwindows.MainWindow):  # 主页界面类 -----------
    def __init__(self):
        super(MainWin, self).__init__()
        # self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LoadWin()
    w.show()
    sys.exit(app.exec())