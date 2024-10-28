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
    # 区域航线数据
    Grab_area_leftrear = [1,1]     #区域航线左下角 xy
    Grab_area_rightfront = [17,15]     #区域航线右上角 xy
    Grab = 3 #换行间距  = 摄像头视距 单位米
    Grab_z = 3
    Grab_area_yaw = 0   #飞行器朝向

    def airline(self):  # 航线规划
        line = int(divmod(self.Grab_area_rightfront[0]-self.Grab_area_leftrear[0],self.Grab)[0])+1
        i = 1
        drone.flytopos(self.Grab_area_leftrear[0], self.Grab_area_leftrear[1], self.Grab_z, self.Grab_area_yaw,Obstacle=True)
        for i in range(line):   #循环执行航线次数 = 平均数+1
          if i%2==0:    # i为奇数
            # x不变，飞机直线向北
            drone.flytopos(self.Grab_area_leftrear[0]+i*self.Grab, self.Grab_area_rightfront[1], self.Grab_z, self.Grab_area_yaw,FindTarget = True,Obstacle=True)
            print("直线航线完成")
            if self.replaceline(self.Grab_area_leftrear[0]+i*self.Grab,self.Grab_area_rightfront[1]):
                print("换航完成")
                i+=1
          else:   # i为偶数
            drone.flytopos(self.Grab_area_leftrear[0]+i*self.Grab, self.Grab_area_leftrear[1], self.Grab_z, self.Grab_area_yaw,FindTarget = True,Obstacle=True)
            print("直线航线完成")
            if self.replaceline(self.Grab_area_leftrear[0]+i*self.Grab,self.Grab_area_leftrear[1]):
                print("换航完成")
                i+=1
        if line%2==0: # line为奇数
            drone.flytopos(self.Grab_area_rightfront[0], self.Grab_area_rightfront[1], self.Grab_z, self.Grab_area_yaw,FindTarget=True,Obstacle=True)

    def replaceline(self, x , y):
        '''换行函数，飞行器自动向左或向右平移，返回true'''
        if drone.flytopos(x+self.Grab, y, self.Grab_z, self.Grab_area_yaw,FindTarget=True,Obstacle=True):
            return True

    def start_mission(self):
        # 开启避障及仿地
        drone.mqtt.open_obstacle("true")
        drone.mqtt.open_terrain("true")

        if drone.arm():
            time.sleep(1)
            if drone.takeoff(self.Grab_z):
                time.sleep(1)
                # 扫描航线，并且读取目标箱子的位置
                self.airline()
                time.sleep(5)
                try:print("apple位置X：" + str(drone.apple_box_pose[0]) + " Y："+ str(drone.apple_box_pose[1]))
                except:print("未找到apple box")
                try:print("eggplant位置X：" + str(drone.eggplant_box_pose[0]) + " Y："+ str(drone.eggplant_box_pose[1]))
                except:print("未找到eggplant box")
                try:print("pear位置X：" + str(drone.pear_box_pose[0]) + " Y："+ str(drone.pear_box_pose[1]))
                except:print("未找到pear box")
                try:print("watermelon位置X：" + str(drone.watermelon_box_pose[0]) + " Y："+ str(drone.watermelon_box_pose[1]))
                except:print("未找到watermelon box")
            elif drone.land():  #返航点
                return

if __name__ == '__main__':
    ai = AI_TEST()
    drone = SpotController(target=["apple_box","eggplant_box","pear_box","watermelon_box"])
    ai.start_mission()