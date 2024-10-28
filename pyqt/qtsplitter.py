import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class splitterexample(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
    def initui(self):
        hbox=QHBoxLayout(self)
        self.setWindowTitle("Qsplitter")
        self.setGeometry(300,300,300,200)
        topleft=QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        bottom=QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        splitter1=QSplitter(Qt.Horizontal)
        textedit=QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100,200])
        splitter2=QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=splitterexample()
    demo.show()
    sys.exit(app.exec_())

