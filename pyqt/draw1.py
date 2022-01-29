import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtGui import QPainter,QPixmap
from PyQt5.QtCore import Qt,QPoint

class win(QWidget):
    def __init__(self,parent=None):
        super(win,self).__init__(parent)
        self.setWindowTitle('draw example')
        self.lastPoint=QPoint()
        self.endPoint=QPoint()
        self.initui()
    def initui(self):
        self.resize(600,500)
        self.l1=QLabel("draw with mouse!")
        self.pix=QPixmap(400,400)
        self.pix.fill(Qt.white)
        lay=QVBoxLayout()
        lay.addWidget(self.l1)

    def paintEvent(self,event):
        pp=QPainter(self.pix)
        pp.drawLine(self.lastPoint,self.endPoint)
        self.lastPoint=self.endPoint
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix)
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.lastPoint=event.pos()
            self.endPoint=self.lastPoint

    def mouseMoveEvent(self,event):
        if event.button() and Qt.LeftButton:
            self.endPoint=event.pos()
            self.update()

        
    def mouseReleaseEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.endPoint=event.pos()
            self.update()

        
if __name__=="__main__":
    app=QApplication(sys.argv)
    w=win()
    w.show()
    sys.exit(app.exec_())

