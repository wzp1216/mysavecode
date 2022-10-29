#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

#QHBoxLayout  水平布局；
#QVBoxLayout  垂直布局；
#addStretsh   伸缩器
#QGridLayout  grid layout;
#QFormLayout   表单布局；
#QSplitter    可拖变布局

class mytab(QTabWidget):
    def __init__(self,parent=None):
        super(mytab,self).__init__(parent)
        self.htab=QWidget()
        self.vtab=QWidget()
        self.gtab=QWidget()
        self.splitter_tab=QWidget()
        self.setWindowTitle("layout")
        self.resize(800,600)

        self.addTab(self.htab,"tQHBoxLayou")
        self.addTab(self.vtab,"tQVBoxLayou")
        self.addTab(self.gtab,"Grid")
        self.addTab(self.splitter_tab,"splitter")
        self.htabUI()
        self.vtabUI()
        self.gridtabUI()
        self.splittertabUI()


    def htabUI(self):
        self.label1=QLabel("11111")
        self.label2=QLabel("22222")
        self.label3=QLabel("33333")
        self.label4=QLabel("LEFT：ADDSTRETCH1右侧ADDSTRETCH2，44444")
        layout=QHBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addStretch(2)
        self.htab.setLayout(layout)


    def vtabUI(self):
        self.label_tab2_1=QLabel("vvvvv")
        self.label_tab2_2=QLabel("vvvvv")
        self.label_tab2_3=QLabel("vvvvv")
        self.label_tab2_4=QLabel("vvvvv")
        layout=QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.label_tab2_1)
        layout.addWidget(self.label_tab2_2)
        layout.addWidget(self.label_tab2_3)
        layout.addWidget(self.label_tab2_4)
        layout.addStretch(1)
        self.vtab.setLayout(layout)

    def gridtabUI(self):
        self.txt0=QLabel("txt0,0")
        self.txt1=QLabel("txt0,2")
        self.txt2=QLabel("txt1,1")
        self.txt3=QLabel("txt1,2")
        self.txt4=QLabel("txt2,2")
        self.txt5=QLabel("txt3,1--3,2-------------------------8888888888888888888888888888888-")
        layout=QGridLayout()
        layout.addWidget(self.txt0,0,0)
        layout.addWidget(self.txt1,0,2)
        layout.addWidget(self.txt2,1,1)
        layout.addWidget(self.txt3,1,2)
        layout.addWidget(self.txt4,2,2)
        layout.addWidget(self.txt5,3,1,3,2)
        self.gtab.setLayout(layout)

    def splittertabUI(self):
        hlay=QHBoxLayout()
        splitter1=QSplitter(Qt.Horizontal)
        txtedit=QTextEdit()
        f1=QFrame()
        f1.setFrameShape(QFrame.StyledPanel)
        splitter1.addWidget(f1)
        splitter1.addWidget(txtedit)
        
        l2=QLabel("splitter")
        f2=QFrame()
        f2.setFrameShape(QFrame.StyledPanel)
        sp2=QSplitter(Qt.Vertical)
        sp2.addWidget(splitter1)
        sp2.addWidget(l2)
        sp2.addWidget(f2)
        hlay.addWidget(sp2)
        self.splitter_tab.setLayout(hlay)


        


#testwin
class testwin(QDialog):
    def __init__(self,parent=None):
        super(testwin,self).__init__(parent)
        self.setWindowTitle("layout window")
        self.resize(800,600)
        
        self.TabWidget=mytab()
        layout=QHBoxLayout()
        layout.addWidget(self.TabWidget)
        self.setLayout(layout)

#main
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=testwin()
    win.show()
    sys.exit(app.exec_())
