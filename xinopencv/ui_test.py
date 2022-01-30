import sys
from PyQt5 import QtWidgets

from loadui import Ui_load
#from uitest import class


class testwin(QtWidgets.QWidget,Ui_load):
    def __init__(self):
        super(testwin,self).__init__()
        self.setupUi(self)

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    w=testwin()
    w.show()
    sys.exit(app.exec_())

