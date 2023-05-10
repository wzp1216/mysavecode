# coding: utf-8
import paho.mqtt.client as mqtt
import json
import threading
import time
import copy
import signal
import os
import sys

from threading import Thread,  Condition

signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)

class SpotMqtt:
    HOST = "192.168.8.188"
    PORT = 1883
    raw_msg = {
        "cmd":"",
        "args":{},
        "qon":0
    }

    def __init__(self, role1, role2): 
        # 初始化mqtt
        try:
            self.client = mqtt.Client()
            self.client.connect(self.HOST, self.PORT, keepalive=600)
            self.client.on_connect=self.on_connect
            self.client.loop_start()
            self.mode = "listen"
            self.role1 = self.raw_msg.copy()  # 注意此处需要拷贝
            self.role1["id"] = role1
            exec("self."+role1+"=self.role1")
            self.role2 = self.raw_msg.copy()
            self.role2["id"] = role2
            self.role2["result"] = 2
            exec("self."+role2+"=self.role2")
            self.topic = "/"+self.role1["id"]+"2"+self.role2["id"]  # 发布topic
            self.led_topic = "/"+role2+"/referee/color_led"  # 定义led的topic
        except:
            print("\033[31mNot Connected MQTT Service\033[0m")

    def on_connect(self, client, userdata, flags, rc):
        print("\033[32mConnected with result code"+str(rc)+"\033[0m")
        self.client.on_message = self.on_message
        self.client.subscribe("/"+self.role2["id"]+"2"+self.role1["id"], qos=0)

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("On Subscribed: qos = %d" % granted_qos)

    def on_disconnect(self, client, userdata, rc):  #后续需要实现掉线重连机制
        if rc != 0:
            print("\033[33m Unexpected disconnection %s\033[0m" % rc)
    
    def on_message(self, client, userdata, msg):
        # print("Receive msg::"+msg.topic + "::" + str(msg.payload))
        
        try:  role2_msg = json.loads(str(msg.payload))
        except:
            print("\033[33m Receive json error\033[0m")
            return False
        try: temp=role2_msg["body"]
        except:
            print("\033[33m message.body error\033[0m")
            return False

        if self.mode == "push":
            if self.role1["cmd"] != temp["cmd"]:
                #print("cmd error:inconformity")
                return False

        self.role2["cmd"] = temp["cmd"]
        self.role2["id"] = temp["id"]
        self.role2["qon"] = temp["qon"]
        self.role2["args"] = temp["args"]
        self.role2["result"] = temp["result"]
        #print(self.role2)
    
    def live(self):  # 后续实现长时间无响应，自动断线机制
        """持续发送消息"""
        while 1:
            time.sleep(1)
            self.role1_msg["timestamp"] = time.time()  # 更新时间戳
            payload = json.dumps(self.role1_msg)  # 更新消息内容
            self.client.publish(self.topic, payload=payload, qos=0)
        
    def start(self):
        """开始与外部设备双向通讯"""
        # 握手5次
        for i in range(5):
            try:
                self.client.publish("/"+self.role2["id"], payload='{"requestid":"' + self.role1["id"] +'"}')
                time.sleep(0.3)
            except:
                print("\033[31mNot Connected MQTT Service: " + self.HOST+"\033[0m")
                sys.exit()

        self.mode = "push"
        # 初始化请求
        self.role1_msg = {
            "type":"WorkRequest",
            "body":self.role1,
            "timestamp": 1231231233
        }
        listen = threading.Thread(target=self.live)
        listen.setDaemon(True)
        listen.start()

    def push(self, cmd="", args={}, qon=1):
        """更新消息内容，在完成所有消息内容修改后调用"""
        self.role1["cmd"]=cmd
        self.role1["args"]=args
        self.role1["qon"]=qon
        self.role1_msg["body"]=self.role1
        self.role2["result"]=2
        #print(self.role1_msg)

    def stop(self):
        """结束通讯"""
        # 发送qon=0一段时间后，结束live，但不关闭与服务器连接和订阅
        pass

    def push_color(self, color):
        color_msg = {}        
        color_msg["color"]=color
        color_pay = json.dumps(color_msg)
        try:
            self.client.publish(self.led_topic, payload=color_pay, qos=0)
            time.sleep(0.2)
        except Exception as e:
            print("\033[31m MQTT error\033[0m", e)

    def push_pwm(self, pwm):
        try:
            print("pwm : "+pwm)
            self.client.publish("/1/referee/pwm", payload=pwm, qos=0)
            time.sleep(0.2)
        except Exception as e:
            print("\033[31m MQTT error\033[0m", e)

    def push_car_mission(self,mission):
        try:
            self.client.publish("/1/referee/car_mission", payload=mission, qos=0)
            time.sleep(0.2)
        except Exception as e:
            print("\033[31m MQTT error\033[0m", e)
    
    def open_obstacle(self,obstacle):
        if obstacle in ["false","true"]:
            try:
                self.client.publish("/1/referee/obstacle", payload=obstacle, qos=0)
                time.sleep(0.2)
            except Exception as e:
                print("\033[31m MQTT error\033[0m", e)
        else: print("\033[31m error:Obstacle is Invalid\033[0m")

    def open_terrain(self,terrain):
        if terrain in ["false","true"]:
            try:
                self.client.publish("/1/referee/distance", payload=terrain, qos=0)
                time.sleep(0.2)
            except Exception as e:
                print("\033[31m MQTT error\033[0m", e)
        else: print("\033[31m error:Terrain is Invalid\033[0m")

    def push_foundbox(self, box_class,pose):
        #rolev = []
        self.push_color("red")
        try:
            rolev = {
                "box_class":box_class,
                "x":pose[0],
                "y":pose[1]
            }
            payload = json.dumps(rolev)  # 更新消息内容
            print(payload)
            self.client.publish("/1/referee/vision", payload=payload, qos=0)
            time.sleep(0.2)
        except Exception as e:
            print("\033[31m MQTT error\033[0m", e)