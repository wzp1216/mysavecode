# coding: utf-8
from Multi_Function_IO import *
import time

io = MultiFunction_IO()

io.setPWMFreq(50) # 设置输出频率50Hz


io.setServoPulse(0, 1000)
time.sleep(2)
io.setServoPulse(0, 2000)

# Code END 15
