# -*- coding: utf-8 -*-
import sys
from  PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from  PyQt5.QtWidgets import QVBoxLayout,QFormLayout
from formlay import qlineedit,formlay



class center(QWidget):
    def __init__(self):
        super(center,self).__init__()
        self.init()
    def init(self):
        layout=QVBoxLayout()
        self.t1=qlineedit()
        layout.addWidget(self.t1)
        self.t2=formlay()
        layout.addWidget(self.t2)
        self.setLayout(layout)

class mainwin(QMainWindow):
    def __init__(self,parent=None):
        super(mainwin,self).__init__(parent)
        self.init()
    def init(self):
        self.mycenter=center()
        self.setCentralWidget(self.mycenter)
        self.show()



if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=mainwin()
    mywin.show()
    sys.exit(app.exec_())