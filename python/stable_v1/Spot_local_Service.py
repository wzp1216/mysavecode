# -*- coding:utf-8 –*-
from __future__ import print_function
from re import T
import rospy
import math
import time
from Spot_Mqtt_Service import *
from Spot_darknet_Service import *
from mavros_msgs.msg import State, PositionTarget,ExtendedState,ParamValue
from mavros_msgs.srv import CommandBool, SetMode,ParamSet,ParamGet
from geometry_msgs.msg import PoseStamped, Twist,Vector3
from sensor_msgs.msg import Imu, NavSatFix
from vision_landing.msg import Local_control_state
from vision_landing.msg import State as vision_land_state
from pyquaternion import Quaternion

class SpotController:
    def __init__(self,target):
        self.imu = None
        self.gps = None
        self.visionland_state = None
        self.home_position_x = None
        self.home_position_y = None
        self.return_home_height = 2
        self.local_pose = None
        self.cur_target_pose = None
        self.arm_state = False
        self.state = None

        self.vision_state = Local_control_state()

        self.meet_x = None
        self.meet_y = None
        self.mqtt_connect = True
        self.dark_connect = True

        self.apple_box_pose = None
        self.potato_box_pose = None
        self.pear_box_pose = None
        self.eggplant_box_pose = None
        self.watermelon_box_pose = None

        self.apple_box_pose1 = None
        self.potato_box_pose1 = None
        self.pear_box_pose1 = None
        self.eggplant_box_pose1 = None
        self.watermelon_box_pose1 = None

        rospy.init_node("spot_local_control")

        '''
        ros subscribers
        '''
        self.local_pose_sub = rospy.Subscriber( "/mavros/local_position/pose", PoseStamped, self.local_pose_callback )
        self.mavros_sub = rospy.Subscriber( "/mavros/state", State, self.state_callback )
        self.gps_sub = rospy.Subscriber( "/mavros/global_position/global", NavSatFix, self.gps_callback )
        self.imu_sub = rospy.Subscriber( "/mavros/imu/data", Imu, self.imu_callback )
        self.landed_sub = rospy.Subscriber ("/mavros/extended_state", ExtendedState, self.landed_callback )
        self.visionland_sub = rospy.Subscriber( "/vision_land/state", vision_land_state, self.visionland_callback )

        '''
        ros publishers
        '''
        self.local_target_pub = rospy.Publisher( "mavros/setpoint_raw/local", PositionTarget, queue_size=10 )
        self.visionland_pub = rospy.Publisher( "/local_control/vision_land/state", Local_control_state, queue_size=10 )
        self.obs_goal_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)

        '''
        ros services
        '''
        self.armService = rospy.ServiceProxy( "/mavros/cmd/arming", CommandBool )
        self.flightModeService = rospy.ServiceProxy( "/mavros/set_mode", SetMode )
        self.param_set_service = rospy.ServiceProxy('/mavros/param/set', ParamSet)  # 设置飞控参数
        self.param_get_service = rospy.ServiceProxy('/mavros/param/get', ParamGet)  # 设置飞控参数

        try:
            self.mqtt = SpotMqtt("S1","Q1")
        except:
            print("\033[31mMqtt init Failed\033[0m")
            self.mqtt_connect = False

        try:
            self.darknet = SpotVisionDarknet(target)
        except:
            print("\033[31mDarknet init Failed\033[0m")
            self.dark_connect = False

        if self.mqtt_connect:self.mqtt.start()

        print("\033[32mSpot Controller Initialized!\033[0m")

    def flytopos(self,x,y,z,yaw,FindTarget = False,Obstacle = False ):
        '''
        直线移动至目标点

        x = 期望位置 X
        y = 期望位置 Y
        z = 期望高度 Z
        yaw  = 期望航向 Yaw
        FindTarget = 飞往目标点期间是否需要寻找目标
        Obstacle = 
        
        '''
        if not self.dark_connect:FindTarget = False
        Apple = 0
        Potato = 0
        Pear = 0
        Eggplant = 0
        Watermelon = 0
        #print("fly to pos")
        if Obstacle:
            self.obs_avoidance(1)
            dis = 0.7
            self.obs_target_pose = self.construct_obs_target(x,y,z)
            for i in range(10):
                self.obs_goal_pub.publish(self.obs_target_pose)
                if self.offboard():
                    time.sleep(0.2)
                    continue
                else:return False
        else:
            self.obs_avoidance(0)
            dis = 0.15
            self.cur_target_pose = self.construct_target(x, y, z, yaw)
            for i in range(10):
                #print("1")
                # 若避障开启时，发布避障设定点。未开时，发布普通设定点
                self.local_target_pub.publish(self.cur_target_pose)
                if self.offboard():
                    time.sleep(0.2)
                    continue
                #else:return False
        #print("set offboard")
        '''
        main ROS thread
        '''
        nonevision =0 
        findclass = False
        while self.state.armed and self.state.mode == "OFFBOARD" and (rospy.is_shutdown() is False):
            if not Obstacle:
                self.local_target_pub.publish(self.cur_target_pose)
            if FindTarget:
                # 读取帧
                vision = self.darknet.vision_Class(0)
                if vision == "":
                    nonevision +=1
                else:
                    nonevision = 0
                if nonevision > 20:
                    findclass = True
                if self.apple_box_pose == None:
                    # 若找到了Apple box，则记录apple_box位置
                    findclass = False
                    if vision == "apple_box":
                        Apple = Apple+1
                    else:Apple = 0
                    if Apple > 3:
                        Apple = 0
                        print("=== Find Apple ===")
                        self.apple_box_pose = [self.local_pose.pose.position.x,self.local_pose.pose.position.y]
                        self.mqtt.push_foundbox("apple_box",self.apple_box_pose)

                elif self.apple_box_pose1 == None and findclass:
                    # 若再次找到了Apple box，则记录apple_box 1位置
                    if vision == "apple_box" and self.vision_position_error(self.apple_box_pose[0],self.apple_box_pose[1]):
                        Apple = Apple+1
                    else:Apple = 0
                    if Apple > 3:
                        Apple = 0
                        print("=== Find Apple 1 ===")
                        self.apple_box_pose1 = [self.local_pose.pose.position.x,self.local_pose.pose.position.y]
                        self.mqtt.push_foundbox("apple_box",self.apple_box_pose1)
                        findclass = False

                if self.potato_box_pose == None:
                    # 若找到了Potato box，则记录potato_box位置
                    if vision == "potato_box":
                        Potato = Potato+1
                    else:Potato = 0
                    if Potato > 3:
                        print("=== Find Potato ===")
                        self.potato_box_pose = [self.local_pose.pose.position.x,self.local_pose.pose.position.y]
                        self.mqtt.push_foundbox("potato_box",self.potato_box_pose)
                        
                if self.pear_box_pose == None:
                    # 若找到了Pear_box，则记录Pear_box位置
                    findclass = False
                    if vision == "pear_box":
                        Pear = Pear+1
                    else:Pear = 0
                    if Pear > 3:
                        print("=== Find Pear ===")
                        self.pear_box_pose = [self.local_pose.pose.position.x,self.local_pose.pose.position.y]
                        self.mqtt.push_foundbox("pear_box",self.pear_box_pose)

                elif self.pear_box_pose1 == None and findclass:
                    # 若找到了Pear_box，则记录Pear_box位置 其中判断pear box的距离
                    if vision == "pear_box" and self.vision_position_error(self.pear_box_pose[0],self.pear_box_pose[1]):
                        Pear = Pear+1
                    else:Pear = 0
                    if Pear > 3:
                        print("=== Find Pear 1 ===")
                        self.pear_box_pose1 = [self.local_pose.pose.position.x,self.local_pose.pose.position.y]
                        self.mqtt.push_foundbox("pear_box",self.pear_box_pose1)
                        findclass = False

                if self.eggplant_box_pose == None:
                    # 若找到了Eggplant box，则记录Eggplant_box位置
                    if vision == "eggplant_box":
                        Eggplant = Eggplant+1
                    else:Eggplant = 0
                    if Eggplant > 3:
                        print("=== Find Eggplant ===")
                        self.eggplant_box_pose = [self.local_pose.pose.position.x,self.local_pose.pose.position.y]
                        self.mqtt.push_foundbox("eggplant_box",self.eggplant_box_pose)
                
                elif self.eggplant_box_pose1 == None and findclass:
                    # 若找到了eggplant_box，则记录eggplant_box位置 其中判断eggplant_box 的距离
                    if vision == "eggplant_box" and self.vision_position_error(self.eggplant_box_pose[0],self.eggplant_box_pose[1]):
                        Eggplant = Eggplant+1
                    else:Eggplant = 0
                    if Eggplant > 3:
                        print("=== Find Eggplant 1 ===")
                        self.eggplant_box_pose1 = [self.local_pose.pose.position.x,self.local_pose.pose.position.y]
                        self.mqtt.push_foundbox("eggplant_box",self.eggplant_box_pose1)
                        findclass = False

                if self.watermelon_box_pose == None:
                    # 若找到了Watermelon，则记录Watermelon位置
                    if vision == "watermelon_box":
                        Watermelon = Watermelon+1
                    else:Watermelon = 0
                    if Watermelon > 3:
                        print("=== Find Watermelon ===")
                        self.watermelon_box_pose = [self.local_pose.pose.position.x,self.local_pose.pose.position.y]
                        self.mqtt.push_foundbox("watermelon_box",self.watermelon_box_pose)

                elif self.watermelon_box_pose1 == None and findclass:
                    # 若找到了eggplant_box，则记录eggplant_box位置 其中判断eggplant_box 的距离
                    if vision == "watermelon_box" and self.vision_position_error(self.watermelon_box_pose[0],self.watermelon_box_pose[1]):
                        Watermelon = Watermelon+1
                    else:Watermelon = 0
                    if Watermelon > 3:
                        print("=== Find Eggplant 1 ===")
                        self.watermelon_box_pose1 = [self.local_pose.pose.position.x,self.local_pose.pose.position.y]
                        self.mqtt.push_foundbox("watermelon_box",self.watermelon_box_pose1)
                        findclass = False
            if self.position_distance(self.local_pose,self.obs_target_pose if Obstacle else self.cur_target_pose,dis):
                self.hover()
                return True
            time.sleep(0.1)
        return False

    def construct_target(self, x, y, z, yaw, yaw_rate = 0.5):
        target_raw_pose = PositionTarget()
        target_raw_pose.header.stamp = rospy.Time.now()
        target_raw_pose.coordinate_frame = 7
        target_raw_pose.position.x = x
        target_raw_pose.position.y = y
        target_raw_pose.position.z = z
        target_raw_pose.velocity = Vector3(0,0,0)
        target_raw_pose.acceleration_or_force = Vector3(0.1,0.1,0.1)
        yaw = math.radians(80-yaw)
        target_raw_pose.yaw = yaw
        target_raw_pose.yaw_rate = yaw_rate
        target_raw_pose.type_mask = 256
        return target_raw_pose

    def construct_obs_target(self, x, y, z):
        target_obs_pose = PoseStamped()
        target_obs_pose.header.stamp = rospy.Time.now()
        target_obs_pose.pose.position.x = x
        target_obs_pose.pose.position.y = y
        target_obs_pose.pose.position.z = z
        return target_obs_pose
    
    def vision_position_error(self,x,y):
        delta_x = math.fabs(x - self.local_pose.pose.position.x)
        delta_y = math.fabs(y - self.local_pose.pose.position.y)
        if(delta_x >2 and delta_y>2):
            return True
        return False
        #return(delta_x+delta_y)

    def position_distance(self, cur_p, target_p, threshold=0.1):
        '''
        判断三维位置误差

        cur_p : poseStamped
        target_p : positionTarget
        threshold : Threshold
        obs : Judge yaw
        '''
        try:
            delta_x = math.fabs(cur_p.pose.position.x - target_p.position.x)
            delta_y = math.fabs(cur_p.pose.position.y - target_p.position.y)
            delta_z = math.fabs(cur_p.pose.position.z - target_p.position.z)
        except:
            delta_x = math.fabs(cur_p.pose.position.x - target_p.pose.position.x)
            delta_y = math.fabs(cur_p.pose.position.y - target_p.pose.position.y)
            delta_z = math.fabs(cur_p.pose.position.z - target_p.pose.position.z)
        if (delta_x + delta_y < threshold):
            if delta_z < 0.3:
                return True
            else:return False
        else:
            return False

    def obs_avoidance(self,status):
        """用于打开或关闭自主避障模式
        Args:
            status(int):1代表打开，0代表关闭
        """
        value = ParamValue()
        param_id = "COM_OBS_AVOID"
        if status in [0,1]:
            value.integer = status
            self.param_set_service(param_id, value)
        else: print("\033[31m error:OBS_param is Invalid\033[0m")

    def local_pose_callback(self, msg):
        self.local_pose = msg
        self.local_yaw = (90-math.degrees(self.q2yaw(self.local_pose.pose.orientation)))

    def state_callback(self, msg):
        self.state = msg

    def imu_callback(self, msg):
        self.imu = msg

    def gps_callback(self, msg):
        self.gps = msg

    """降落状态
    状态值说明:
        UNDEFINED = 0
        GROUND = 1
        IN_AIR = 2
        TAKEOFF = 3
        LANDING = 4
    """
    def landed_callback(self, msg):
        self.landed = msg.landed_state

    def visionland_callback(self, msg):
        self.visionland_state = msg

    def find_vision_tag(self):
        """
        查询红外视觉标签数量
        """
        return self.visionland_state.pointNum

    def vision_land_start(self,land_height = 0):
        '''
        视觉降落函数

        land_height = 0
        '''
        if self.landed == 2:
            if self.local_pose.pose.position.z > land_height+0.5:
                print("=== Start Vision Land ===")
                while(True):
                    self.vision_state.start = True
                    self.vision_state.desired_z = land_height
                    self.visionland_pub.publish(self.vision_state)
                    if not self.state.mode == "OFFBOARD":
                        self.offboard()
                    str = "\rposeX: {:.2f} poseY: {:.2f} nowHeight: {:.2f} pointNum: {:d}".format(self.local_pose.pose.position.x, self.local_pose.pose.position.y, self.local_pose.pose.position.z, self.visionland_state.pointNum)
                    print(str, end="")
                    time.sleep(0.2)
                    if self.visionland_state.workState == False:
                        if self.landed == 1:
                            self.disarm()
                            print("\r\033[32mSpot vision_landing Success\033[0m")
                            return True
                        else:
                            print("\r\033[31mSpot vision land failed!\033[0m")
                            return False
                    if self.landed == 1:
                        self.vision_state.start = False
                        self.visionland_pub.publish(self.vision_state)
                        self.disarm()
                        print("\r\033[32mSpot vision_landing Success\033[0m")
                        return True
            else:
                print("\033[33mSpot not In the air , but less than vision distinguish minimum height!\033[0m")
                self.flytopos(self.local_pose.pose.position.x,self.local_pose.pose.position.y,1.1,self.local_yaw)
                return self.vision_land_start(land_height)
        else:
            print("\033[31mSpot not In the air , vision land failed!\033[0m")
            return False

    def q2yaw(self, q):
        '''
        通过四元数返回航向
        '''
        if isinstance(q, Quaternion):
            rotate_z_rad = q.yaw_pitch_roll[0]
        else:
            q_ = Quaternion(q.w, q.x, q.y, q.z)
            rotate_z_rad = q_.yaw_pitch_roll[0]

        return rotate_z_rad

    def arm(self):
        '''
        解锁，并刷新返航点
        '''
        self.obs_avoidance(0)
        for i in range(20):
            self.armService(True)
            time.sleep(0.5)
            if self.state.armed == True:
                self.home_position_x = self.local_pose.pose.position.x
                self.home_position_y = self.local_pose.pose.position.y
                self.home_position_yaw = self.local_yaw
                print("Spot RTL Home Refresh Success")
                return True
        print("\033[31mSpot Arming failed!\033[0m")
        return False

    def disarm(self):
        '''
        加锁
        '''
        if self.armService(False):
            return True
        else:
            print("\033[31mSpot Disarming Failed\033[0m")
            return False

    def offboard(self):
        '''
        切换Api模式
        '''
        if self.state.mode == "POSCTL" or self.state.mode == "OFFBOARD":
            if self.flightModeService(custom_mode='OFFBOARD'):
                return True
            else:
                print("\033[31mSpot Offboard Failed\033[0m")
                return False
        else:
            print("\033[31mSpot RC mode not of POSTCL\033[0m")
            return False

    def takeoff(self,takeoff_height = 1.5):
        '''
        自动起飞

        takeoff_height = 默认起飞高度 1.5 米
        '''
        self.obs_avoidance(0)
        if self.flytopos(self.local_pose.pose.position.x, self.local_pose.pose.position.y, self.local_pose.pose.position.z + takeoff_height, self.local_yaw):
            return self.takeoff_detection(height = takeoff_height)
        else:
            print("\033[31mSpot TAKEOFF Setpoint Failed\033[0m")
            return False

    def land(self):
        '''
        在当前位置自动降落
        '''
        self.obs_avoidance(0)
        self.flytopos(self.local_pose.pose.position.x,self.local_pose.pose.position.y,-1,self.local_yaw)
        if self.flightModeService(custom_mode='AUTO.LAND'):
            while True:
                if self.landed == 1:
                    print("\033[32mSpot Land Success\033[0m")
                    self.flightModeService(custom_mode='POSCTL')
                    return True
                time.sleep(0.25)
        else:
            print("\033[31mSpot Land Failed\033[0m")
            return False
        
    def hover(self):
        '''
        自动悬停 (飞行器油门需保持中位)
        '''
        if self.flightModeService(custom_mode='POSCTL'):
            #print("\033[32mSpot hover Success\033[0m")
            self.obs_avoidance(0)
            return True
        else:
            print("\033[31mSpot hover Failed\033[0m")
            return False

    def takeoff_detection(self,height = 1):
        time_out = 0
        while True:
            #print("Wait Spot TAKEOFF To Height")
            time_out+=1
            time.sleep(1)
            if self.state.armed == True and time_out <= 50:
                #if (abs(self.local_pose.pose.position.z - height) < 0.5):
                print("\033[32mSpot TAKEOFF Success\033[0m")
                self.hover()
                return True
            else:
                print("\033[31mSpot TAKEOFF Failed: no arm or time out\033[0m")
                return False
        return True

    def car_meet(self):
        """
        飞行器在任意位置请求，飞行器会获取小车位置，并飞往小车上方
        """
        if not self.mqtt_connect:return
        self.mqtt.push_car_mission("land")
        print("\033[33m ====== Drone Request Car Meet ======\033[0m")
        i=0
        self.mqtt.push(cmd="meet")
        while self.mqtt.role2["result"] != 1:
            time.sleep(0.5)
            if i >= 120:  # 等待1分钟
                return False
            i += 1
        # 收到充电平台位置信息后前往
        print("\033[32m ====== Receive Meet Pose ======\033[0m")
        self.meet_x, self.meet_y = self.mqtt.role2["args"]["x"], self.mqtt.role2["args"]["y"]
        print("====== Flyto Meet Pose: x:"+str(self.meet_x) + " y :"+str(self.meet_y))
        self.mqtt.push()  # clear cmd which have done
        self.flytopos(self.meet_x,self.meet_y,1.5,0,Obstacle=True)
        time.sleep(1)
        self.flytopos(self.meet_x,self.meet_y,1.0,0)
        time.sleep(1)
        print("\033[32m ====== Car Meet Mission Completed ======\033[0m")

    def car_land(self):
        """
        飞行器抵达小车上方后，请求降落，小车展板打开等待无人机降落
        无人机自动降落至小车
        """
        if not self.mqtt_connect:return
        self.mqtt.push_car_mission("land")
        print("\033[33m ====== Drone Request Land to Car ======\033[0m")
        # 抵达后请求降落
        i = 0
        self.mqtt.push(cmd="land")
        print("请求降落")
        while self.mqtt.role2["result"] != 1:
            time.sleep(0.5)
            if i >= 120:  # 等待1分钟
                return False
            i += 1
        self.mqtt.push()
        print("\033[32m ====== Car Deck Open Completed ======\033[0m")
        timeout = 0
        tag = 0
        while(True):
            print("====== Find VisionTag:"+str(tag)+ " ======")
            tag = self.find_vision_tag()+tag
            if(tag > 0):
                return self.vision_land_start(0)
            if(timeout > 10):
                self.flytopos(self.meet_x, self.meet_y, 1.5, 0)
                time.sleep(1)
                for i in range(5):
                    tag = self.find_vision_tag()+tag
                    time.sleep(0.5)
                if tag > 0:
                    return self.vision_land_start(0)
                else:
                    print("\033[31m ====== Not Find VisionTag, Drone land Now =======\033[0m")
                    self.land()
                    while True:
                        time.sleep(0.2)
                        if self.landed == 1:
                            self.flightModeService(custom_mode='POSCTL')
                            return False
            timeout+=1
            time.sleep(0.5)

    def car_return_home(self):
        """
        小车不关闭展板的情况下，携带无人机返回起始点
        """
        if not self.mqtt_connect:return
        self.mqtt.push_car_mission("back")
        print("\033[33m ====== Drone Request Car Return Home ======\033[0m")
        # 抵达后请求降落
        i = 0
        self.mqtt.push(cmd="return")
        print("请求返航")
        while self.mqtt.role2["result"] != 1:
            time.sleep(0.5)
            if i >= 120:  # 等待1分钟
                return False
            i += 1
        self.mqtt.push()
        print("\033[32m ====== Car Return Home Completed ======\033[0m")

    def car_start(self):
        """
        小车开始运行，沿磁条行进
        """
        if not self.mqtt_connect:return
        self.mqtt.push_car_mission("start")
        print("\033[33m ====== Drone Request Car Start Mission ======\033[0m")
        i = 0  # 通讯超时计数器，判断小车回复是否超时，i的大小与result的查询间隔和具体任务需要的等待时间有关
        self.mqtt.push(cmd="start")
        while self.mqtt.role2["result"] != 1:
            time.sleep(0.5)
            # 判断超时
            if i >= 10: # 5s超时，即0.5*10
                return True
            i += 1
        self.mqtt.push()
        print("\033[32m ====== Car Start Completed ======\033[0m")

    def car_charge(self,charge_time = 6):
        """
        小车模拟充电
        小车播报语音：正在充电 充电已完成
        charge_time = 充电时间 秒s
        """
        if not self.mqtt_connect:return
        self.mqtt.push_car_mission("wait_charge")
        print("\033[33m ====== Drone Request Charge the Car ======\033[0m")
        i=0
        self.mqtt.push(cmd="wait_charge")
        while self.mqtt.role2["result"] != 1:
            time.sleep(0.5)
            if i >= 120:  # 等待1分钟
                return False
            i += 1
        self.mqtt.push()

        time.sleep(charge_time)
        self.mqtt.push(cmd="charge", args={"status":"False"})
        self.mqtt.push_car_mission("charge")
        while self.mqtt.role2["result"] != 1:
            if self.mqtt.role2["result"] == 2:
                self.mqtt.push(cmd="charge", args={"status":"True"})
            time.sleep(0.5)
            if i >= 120:  # 等待1分钟
                return False
            i += 1
        self.mqtt.push_car_mission("chargeoff")
        self.mqtt.push()
        print("\033[32m ====== Charging Completed ======\033[0m")

    def car_takeoff_reu(self,height = 1.5):
        '''
        飞机从小车平台请求起飞
        并起飞至height

        height = 从小车起飞的起飞高度
        '''
        if not self.mqtt_connect:return
        print("\033[33m ====== Drone Request Takeoff the Car ======\033[0m")
        i = 0
        self.mqtt.push(cmd="takeoff", args={"status":0})
        while self.mqtt.role2["result"] != 1:
            time.sleep(0.5)
            if i >= 120:  # 等待1分钟
                return False
            i += 1
        if self.arm():
            time.sleep(1)
            self.mqtt.push_car_mission("takeoff")
            self.takeoff(height)
            time.sleep(3)
            self.mqtt.push_car_mission("car_start")
            self.mqtt.push(cmd="takeoff", args={"status":1})
            time.sleep(3)
            self.mqtt.push()
            print("\033[32m ====== Takeoff Completed ======\033[0m")

    def carland(self):
        """
        飞行器抵达小车上方后，请求降落，小车展板打开等待无人机降落
        无人机自动降落至小车
        """
        if not self.mqtt_connect:return
        self.mqtt.push_car_mission("land")
        print("\033[33m ====== Drone Request Land to Car ======\033[0m")
        # 抵达后请求降落
        i = 0
        self.mqtt.push(cmd="land")
        print("请求降落")
        while self.mqtt.role2["result"] != 1:
            time.sleep(0.5)
            if i >= 120:  # 等待1分钟
                return False
            i += 1
        self.mqtt.push()
        print("\033[32m ====== Car Deck Open Completed ======\033[0m")
        self.flytopos(drone.meet_x, drone.meet_y, 1, yaw=0)
        time.sleep(1)
        print("\033[32m ====== Drone land Now =======\033[0m")
        time_out = 0
        while True:
            self.flytopos(drone.meet_x, drone.meet_y, drone.local_pose.pose.position.z - 0.2, yaw=0)
            print("Drone is landing")
            time_out+=1
            time.sleep(0.1)
            if self.local_pose.pose.position.z < 0.2:
                self.flightModeService(custom_mode='AUTO.LAND')
                if time_out >= 10:
                    self.flightModeService(custom_mode='POSCTL')
                    time_out = 0
            if self.landed == 1:
                self.disarm()
                print("\033[32m ====== Drone landed =======\033[0m")
                time.sleep(0.5)
                self.flightModeService(custom_mode='POSCTL')
                time.sleep(0.5)
                break

# Code END 711
