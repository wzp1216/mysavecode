#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import  Qt,QRect

class Drawing(QDialog):
    def __init__(self,parent=None):
        super(Drawing,self).__init__(parent)
        self.setWindowTitle("draw in window")
        self.resize(800,600)
        self.text='study PYQT'
    def paintEvent(self,event):
        painter=QPainter(self)
        #painter.begin(self)
        self.drawPoints(painter)
        #painter.end()
    def drawPoints(self,qp):
            qp.setPen(Qt.red)
            size=self.size()
            print("this windows size is ",size)
            for i in range(1000):
                x=200*(-1+2.0*i/1000)+size.width()/2.0
                y=-50*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0
                qp.drawPoint(int(x),int(y))

##     drawText(self,event,qp):
            qp.setFont(QFont('SimSun',20))
            rect1=QRect(20,30,60,90)
            qp.drawText(20,30,self.text)
            qp.drawRect(QRect(10,20,80,100))
            qp.drawRect(QRect(20,30,90,110))
            qp.drawRect(QRect(30,40,90,120))

            pen=QPen(Qt.black,2,Qt.SolidLine)
            qp.setPen(pen)
            qp.drawLine(20,40,280,40)

            pen.setStyle(Qt.DashDotLine)
            qp.setPen(pen)
            qp.drawLine(60,80,280,80)
            
            brush=QBrush(Qt.SolidPattern)
            qp.setBrush(brush)
            qp.drawRect(100,120,130,160)

            brush=QBrush(Qt.Dense3Pattern)
            qp.setBrush(brush)
            qp.drawRect(140,160,180,160)

            brush=QBrush(Qt.VerPattern)
            qp.setBrush(brush)
            qp.drawRect(180,190,280,260)

            brush=QBrush(Qt.BDiagPattern)
            qp.setBrush(brush)
            qp.drawRect(240,260,380,360)

if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=Drawing()
    demo.show()
    sys.exit(app.exec_())

