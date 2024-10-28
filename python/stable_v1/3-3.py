# coding: utf-8
from Spot_local_Service import *
from Multi_Function_IO import *

import time
from decimal import *
import signal
import sys
import json

#定义终止运行函数,用户输入ctrl+c 退出运行
def quit(signum, frame):
    rospy.loginfo("test_targed_node quit")
    sys.exit()

signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)

class AI_TEST(object):
    # 全局高度
    Global_z = 1.5

    # 投放箱位置数据
    box1 = [] # 投放1位置
    box2 = [] # 投放2位置
    box3 = [] # 投放3位置

    # 区域航线数据
    Grab_area_leftrear = []     #区域航线左下角 xy
    Grab_area_rightfront = []     #区域航线右上角 xy
    Grab = 3 # 换行间距 单位米
    Grab_z = 1.3 # 扫描航线飞行高度
    Grab_area_yaw = 0   #飞行器朝向

    # 抓手打开pwn值
    open = 2300
    close = 1000
    # 备用信息，若未识别到，则执行该数据
    mission = json.loads(
        '{"Grab":{"apple_box":0,"apple_box1":0,"pear_box":1,"pear_box1":1},"Grab_area_leftrear":[1,1],"Grab_area_rightfront":[17,15]'+
        ',"box1":[20.3618, 13.0644, 0.4],"box2":[20.3668, 8.1924, 0.4],"box3":[20.3668, 3.0560, 0.4]}')

    def read_qr_code(self):
        print("开始识别二维码")
        if drone.darknet.detect(10):
            print(str(drone.darknet.text))
            self.mission = json.loads(drone.darknet.text)
        else:
            print("未识别到二维码，执行备用信息")
        print("载入二维码数据: ")
        print(self.mission["Grab"])
        self.Grab_area_leftrear, self.Grab_area_rightfront = self.mission["Grab_area_leftrear"], self.mission["Grab_area_rightfront"]
        self.box1, self.box2, self.box3 = self.mission["box1"], self.mission["box2"],self.mission["box3"]
        print("lerear x : " + str(self.Grab_area_leftrear[0]) + " lerear y : " + str(self.Grab_area_leftrear[1]))
        print("rifront x : " + str(self.Grab_area_rightfront[0]) + " rifront y : " + str(self.Grab_area_rightfront[1]))
        print("box1 x: " + str(self.box1[0])+ "box1 y: "+str(self.box1[1]))
        print("box2 x: " + str(self.box2[0])+ "box2 y: "+str(self.box2[1]))
        print("box3 x: " + str(self.box3[0])+ "box3 y: "+str(self.box3[1]))

    def airline(self):  # 航线规划
        line = int(divmod(self.Grab_area_rightfront[0]-self.Grab_area_leftrear[0],self.Grab)[0])+1
        i = 1
        drone.flytopos(self.Grab_area_leftrear[0], self.Grab_area_leftrear[1], self.Grab_z, self.Grab_area_yaw,Obstacle=False)
        for i in range(line):   #循环执行航线次数 = 平均数+1
          drone.mqtt.push_color("yellow")
          if i%2==0:    # i为奇数
            # x不变，飞机直线向北
            drone.flytopos(self.Grab_area_leftrear[0]+i*self.Grab, self.Grab_area_rightfront[1], self.Grab_z, self.Grab_area_yaw,FindTarget = True,Obstacle=False)
            print("直线航线完成")
            if self.replaceline(self.Grab_area_leftrear[0]+i*self.Grab,self.Grab_area_rightfront[1]):
                print("换航完成")
                i+=1
          else:   # i为偶数
            drone.flytopos(self.Grab_area_leftrear[0]+i*self.Grab, self.Grab_area_leftrear[1], self.Grab_z, self.Grab_area_yaw,FindTarget = True,Obstacle=False)
            print("直线航线完成")
            if self.replaceline(self.Grab_area_leftrear[0]+i*self.Grab,self.Grab_area_leftrear[1]):
                print("换航完成")
                i+=1
        if line%2==0: # line为奇数
            drone.flytopos(self.Grab_area_rightfront[0], self.Grab_area_rightfront[1], self.Grab_z, self.Grab_area_yaw,FindTarget=True,Obstacle=False)

    def replaceline(self, x , y):
        '''换行函数，飞行器自动向左或向右平移，返回true'''
        if drone.flytopos(x+self.Grab, y, self.Grab_z, self.Grab_area_yaw,FindTarget=True,Obstacle=False):
            return True
    
    def GrabLand(self,x , y , z , yaw = 0 , land_height = 0,target_class = "apple_box"):
        ''' 观测点识别箱子 '''
        if drone.state.armed and drone.local_pose.pose.position.z > 0.5:
            io.setServoPulse(0, self.open)
            # 飞机飞到货物上方
            drone.flytopos(x, y, z, yaw,Obstacle=True)
            time.sleep(1)
            drone.flytopos(x,y,0.4,yaw)
            time.sleep(3)
            drone.land()    

    def launch(self,box):
        '''
        飞机起飞，并飞到货物投放区上方后投放箱子
        '''
        if box == 0:
            box_x,box_y,box_z = self.box1[0],self.box1[1],self.box1[2]
        if box == 1:
            box_x,box_y,box_z = self.box2[0],self.box2[1],self.box2[2]
        if box == 2:
            box_x,box_y,box_z = self.box3[0],self.box3[1],self.box3[2]

        if drone.arm():
            time.sleep(1)
            if drone.takeoff(self.Global_z):
                time.sleep(3)
                # 起飞完成后，向mqtt灯报告当前任务
                drone.mqtt.push_color("blue")
                # 箱子上方 第三个参数代表飞机高度
                drone.flytopos(box_x,box_y,self.Global_z,drone.local_yaw,Obstacle=False)
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

        # 读取并载入任务二维码信息
        self.read_qr_code()

        # 开启避障及仿地
        drone.mqtt.open_obstacle("true")
        drone.mqtt.open_terrain("true")

        # 第一次从小车起飞
        if drone.arm():
            drone.takeoff(1.3)

        # 扫描航线，并且读取目标箱子的位置
        self.airline()

        time.sleep(1)

        if "apple_box" in self.mission["Grab"]:
            try:print("apple位置X：" + str(drone.apple_box_pose[0]) + " Y："+ str(drone.apple_box_pose[1]))
            except:print("未找到apple box")
        if "apple_box1" in self.mission["Grab"]:
            try:print("apple1位置X：" + str(drone.apple_box_pose1[0]) + " Y："+ str(drone.apple_box_pose1[1]))
            except:print("未找到apple box1")
        if "pear_box" in self.mission["Grab"]:
            try:print("pear位置X：" + str(drone.pear_box_pose[0]) + " Y："+ str(drone.pear_box_pose[1]))
            except:print("未找到pear box")
        if "pear_box1" in self.mission["Grab"]:
            try:print("pear1位置X：" + str(drone.pear_box_pose1[0]) + " Y："+ str(drone.pear_box_pose1[1]))
            except:print("未找到pear box1")

        # 抓取货物部分，会抓取货物区域内的货物 循环次数根据任务数组长度而定
        appbox = 0 # 苹果抓取次数
        peabox = 0 # 土豆抓取次数
        eggbox = 0
        print(str(len(self.mission["Grab"])))
        for i in range(len(self.mission["Grab"])):
            if "apple_box" in self.mission["Grab"] and (appbox < 1) and (drone.apple_box_pose != None):
                appbox=appbox+1
                print("降落至apple box")
                self.GrabLand(drone.apple_box_pose[0],drone.apple_box_pose[1],self.Grab_z,yaw = 0,target_class = "apple_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["apple_box"])

            elif "apple_box1" in self.mission["Grab"] and (appbox < 2) and (drone.apple_box_pose1 != None):
                appbox=appbox+1
                print("降落至apple box 1")
                self.GrabLand(drone.apple_box_pose1[0],drone.apple_box_pose1[1],self.Grab_z,yaw = 0,target_class = "apple_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["apple_box1"])
                

            elif "pear_box" in self.mission["Grab"] and (peabox < 1) and (drone.pear_box_pose != None):
                peabox=peabox+1
                print("降落至pear box")
                self.GrabLand(drone.pear_box_pose[0],drone.pear_box_pose[1],self.Grab_z,yaw = 0,target_class = "pear_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["pear_box"])
                #=============

            elif "pear_box1" in self.mission["Grab"] and (peabox < 2) and (drone.pear_box_pose1 != None):
                peabox=peabox+1
                print("降落至pear box1")
                self.GrabLand(drone.pear_box_pose1[0],drone.pear_box_pose1[1],self.Grab_z,yaw = 0,target_class = "pear_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["pear_box1"])
                #==========

            time.sleep(3)


if __name__ == '__main__':
    ai = AI_TEST()
    io = MultiFunction_IO()
    io.setPWMFreq(50)
    drone = SpotController(target=["apple_box","pear_box","eggplant_box"])
    ai.start_mission()

# Code END 219