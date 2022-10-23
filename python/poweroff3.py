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
    tim1=date_read()

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
        if (tim1['usertime']>=51):
            os.system("bash /opt/user_time/shut2_msg.sh")
            os.system("echo 'wzy091030' | sudo -S shutdown -h now")
   
#判断时间，时间整除20则提示；
        tim1=date_read()
        if (tim1['usertime']%10==0):
            #print("user time 10 mins")
            showUI=True

    if (not sameday):
        date_write(tim)

    return showUI

#mainwodows


if __name__=='__main__':
    a=json_read1()
    if (a):
        os.system("bash /opt/user_time/tim20.sh")



