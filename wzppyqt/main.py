# coding=utf-8
import sys
import cv2
from PyQt5.QtGui import *
from PyQt5.Qt import *
import matplotlib.pyplot as plt

class Myapp(QMainWindow):
    def __init__(self):
        super(Myapp,self).__init__()
        self.setWindowTitle('wzp study opencv&qt')
        self.setWindowIcon(QIcon('icons/main.png'))
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)
        self.showMaximized()
        self.toolsbar=self.addToolBar('工具栏')
        self.action_left_rotate=QAction(QIcon("icons/left_roate.png"),"Left_Roate")
        self.toolsbar.addAction(self.action_left_rotate)
        self.toolsbar.setVisible(True)
        self.src_img=None;
        self.cur_img=None;

    def update_img(self):
        if self.src_img is None:
            return


if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setStyleSheet(open('setting/AMOLED.qss',encoding='utf-8').read())
    win1=Myapp()
    win1.show()
    sys.exit(app.exec_())
