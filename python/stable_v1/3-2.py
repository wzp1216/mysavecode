# coding: utf-8
from Spot_local_Service import *
from Multi_Function_IO import *
from decimal import *
import time
import signal
import sys

#定义终止运行函数,用户输入ctrl+c 退出运行
def quit(signum, frame):
    rospy.loginfo("test_targed_node quit")
    sys.exit()

signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)

class AI_TEST(object):
    # 全局高度
    Grab_area_x = 3.7700   # 默认箱子所在的位置 抓取的区域
    Grab_area_y = 5.4000
    Grab_area_yaw = 0 # 正北

    Global_z = 1.3

    # 投放箱位置数据
    box1_x = 20.3618 # 投放1位置
    box1_y = 13.0644
    box1_z = 0.5

    # 抓手打开pwn值
    open = 1800
    close = 870
    
    def GrabLand(self,x , y , z , yaw = 0 , land_height = 0,target_class = "apple_box"):
        ''' 观测点识别箱子 '''
        if drone.state.armed and drone.local_pose.pose.position.z > 0.5:
            # 飞机飞到货物上方
            drone.flytopos(x, y, z, yaw,Obstacle=True)

            # 打开抓手，等待抓取
            io.setServoPulse(0, self.open)
            drone.flytopos(x, y, 0.5, yaw=0)
            drone.land()

    def launch(self):
        '''
        飞机起飞，并飞到货物投放区上方后投放箱子
        '''
        box_x,box_y,box_z = self.box1_x,self.box1_y,self.box1_z

        if drone.arm():
            time.sleep(1)
            if drone.takeoff(self.Global_z):
                time.sleep(3)
                # 起飞完成后，向mqtt灯报告当前任务
                # drone.mqtt.push_color("yellow")
                # 箱子上方 第三个参数代表飞机高度
                drone.flytopos(box_x,box_y,self.Global_z,drone.local_yaw,Obstacle=True)
                time.sleep(5)
                # 仍然是箱子上方，但降低高度确保投放精度
                drone.flytopos(box_x,box_y,box_z+0.1,drone.local_yaw)
                time.sleep(3)
                # 等待飞行器稳定后，打开抓手
                io.setServoPulse(0, self.open)
                drone.mqtt.push_pwm("throw")
                time.sleep(2)
                # 投放完毕后，上升高度
                drone.flytopos(box_x,box_y,self.Global_z,drone.local_yaw)
                time.sleep(2)
                return True

    def start_mission(self):
        # 抓手初始化输出通道 1、2需要根据通道进行调整
        io.setServoPulse(0, self.open)
        # 开启避障及仿地
        drone.mqtt.open_obstacle("true")
        drone.mqtt.open_terrain("true")
        time.sleep(1)
        if drone.arm():
            time.sleep(1)
            if drone.takeoff(self.Global_z):
                time.sleep(1)
                self.GrabLand(self.Grab_area_x,self.Grab_area_y,1.0,0,0,"apple_box")
                time.sleep(2)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch()

            elif drone.land():  #返航点
                return

if __name__ == '__main__':
    ai = AI_TEST()
    io = MultiFunction_IO()
    io.setPWMFreq(50)
    drone = SpotController(target = ["apple_box","pear_box","eggplant_box","watermelon_box"])
    ai.start_mission()