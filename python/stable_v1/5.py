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
    Grab = 1.5 # 换行间距 单位米
    Grab_z = 1.3 # 扫描航线飞行高度
    Grab_area_yaw = 0   #飞行器朝向

    # 抓手打开pwn值
    open = 1800 
    close = 770
    # 备用信息，若未识别到，则执行该数据
    mission = json.loads(
        '{"Grab":{"eggplant_box":1,"eggplant_box1":1,"watermelon_box":2,"watermelon_box1":2,"apple_box":3,"apple_box1":3,"pear_box":4,"pear_box1":4}'+
        ',"Grab_area_leftrear":[14.290,7.454],"Grab_area_rightfront":[25.501,17.572]'+
        ',"box1":[29.173, 17.1671, 0.5],"box2":[29.212, 13.1190, 0.5],"box3":[29.244, 8.880, 0.5]}')

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

        drone.flytopos(drone.local_pose.pose.position.x + 0.2, drone.local_pose.pose.position.y + 0.2, 2, 0, True, True)
        time.sleep(1)
        

    def airline(self):  # 航线规划
        line = int(divmod(self.Grab_area_rightfront[0]-self.Grab_area_leftrear[0],self.Grab)[0])+1
        drone.flytopos(self.Grab_area_leftrear[0], self.Grab_area_leftrear[1], self.Grab_z, self.Grab_area_yaw,Obstacle=True) #飞到航线起始点
        for i in range(line):
            drone.mqtt.push_color("yellow")
            
            #飞机直线向北飞行
            if i%2==0:
                drone.flytopos(self.Grab_area_leftrear[0]+i*self.Grab, self.Grab_area_rightfront[1], self.Grab_z, self.Grab_area_yaw,FindTarget = True,Obstacle=True)
                print("直线航线完成")
                # 飞机向左换航
                if (self.Grab_area_rightfront[0]- (self.Grab_area_leftrear[0]+i*self.Grab)) >= self.Grab:
                    if self.replaceline(self.Grab_area_leftrear[0]+i*self.Grab,self.Grab_area_rightfront[1]):
                        print("换航完成")
                else:
                    drone.flytopos(self.Grab_area_rightfront[0],self.Grab_area_rightfront[1],self.Grab_z,self.Grab_area_yaw,FindTarget=True,Obstacle=True)
                    print("换航完成")
                    drone.flytopos(self.Grab_area_rightfront[0],self.Grab_area_leftrear[1],self.Grab_z,self.Grab_area_yaw,FindTarget=True,Obstacle=True)
                    print("航线飞行完成")

            #飞机直线向南飞行
            else:
                drone.flytopos(self.Grab_area_leftrear[0]+i*self.Grab, self.Grab_area_leftrear[1], self.Grab_z, self.Grab_area_yaw,FindTarget = True,Obstacle=True)
                print("直线航线完成")
                # 飞机向右换航
                if (self.Grab_area_rightfront[0] - (self.Grab_area_leftrear[0]+i*self.Grab)) >= self.Grab:
                    if self.replaceline(self.Grab_area_leftrear[0]+i*self.Grab,self.Grab_area_leftrear[1]):
                        print("换航完成")
                else:
                    drone.flytopos(self.Grab_area_rightfront[0],self.Grab_area_leftrear[1],self.Global_z,self.Grab_area_yaw,FindTarget=True,Obstacle=True)
                    print("换航完成")
                    drone.flytopos(self.Grab_area_rightfront[0],self.Grab_area_rightfront[1],self.Grab_z,self.Grab_area_yaw,FindTarget=True,Obstacle=True)
                    print("航线飞行完成")

    def replaceline(self, x , y):
        '''换行函数，飞行器自动向左或向右平移，返回true'''
        if drone.flytopos(x+self.Grab, y, self.Grab_z, self.Grab_area_yaw,FindTarget=True,Obstacle=True):
            return True
    
    def GrabLand(self,x , y , z , yaw = 0 , land_height = 0,target_class = ""):
        ''' 观测点识别箱子 '''
        if drone.state.armed and drone.local_pose.pose.position.z > 0.5:
            # 飞机飞到货物上方
            drone.flytopos(x, y, z, yaw,Obstacle=True)

            # 打开抓手，等待抓取
            io.setServoPulse(0, self.open)
            timeout = 0 # 超时计次变量
            tag = 0 # 红外tag发现累计次数变量
            target_true = 0 # 需要抓取的目标物体名称，识别正确数量

            for i in range(15):
                if drone.darknet.vision_Class(0) == target_class:
                    target_true=target_true+1
                time.sleep(0.2)
            
            # ********************任务5时注释掉********************
            # while(target_true>5):
            #     print("识别到:"+target_class+"!")
            #     time.sleep(1)
            #     drone.land()
            #     drone.flightModeService(custom_mode='POSCTL')
            # print("类别不符，跳过本次抓取")
            # return False
            # *******************任务5时注释掉**********************

            # *********************任务4-2时注释掉******************
            while(target_true>5):
                print("识别到:"+target_class+"!")
                tag = drone.find_vision_tag()+tag
                print("find vision_tag:"+str(tag))
                # 若能找到tag，则调用vision_land_start函数，并返回
                if(tag > 0):
                    return drone.vision_land_start(land_height)
                # 若超时
                if(timeout > 10):
                    # 飞行器上升高度，扩大搜索视野
                    drone.flytopos(x, y, z+0.8, drone.local_yaw)
                    time.sleep(3)
                    tag = drone.find_vision_tag()+tag
                    # 若能找到tag，则调用vision_land_start函数，并返回
                    if tag > 0:
                        return drone.vision_land_start(land_height)
                    # 若仍未找到tag ，则返回false
                    else:
                        print("未找到红外标记")
                        drone.land()
                        drone.flightModeService(custom_mode='POSCTL')
                        return False
                # 每次循环计数+1 频率控制：2hz
                timeout+=1
                time.sleep(0.5)
            print("类别不符，跳过本次抓取")
            return False
            # *********************任务4-2时注释掉******************

    def launch(self,box):
        '''
        飞机起飞，并飞到货物投放区上方后投放箱子
        '''
        if box == 1:
            box_x,box_y,box_z = self.box1[0],self.box1[1],self.box1[2]
        if box == 2:
            box_x,box_y,box_z = self.box2[0],self.box2[1],self.box2[2]
        if box == 3:
            box_x,box_y,box_z = self.box3[0],self.box3[1],self.box3[2]
        if box == 4:
            box_x,box_y,box_z = self.box1[0],self.box1[1],self.box1[2]

        if drone.arm():
            time.sleep(1)
            if drone.takeoff(self.Global_z):
                time.sleep(3)
                # 起飞完成后，向mqtt灯报告当前任务
                drone.mqtt.push_color("blue")
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

        # 读取并载入任务二维码信息
        self.read_qr_code()

        # 开启避障及仿地
        drone.mqtt.open_obstacle("true")
        drone.mqtt.open_terrain("true")

        # 发布小车运行命令，小车驶往无人机起飞位置
        drone.car_start()
        time.sleep(3)

        # 第一次从小车起飞
        drone.car_takeoff_reu(1.3)
        '''
        
        if drone.arm():
            time.sleep(1)
            drone.takeoff(self.Global_z)
        '''
        # 扫描航线，并且读取目标箱子的位置
        self.airline()

        time.sleep(1)

        if "eggplant_box" in self.mission["Grab"]:
            try:print("eggplant_box位置X：" + str(drone.eggplant_box_pose[0]) + " Y："+ str(drone.eggplant_box_pose[1]))
            except:print("未找到eggplant box")
        if "watermelon_box" in self.mission["Grab"]:
            try:print("watermelon_box位置X：" + str(drone.watermelon_box_pose[0]) + " Y："+ str(drone.watermelon_box_pose[1]))
            except:print("未找到watermelon box")
        if "apple_box" in self.mission["Grab"]:
            try:print("apple_box位置X：" + str(drone.apple_box_pose[0]) + " Y："+ str(drone.apple_box_pose[1]))
            except:print("未找到apple box")
        if "pear_box" in self.mission["Grab"]:
            try:print("pear_box位置X：" + str(drone.pear_box_pose[0]) + " Y："+ str(drone.pear_box_pose[1]))
            except:print("未找到pear box")

        # ***********做任务4-2时注释掉***************
        if "eggplant_box1" in self.mission["Grab"]:
            try:print("eggplant_box1位置X：" + str(drone.eggplant_box_pose1[0]) + " Y："+ str(drone.eggplant_box_pose1[1]))
            except:print("未找到eggplant box1")
        if "watermelon_box1" in self.mission["Grab"]:
            try:print("watermelon_box1位置X：" + str(drone.watermelon_box_pose1[0]) + " Y："+ str(drone.watermelon_box_pose1[1]))
            except:print("未找到watermelon box1")
        if "apple_box1" in self.mission["Grab"]:
            try:print("apple_box1位置X：" + str(drone.apple_box_pose1[0]) + " Y："+ str(drone.apple_box_pose1[1]))
            except:print("未找到apple box1")
        if "pear_box1" in self.mission["Grab"]:
            try:print("pear_box1位置X：" + str(drone.pear_box_pose1[0]) + " Y："+ str(drone.pear_box_pose1[1]))
            except:print("未找到pear box1")
        # ***********做任务4-2时注释掉**************

        # 获取小车位置，并飞往
        drone.car_meet()
        time.sleep(1)

        # 辅助降落至小车
        drone.car_land() 
        time.sleep(1)

        # 发送充电命令，充电6秒
        drone.car_charge(6) 
        time.sleep(1)

        # 请求起飞1.3米并自动起飞悬停
        drone.car_takeoff_reu(1.3) 

        # 抓取货物部分，会抓取货物区域内的货物 循环次数根据任务数组长度而定
        appbox = 0 # 苹果抓取次数
        peabox = 0 # 梨抓取次数
        eggbox = 0 # 茄子抓取次数
        watbox = 0 #西瓜抓取次数
        print(str(len(self.mission["Grab"])))
        for i in range(len(self.mission["Grab"])):
            if "eggplant_box" in self.mission["Grab"] and (eggbox < 1) and (drone.eggplant_box_pose != None):
                eggbox=eggbox+1
                print("降落至eggplant box")
                self.GrabLand(drone.eggplant_box_pose[0],drone.eggplant_box_pose[1],self.Grab_z,yaw = 0,target_class = "eggplant_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["eggplant_box"])

            elif "watermelon_box" in self.mission["Grab"] and (watbox < 1) and (drone.watermelon_box_pose != None):
                watbox=watbox+1
                print("降落至watermelon box")
                self.GrabLand(drone.watermelon_box_pose[0],drone.watermelon_box_pose[1],self.Grab_z,yaw = 0,target_class = "watermelon_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["watermelon_box"])

            elif "apple_box" in self.mission["Grab"] and (appbox < 1) and (drone.apple_box_pose != None):
                appbox=appbox+1
                print("降落至apple box")
                self.GrabLand(drone.apple_box_pose[0],drone.apple_box_pose[1],self.Grab_z,yaw = 0,target_class = "apple_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["apple_box"])

            elif "pear_box" in self.mission["Grab"] and (peabox < 1) and (drone.pear_box_pose != None):
                peabox=peabox+1
                print("降落至pear box")
                self.GrabLand(drone.pear_box_pose[0],drone.pear_box_pose[1],self.Grab_z,yaw = 0,target_class = "pear_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["pear_box"])     


            # *******************************任务4-2时注释掉************************
            elif "eggplant_box1" in self.mission["Grab"] and (eggbox < 2) and (drone.eggplant_box_pose1 != None):
                eggbox=eggbox+1
                print("降落至eggplant box 1")
                self.GrabLand(drone.eggplant_box_pose1[0],drone.eggplant_box_pose1[1],self.Grab_z,yaw = 0,target_class = "eggplant_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["eggplant_box1"])

            elif "watermelon_box1" in self.mission["Grab"] and (watbox < 2) and (drone.watermelon_box_pose1 != None):
                watbox=watbox+1
                print("降落至watermelon box 1")
                self.GrabLand(drone.watermelon_box_pose1[0],drone.watermelon_box_pose1[1],self.Grab_z,yaw = 0,target_class = "watermelon_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["watermelon_box1"])

            elif "apple_box1" in self.mission["Grab"] and (appbox < 2) and (drone.apple_box_pose1 != None):
                appbox=appbox+1
                print("降落至apple box 1")
                self.GrabLand(drone.apple_box_pose1[0],drone.apple_box_pose1[1],self.Grab_z,yaw = 0,target_class = "apple_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["apple_box1"])

            elif "pear_box1" in self.mission["Grab"] and (peabox < 2) and (drone.pear_box_pose1 != None):
                peabox=peabox+1
                print("降落至pear box 1")
                self.GrabLand(drone.pear_box_pose1[0],drone.pear_box_pose1[1],self.Grab_z,yaw = 0,target_class = "pear_box")
                time.sleep(3)
                io.setServoPulse(0, self.close)
                drone.mqtt.push_pwm("grab")
                self.launch(self.mission["Grab"]["pear_box1"]) 
            # *******************************任务4-2时注释掉************************

            time.sleep(3)

        time.sleep(2)
        drone.car_meet()
        time.sleep(2)
        drone.car_land()
        time.sleep(2)
        drone.car_return_home()

if __name__ == '__main__':
    ai = AI_TEST()
    io = MultiFunction_IO()
    io.setPWMFreq(50)
    drone = SpotController(target=["eggplant_box","watermelon_box","apple_box","pear_box"])
    ai.start_mission()

# Code END 357