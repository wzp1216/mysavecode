# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QGridLayout
from layout_sample import testwin

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

        layout=QGridLayout()
        layout.addWidget(msgbut,0,0)
        layout.addWidget(layout_but,0,1)

        main_frame=QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)
        
    def layoutsample(self):
        self.layout_win=testwin()
        self.layout_win.exec()

    def qtmessage():
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = mainwin()
    mywin.show()
    sys.exit(app.exec_())
