# coding: utf-8
from decimal import *
import os
import smbus
import time
import math
class MultiFunction_IO:
    def __init__(self):
        self.SUBADR1 = 0x02
        self.SUBADR2 = 0x03
        self.SUBADR3 = 0x04
        self.MODE1 = 0x00
        self.PRESCALE = 0xFE
        self.LED0_ON_L = 0x06
        self.LED0_ON_H = 0x07
        self.LED0_OFF_L = 0x08
        self.LED0_OFF_H = 0x09
        self.ALLLED_ON_L = 0xFA
        self.ALLLED_ON_H = 0xFB
        self.ALLLED_OFF_L = 0xFC
        self.ALLLED_OFF_H = 0xFD
        self.bus = smbus.SMBus(1)
        self.address = 0x40
        self.write(self.MODE1, 0x00)
        
        print("\033[32mSpot MultiFunction_IO Initialized!\033[0m")

    def write(self, reg, value):
        "Writes an 8-bit value to the specified register/address"
        self.bus.write_byte_data(self.address, reg, value)

    def read(self, reg):
        "Read an unsigned byte from the I2C device"
        result = self.bus.read_byte_data(self.address, reg)
        return result

    def setPWMFreq(self, freq):
        "设置输出频率"
        prescaleval = 25000000.0  # 25MHz
        prescaleval /= 4096.0  # 12-bit
        prescaleval /= float(freq)
        prescaleval -= 1.0
        prescale = math.floor(prescaleval + 0.5)
        oldmode = self.read(self.MODE1)
        newmode = (oldmode & 0x7F) | 0x10  # sleep
        self.write(self.MODE1, newmode)  # go to sleep
        self.write(self.PRESCALE, int(math.floor(prescale)))
        self.write(self.MODE1, oldmode)
        time.sleep(0.005)
        self.write(self.MODE1, oldmode | 0x80)

    def setPWM(self, channel, on, off):
        "设置单个通道"
        self.write(self.LED0_ON_L + 4 * channel, on & 0xFF)
        self.write(self.LED0_ON_H + 4 * channel, on >> 8)
        self.write(self.LED0_OFF_L + 4 * channel, off & 0xFF)
        self.write(self.LED0_OFF_H + 4 * channel, off >> 8)

    def setServoPulse(self, channel, pulse):
        "设置舵机脉冲，输出频率必须为50Hz"
        pulse = int(pulse * 4096 / 20000)  # PWM frequency is 50HZ,the period is 20000us
        self.setPWM(channel, 0, pulse)


    def setMotoPluse(self, channel, pulse):
        if pulse > 3000:
            self.setPWM(channel, 0, 3000)
        else:
            self.setPWM(channel, 0, pulse)
            
    def selfCheck(self):
        self.setServoPulse(0, 2000)
        time.sleep(1)
        self.setServoPulse(0, 1500)

# Code END 76