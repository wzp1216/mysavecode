import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QHBoxLayout,QGraphicsScene,QGraphicsView,QVBoxLayout

class sencedemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,700)
        self.l1=QLabel("aaaaaaa")
        self.hbox=QVBoxLayout()
        #创建场景
        self.scene=QGraphicsScene()
        self.scene.setSceneRect(0,0,300,300)
        self.scene.addText('PYQT5',font=QFont('Roman times',80,QFont.Bold))
        self.view=QGraphicsView()
        self.view.resize(300,300)
        self.view.setScene(self.scene)
        self.hbox.addWidget(self.view)
        self.hbox.addWidget(self.l1)
        #self.hbox.setContentsMargins(0,0,0,0)
        self.setLayout(self.hbox)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=sencedemo()
    win.show()
    sys.exit(app.exec_())



