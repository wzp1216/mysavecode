import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Draw_sin(QDialog):
    def __init__(self,parent=None):
        super(Draw_sin,self).__init__(parent)
        self.resize(300,200)
        self.setWindowTitle("draw sin")
    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
    def drawPoints(self,qp):
        qp.setPen(Qt.red)
        size=self.size()
        for i in range(1000):
            x=100*(-1+2.0*i/1000)+size.width()/2.0
            y=-50*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0
            qp.drawPoint(int(x),int(y))


if __name__=='__main__':
    app=QApplication(sys.argv)
    w=Draw_sin()
    w.show()
    sys.exit(app.exec_())


