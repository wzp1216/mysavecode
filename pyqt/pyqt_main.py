# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout
from formlay import qlineedit, formlay


class center(QWidget):
    def __init__(self):
        super(center, self).__init__()
        self.init()

    def init(self):
        layout = QVBoxLayout()
        self.t1 = qlineedit()
        layout.addWidget(self.t1)
        self.t2 = formlay()
        layout.addWidget(self.t2)
        self.setLayout(layout)


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
        self.addmenu()

    def init(self):
        self.mycenter = center()
        self.setCentralWidget(self.mycenter)
        self.show()

    def addmenu(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = mainwin()
    mywin.show()
    sys.exit(app.exec_())
