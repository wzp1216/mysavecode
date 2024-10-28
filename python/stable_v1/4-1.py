# coding: utf-8
from Spot_local_Service import *
from Multi_Function_IO import *
from decimal import *
import time
import signal
import os
import sys

#定义终止运行函数,用户输入ctrl+c 退出运行
def quit(signum, frame):
    rospy.loginfo("test_targed_node quit")
    sys.exit()

signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)

class AI_TEST(object):
    # 全局高度
    Global_z = 1.3

    def start_mission(self):
        drone.car_start()
        time.sleep(3)

        drone.mqtt.open_obstacle("true")
        drone.mqtt.open_terrain("true")
        # 第一次从小车起飞
        drone.car_takeoff_reu(1.3)

        time.sleep(5)
        # 小车降落
        drone.car_meet() # 获取小车位置，并飞往
        time.sleep(1)
        drone.car_land() # 辅助降落至小车
        time.sleep(1)
        drone.car_charge() # 发送充电命令
        time.sleep(3)
        drone.car_takeoff_reu(1.5) # 请求起飞并自动起飞悬停
        time.sleep(2)
        drone.flytopos(5,5,2,0,Obstacle=True)
        time.sleep(2)
        drone.car_meet()
        time.sleep(2)
        drone.car_land()
        time.sleep(2)
        drone.car_return_home()

if __name__ == '__main__':
    ai = AI_TEST()
    drone = SpotController(target=["apple_box","potato_box"])
    ai.start_mission()

# Code END 52