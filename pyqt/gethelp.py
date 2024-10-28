import sys
from PyQt5.QtWidgets import QWidget

out=sys.stdout
sys.stdout=open('./help_qwidget.txt','w')
help(QWidget)
sys.stdout.close()
sys.stdout=out


