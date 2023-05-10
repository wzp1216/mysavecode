# coding: utf-8
from Spot_local_Service import *
from Multi_Function_IO import *
from decimal import *
import time
import signal

#定义终止运行函数,用户输入ctrl+c 退出运行
def quit(signum, frame):
    rospy.loginfo("test_targed_node quit")
    sys.exit()

signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)

class AI_TEST(object):

    def start_mission(self):
        while 1:
            time.sleep(1)
            if drone.darknet.vision_Class(0) in ["apple_box", "potato_box", "pear_box", "eggplant_box", "watermelon_box"]:
                print("发现目标物体!")
                drone.mqtt.push_color("red")
                time.sleep(3)
            else:
                print("未发现目标!")

if __name__ == '__main__':
    ai = AI_TEST()
    drone = SpotController(target=["apple_box","potato_box"])
    ai.start_mission()