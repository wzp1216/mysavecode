#!/usr/bin/env python
# coding=utf-8
from PyQt5.QtCore import QObject,pyqtSignal

class testa(QObject):
    mysignal=pyqtSignal(int)
    def sendint(self):
        print("please input a number:")
        try:
            astr=input()
            a=int(astr)
        except ValueError:
            print("input is not a number!")
        self.mysignal.emit(a)
    def recive(self,value):
        print("testa  msg is ",value)

class testb(QObject):
    def recive(self,value):
        print("testb msg is ",value)
        
k=testa()
l=testb()
k.mysignal.connect(k.recive)
k.mysignal.connect(l.recive)
k.sendint();

