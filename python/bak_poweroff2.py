#!/home/wzp/anaconda3/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont 


def date_read():
    try:
        with open('user_time.json','r',encoding='utf-8') as fs:
            t=json.load(fs)
    except IOError as e:
        print(e)
    #print("read the time")
    return t; 


def date_write(t):
    try:
        with open('user_time.json','w',encoding='utf-8') as fs:
            json.dump(t,fs)
    except IOError as e:
        print(e)
    #print("save the time")




#读取JSON日期，判断是否今天，不是今天改为今天；是今天则看时间是否到60；
#json使用时间＋2；
def json_read1():
    showUI=False
    t=time.localtime(time.time())
    use_time=0
    tim={
            'year':t.tm_year,
            'mon':t.tm_mon,
            'day':t.tm_mday,
            'hour':t.tm_hour,
            'min':t.tm_min,
            'usertime':use_time
            }

    date_write(tim)
    tim1=date_write(tim)

    if (tim['year']==tim1['year'] and tim['mon']==tim1['mon']  and tim['day']==tim1['day']):
        sameday=True
    else:
        sameday=False
    
    if (sameday):
        tim['usertime']=tim1['usertime']
        tim['usertime']+=2
        date_write(tim)

        tim1=date_read()
#判断时间，时间大于60则关机；
        if (tim1['usertime']>=60):
            print("shutdown now")
            os.system("echo 'wzy091030' | sudo -S shutdown -a +3")
   
#判断时间，时间整除20则提示；
        tim1=date_read()
        if (tim1['usertime']%20==0):
            print("user time 20 mins")
            showUI=True

    if (not sameday):
        date_write(tim)

    return showUI


class Test1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('使用提醒')
        self.label1=QLabel("使用时间已20分钟")
        self.setCentralWidget(self.label1)
        self.show()

#mainwodows


if __name__=='__main__':
    a=json_read1()
    if (a):
        app = QApplication(sys.argv)
        font=QFont()
        font.setPointSize(24); 
        app.setFont(font); 
        ex=Test1()
        sys.exit(app.exec_())


