#!/usr/bin/env python3
# -*- coding: utf-8 -*
from BaseSensor import PTSensor
from SensorInfo import PTInfo
from mqtt_client import Mqtt_Client
import json
import threading
import time

PM25 = None
mq_c = None
INFO_UPDATE_INTERVAL = 5

def data_upload():
    newinfo = PM25.data_get()
    mq_c.public_info(newinfo.get_info())

def start_timer():
    timer = threading.Timer(1, timer_loop)
    timer.start()

def timer_loop():
    data_upload()
    global timer
    timer = threading.Timer(INFO_UPDATE_INTERVAL, timer_loop)
    timer.start()


if __name__ == '__main__':
    PM25 = PTSensor()
    PM25.sensor_init()
    mq_c = Mqtt_Client(start_timer)
    mq_c.connect_server()


