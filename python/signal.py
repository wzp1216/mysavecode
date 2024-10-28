import sys
from PyQt5.QtWidgets import QApplication,QPushButton
from PyQt5.QtCore import QObject,pyqtSignal,pyqtSlot

class Communicate(QObject):
    speak= pyqtSignal((int,),(str,))
    def __init__(self,parent=None):
        super().__init__()
        self.speak[int].connect(self.say_something)
        self.speak[str].connect(self.say_something)

    @pyqtSlot(int)
    @pyqtSlot(str)
    def say_something(self,arg):
        if isinstance(arg,int):
            print("This is a number:",arg)
        elif isinstance(arg,str):
            print("This is a string:",arg)

if __name__=='__main__':
    app=QApplication(sys.argv)
    someone=Communicate()

    someone.speak[int].emit(20)
    someone.speak[str].emit("hello everyboy")


        
