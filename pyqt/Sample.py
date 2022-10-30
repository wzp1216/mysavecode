# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget

from PyQt5.QtWidgets import QPushButton,QMessageBox
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QGridLayout
from layout_sample import testwin
from draw1_sample import Drawing 
from opencv_openfile import opencv_win
from timer_sample import  time_winForm

class mainwin(QMainWindow):
    def __init__(self, parent=None):
        super(mainwin, self).__init__(parent)
        screen = QDesktopWidget().screenGeometry()
        high = screen.height()
        width = screen.width()
        self.resize(width * 5 // 6, high * 5 // 6)
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))
        self.init()

    def init(self):
        msgbut=QPushButton("show msg")
        msgbut.clicked.connect(self.qtmessage)

        layout_but=QPushButton("show layout sample")
        layout_but.clicked.connect(self.layoutsample)

        draw_bnt=QPushButton("show draw sample")
        draw_bnt.clicked.connect(self.draw_sample)
        
        opencv_openfile_btn=QPushButton("opencv open a file")
        opencv_openfile_btn.clicked.connect(self.opencv_openfile)

        time_btn=QPushButton("time sample")
        time_btn.clicked.connect(self.time_sample)

        layout=QGridLayout()
        layout.addWidget(msgbut,0,0)
        layout.addWidget(layout_but,0,1)
        layout.addWidget(draw_bnt,0,2)
        layout.addWidget(opencv_openfile_btn,1,0)
        layout.addWidget(time_btn,1,1)

        main_frame=QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)
    def time_sample(self):
        self.time_sample_win=time_winForm()
        self.time_sample_win.exec()
    def opencv_openfile(self):
        self.openfile_win=opencv_win()
        self.openfile_win.exec()

    def draw_sample(self):
        self.draw1_win=Drawing()
        self.draw1_win.exec()

        
    def layoutsample(self):
        self.layout_win=testwin()
        self.layout_win.exec()

    def qtmessage(self):
        QMessageBox.information(self,"msg","I will tell you a msg",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = mainwin()
    mywin.show()
    sys.exit(app.exec_())
