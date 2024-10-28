import sys
import cv2 as cv
import matplotlib
matplotlib.use("TkAgg")

import numpy as np
from PyQt5.QtGui import  QImage,QPixmap
from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog,QGridLayout,QLabel,QPushButton

class win(QDialog):
    def __init__(self):
        self.img=np.ndarray(())
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(400,300)
        self.btnopen=QPushButton('Open',self)
        self.btnsave=QPushButton('Save',self)
        self.btnprocess=QPushButton('Process',self)
        self.btnquit=QPushButton('Quit',self)
        self.label=QLabel()
        
        lay=QGridLayout(self)
        lay.addWidget(self.label,0,1,3,4)
        lay.addWidget(self.btnopen,4,1,1,1)
        lay.addWidget(self.btnsave,4,2,1,1)
        lay.addWidget(self.btnprocess,4,3,1,1)
        lay.addWidget(self.btnquit,4,4,1,1)

        self.btnopen.clicked.connect(self.openslot)
        self.btnsave.clicked.connect(self.saveslot)
        self.btnprocess.clicked.connect(self.processslot)
        self.btnquit.clicked.connect(self.close)

    def openslot(self):
        filename,tmp=QFileDialog.getOpenFileName(self,'open image','./','*.png *.jpg *.bmp')
        if filename=='' :return
        self.img=cv.imread(filename,-1)
        if self.img.size==1: return
        self.refreshShow()

    def saveslot(self):
        pass

    def processslot(self):
        if self.img.size==1: return
        self.img=cv.blur(self.img,(5,5))
        self.refreshShow()

    def refreshShow(self):
        if(len(self.img.shape)==3): 
            h,w,channel=self.img.shape
            bytesPerLine=3*w;
            self.qtimg=QImage(self.img.data,w,h,bytesPerLine,QImage.Format_RGB888).rgbSwapped()
            self.label.setPixmap(QPixmap.fromImage(self.qtimg))


if __name__=='__main__':
    a=QApplication(sys.argv)
    w=win()
    w.show()
    sys.exit(a.exec_())



        
        

