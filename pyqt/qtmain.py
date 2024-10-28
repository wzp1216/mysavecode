import sys
import matplotlib
#matplotlib.use("TkAgg")
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog
from PyQt5.QtWidgets import QWidget,QCheckBox
from PyQt5.QtCore import Qt


class Test1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        cb=QCheckBox('Show titel',self)
        cb.move(20,20)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QCheckBox')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex=Test1()
    sys.exit(app.exec_())


