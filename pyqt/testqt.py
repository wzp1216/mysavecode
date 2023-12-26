import sys
import matplotlib
matplotlib.use('TkAgg')

from PyQt5.QtWidgets import QApplication,QWidget

if __name__=="__main__":
    print("this is start")
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('simple')
    w.show()

    sys.exit(app.exec_())

