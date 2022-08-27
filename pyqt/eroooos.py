import random
import sys

from PyQt5.QtCore import Qt,QBasicTimer,pyqtSignal
from PyQt5.QtWidgets import QMainWindow,QFrame,QDesktopWidget,QApplication
from PyQt5.QtGui import QPainter,QColor




class Tetris(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tboard=Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar=self.statusbar()



class Board(QFrame):
    msg2Statusbar=pyqtSignal(str)
    BoardWidth=20
    BoardHeight=32
    Speed=300

    def __init__(self,parent):
        super().__init__(parent)
        self.initBoard()

    def initBoard():
        self.timer=QBasicTimer()
        


if __name__=="__main__":
    app=QApplication(sys.argv)

    sys.exit(app.exec_())




'''
1.创建主程序；创建主窗口；主控件；消息；状态栏；
   设计一个SIGNAL；
'''

