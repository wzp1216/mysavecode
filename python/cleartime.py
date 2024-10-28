#!/home/wzp/anaconda3/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import os
import json


def date_read():
    try:
        with open('/opt/user_time/user_time.json','r') as fs:
            t=json.load(fs)
            return t; 
    except IOError as e:
        print(e)
    #print("read the time")


def date_write(t):
    try:
        with open('/opt/user_time/user_time.json','w') as fs:
            json.dump(t,fs)
    except IOError as e:
        print(e)
    #print("save the time")


#json使用时间=2；
def clear_time():
    tim1=date_read()
    tim1['usertime']=2
    date_write(tim1)

#mainwodows
    

if __name__=='__main__':
    clear_time()
    os.system("/usr/bin/notify-send 'tim=2' ")



