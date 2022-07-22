# -*- coding: utf-8 -*-
import sys
from  PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from  PyQt5.QtWidgets import QLabel,QLineEdit,QTextEdit
from  PyQt5.QtWidgets import QVBoxLayout,QFormLayout
from  PyQt5.QtCore import Qt,QDir

class qlineedit(QWidget):
    def __init__(self):
        super(qlineedit,self).__init__()
        self.init()
    def init(self):
        self.label1=QLabel("this is the label")
        self.lineedit1=QLineEdit("test the edit:")
        self.testedit=QTextEdit("test the textedit:")

        lay=QVBoxLayout()
        lay.addWidget(self.label1)
        lay.addWidget(self.lineedit1)
        lay.addWidget(self.testedit)
        self.setLayout(lay)
        self.show()


class formlay(QWidget):
    def __init__(self):
        super(formlay,self).__init__()
        self.init()
    def init(self):
        self.lineedit1=QLineEdit("a")
        self.lineedit2=QLineEdit("b")
        self.lineedit3=QLineEdit("a.b")

        lay=QFormLayout()
        lay.addRow("frist name:",self.lineedit1)
        lay.addRow("second name:",self.lineedit2)
        lay.addRow("name:",self.lineedit3)
        self.setLayout(lay)

        self.lineedit1.textChanged.connect(self.change)
        self.lineedit2.textChanged.connect(self.change)

    def change(self):
        self.text1=self.lineedit1.text()
        self.text2=self.lineedit2.text()
        self.lineedit3.setText(self.text1+'.'+self.text2)


if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=formlay()
    mywin.show()
    sys.exit(app.exec_())
