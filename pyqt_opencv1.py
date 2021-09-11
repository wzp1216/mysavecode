# -*- coding: utf-8 -*-
import sys
from  PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QLabel
from  PyQt5.QtWidgets import QVBoxLayout,QFormLayout
import halcon as ha


if __name__=='__main__':
    img=ha.read_image('pcb.png')

class center(QWidget):
    def __init__(self):
        super(center,self).__init__()
        self.init()
    def init(self):

        self.img=ha.read_image('pcb.png')
        print(type(self.img))
        region = ha.threshold(img, 0, 122)
        num = ha.count_obj(ha.connection(region))
        print(f'Number of regions: {num}')

        layout=QVBoxLayout()
        self.l1=QLabel("this is the open image:")
        layout.addWidget(self.l1)
        self.l2=QLabel(str(num))
        layout.addWidget(self.l2)
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