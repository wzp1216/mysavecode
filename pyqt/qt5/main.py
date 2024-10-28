# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from mymaniwin import mymainwin

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainwin=mymainwin();
    mainwin.show()
    sys.exit(app.exec_())
