#!/usr/bin/env python3
# -*- coding: utf-8 -*
from PM25Sensor import PTSensor
from SensorInfo import PTInfo
from mqtt_client import Mqtt_Client
import json
import threading
import time
import sys

PM25 = None
mq_c = None
sys_config_file_path = "sys_config"
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

def sys_config_load():
    with open(sys_config_file_path,'r') as config_file:
        config = json.load(config_file)
    sampling_time = config['sampling_time']
    sensor_config = config['sensor_config']
    mqtt_config = config['mqtt_config']
    return sampling_time , sensor_config, mqtt_config


if __name__ == '__main__':
    sampling_time, sensor_config, mqtt_config = sys_config_load()
    PM25 = PTSensor(sensor_config)
    init_status = PM25.sensor_init()
    if False == init_status:
        print("Sensor Init failed")
        sys.exit(1)
    mq_c = Mqtt_Client(mqtt_config, start_timer)
    mq_c.connect_server()
    sys.exit(0)
    


