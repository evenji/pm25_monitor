#!/usr/bin/env python3
# -*- coding: utf-8 -*

import paho.mqtt.client as mqtt
from enum import Enum
import json

class MQTT_RETURN_VALUE(Enum):
    MRV_CONNECT_SUCCESS               = 0
    MRV_VERSION_ERROR                 = 1
    MRV_INVALID_CLIENT_ID             = 2
    MRV_SERVER_ERROR                  = 3
    MRV_INVALID_USERNAME_OR_PASSWORDS = 4
    MRV_NO_AUTHORIZATION              = 5

class Mqtt_Client(object):

    clientID = "PTPM25_1"
    user = r"k5nahpt/PT_PM25_Sensor"
    passwd  = "p6JDJ7MqixIq2GJ8"
    server = "k5nahpt.mqtt.iot.gz.baidubce.com"
    topic_upload_info = r"$baidu/iot/shadow/PT_PM25_Sensor/update"
    port = 1883

    def __init__(self, callback_on_connect):
        self.__callback_on_connect = callback_on_connect
        pass
    
    def load_config(self):
        pass
    
    def connect_server(self):
        self.__client = mqtt.Client(self.clientID)
        self.__client.username_pw_set(self.user,self.passwd)
        self.__client.on_connect = self.on_connect
        self.__client.on_message = self.on_message
        #self.__client.on_disconnect = self.on_disconnect
        self.__client.connect(self.server, self.port, 60)
        self.__client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        if MQTT_RETURN_VALUE["MRV_CONNECT_SUCCESS"].value == rc:
            print("Connect MQTT Server Successfully!")
            self.__callback_on_connect()
            #client.subscribe("$baidu/iot/shadow/pm25_new/update/snapshot")
        elif MQTT_RETURN_VALUE["MRV_VERSION_ERROR"].value == rc:
            print("Connect MQTT Sever Failed, version error!")
        elif MQTT_RETURN_VALUE["MRV_INVALID_CLIENT_ID"].value == rc:
            print("Connect MQTT Sever Failed, invalid client id!")
        elif MQTT_RETURN_VALUE["MRV_SERVER_ERROR"].value == rc:
            print("Connect MQTT Sever Failed, server error!")
        elif MQTT_RETURN_VALUE["MRV_INVALID_USERNAME_OR_PASSWORDS"].value == rc:
            print("Connect MQTT Sever Failed, invalid username or passwords!")
        elif MQTT_RETURN_VALUE["MRV_NO_AUTHORIZATION"].value == rc:
            print("Connect MQTT Sever Failed, no authorzation!")

    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    def package_info(self, info):
        payload_dict = {"reported":info}
        payload_json = json.dumps(payload_dict)
        return payload_json


    def public_info(self, info):
        payload = self.package_info(info)
        print(payload)
        self.__client.publish(self.topic_upload_info, payload)


'''    def on_disconnect(self, client, userdata, rc):
        print("Lose connection with MQTT Server, error code "+ str(rc))
        print("Try to reconnect...")
        client.reconnect()'''
    
