
from PyQt5.QtCore import QThread,pyqtSignal,QDateTime
from PyQt5.QtWidgets import QApplication,QDialog,QLineEdit
import sys
import time

class BackendThread(QThread):
    update_date=pyqtSignal(str)
    def run(self):
        for i in range(1000):
            data=QDateTime.currentDateTime()
            currtime=data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currtime))
            time.sleep(1)

class mywin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt signal and thread sample")
        self.resize(400,100)
        self.input=QLineEdit(self)
        self.input.resize(400,100)
        self.initUI()
    def initUI(self):
        self.backend=BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.backend.start()
    def handleDisplay(self,data):
        self.input.setText(data)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=mywin()
    win.show()
    sys.exit(app.exec_())
    



