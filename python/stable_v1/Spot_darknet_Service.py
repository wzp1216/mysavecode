# -*- coding:utf-8 –*-
import rospy
import cv2
import pyzbar.pyzbar as pyzbar
import math
import time

from darknet_ros_msgs.msg import BoundingBoxes
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class SpotVisionDarknet:
    def __init__(self,target = ["apple_box","pear_box","watermelon_box","eggplant_box"]):
        self.target_class = target
        self.seq = None
        self.darknet = None
        self.Class = None
        self.bridge = CvBridge()
        self.text = None #二维码识别到的文本
        self.frame = None

        try:rospy.init_node("Spot_Darknet")  # 初始化节点
        except:()
        '''Subscriber'''
        self.darknet_bounding = rospy.Subscriber( "/darknet_ros/bounding_boxes", BoundingBoxes, self.darknet_callback)
        self.image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, self.image_callback)

        print("Darknet set find : "+str(self.target_class))
        print("\033[32mDarknet Yolo init Initialized!\033[0m")
    
    def darknet_callback(self, msg):
        '''
        Darknet 神经网络服务回调函数
        '''
        self.darknet = msg
    
    def image_callback(self,ros_image):
        '''
        Ros 图像回调函数，用于抽帧进行二维码任务信息识别
        '''
        self.frame = self.bridge.imgmsg_to_cv2(ros_image, "bgr8")

    def vision_Class(self,lib = 0):
        '''
        读取当前相机识别到的Class
        '''
        try:
            if self.darknet.header.seq == self.seq:
                self.seq = self.darknet.header.seq
                return ""
            else:
                self.seq = self.darknet.header.seq
                # 仅回报需要识别的类型
                if self.darknet.bounding_boxes[lib].Class in self.target_class:
                    return self.darknet.bounding_boxes[lib].Class
                else:return ""
        except:
            return ""

    def decodeDisplay(self,video):
        """
        二维码识别
        输入一帧图像，返回二维码内容（str）
        """
        # 转为灰度图像
        gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        barcodes = pyzbar.decode(gray)
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")
            self.text = barcodeData
            if self.text != "":
                return True

    def detect(self,freq):
        '''
        持续读取图像中二维码数据，返回文本，超时自动退出
        freq : 查找二维码的次数
        '''
        for i in range(freq):
            # 读取当前抽帧
            try:
                frame = self.frame
                if self.decodeDisplay(frame):return True
            except:print("\033[33mNot Have Frame\033[0m")
            print(i)
            time.sleep(0.1)
        return False

# Code END 90