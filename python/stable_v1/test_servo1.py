# coding: utf-8
from Multi_Function_IO import *
import time

io = MultiFunction_IO()

io.setPWMFreq(50) # 设置输出频率50Hz


io.setServoPulse(0, 670)
time.sleep(8)
io.setServoPulse(0, 2200)

# Code END 15
