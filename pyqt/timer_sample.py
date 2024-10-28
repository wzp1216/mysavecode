
import sys
from PyQt5.QtWidgets import QDialog,QApplication,QLabel,QPushButton,QGridLayout
from PyQt5.QtCore import QTimer,QDateTime

class time_winForm(QDialog):
    def __init__(self,parent=None):
        super(time_winForm,self).__init__(parent)
        self.setWindowTitle("time demo")
        #self.listFile=QListWidget()
        self.label=QLabel("time:")
        self.startbtn=QPushButton("start")
        self.endbtn=QPushButton("stop")
        self.timeint=QLabel("")
        layout=QGridLayout(self)
        #init a timer
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.showtime)
        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startbtn,1,0)
        layout.addWidget(self.endbtn,1,1)
        layout.addWidget(self.timeint,2,1,2,2)
        #connect signal
        self.startbtn.clicked.connect(self.starttimer)
        self.endbtn.clicked.connect(self.endtimer)
        self.setLayout(layout)
    def showtime(self):
        time=QDateTime.currentDateTime()
        timeDisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)
    def starttimer(self):
        self.timer.start(1000)
        self.startbtn.setEnabled(False)
        self.endbtn.setEnabled(True)
        self.tim1=QDateTime.currentDateTime()
    def endtimer(self):
        self.timer.stop()
        self.startbtn.setEnabled(True)
        self.endbtn.setEnabled(False)
        self.tim2=QDateTime.currentDateTime()
        self.tim3=self.tim2.toTime_t()-self.tim1.toTime_t()
        self.timeint.setText(str(self.tim3)+"s")

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=time_winForm()
    win.show()
    sys.exit(app.exec_())

