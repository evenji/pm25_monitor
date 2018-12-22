#!/usr/bin/env python3
# -*- coding: utf-8 -*

import serial  
import time  
import sys
import json
from SensorInfo import PTInfo


class BaseSensor(object):
    def __init__(self):
        pass
    
    def sensor_init(self):
        print("this is sensor init")

    def data_get(self):
        pass

    def config_set(self):
        pass

    def sensor_reset(self):
        pass

class PTSensor(BaseSensor):

    DATA_PREFIX_1st = 0x42
    DATA_PREFIX_2nd = 0x4d

    def sensor_init(self):
        super().sensor_init()
        print("this is PM2.5 init")
        #self.__ser = serial.Serial("/dev/ttyAMA0", 115200)
        self.__ser = serial.Serial("/dev/ttyUSB0", 9600)
        if self.__ser.isOpen():
            print("open success")
        else:
            print("open success")

    def data_check_vaild(self,data):
        check_sum = data[-2] << 8 | data[-1]
        print("check_sum = ", check_sum)
        new_check_sum = 0
        new_data = data[:-2]
        print("new_data = ", len(new_data))
        for b in new_data:
            new_check_sum = new_check_sum + b
        new_check_sum = new_check_sum + self.DATA_PREFIX_1st + self.DATA_PREFIX_2nd
        print("new_check_sum = ", new_check_sum)
        if new_check_sum == check_sum:
            return True
        else:
            return False

    def bytes2Int(self, byte2):
        int_new = byte2[0] << 8 | byte2[1]
        return int_new

    def data_parser(self, data):
        pm1_0_sp = self.bytes2Int(data[2:4])
        pm2_5_sp = self.bytes2Int(data[4:6])
        pm10_sp  = self.bytes2Int(data[6:8])
        pm1_0_ae = self.bytes2Int(data[8:10])
        pm2_5_ae = self.bytes2Int(data[10:12])
        pm10_ae  = self.bytes2Int(data[12:14])
        p03um    = self.bytes2Int(data[14:16])
        p05um    = self.bytes2Int(data[16:18])
        p10um    = self.bytes2Int(data[18:20])
        p25um    = self.bytes2Int(data[20:22])
        temp     = self.bytes2Int(data[22:24])
        humi     = self.bytes2Int(data[24:26])
        newInfo = PTInfo()
        newInfo.info_set(pm1_0_sp, pm2_5_sp, pm10_sp, pm1_0_ae, pm2_5_ae, pm10_ae, p03um, p05um, p10um, p25um, temp, humi)
        #print(newInfo.get_info())
        in_json = json.dumps(newInfo.get_info())
        print(in_json)


    def data_get(self):
        super().data_get()
        while True:
            recv =self.__ser.read(1)
            if recv == b'B':
                recv =self.__ser.read(1)
                if recv == b'M':
                    print("get rest data")
                    length_recv =self.__ser.read(2)   # get data length
                    data_length = length_recv[0]<<8 | length_recv[1]
                    data_recv =self.__ser.read(data_length)   # get data length
                    new_data = length_recv + data_recv
                    if True == self.data_check_vaild(new_data) :
                        print("get valid data")
                        self.data_parser(new_data)
                    else:
                        print("get invalid data")
                else:
                    continue
            else:
                continue       
            # 清空接收缓冲区  
            #self.__ser.flushInput()  
            # 必要的软件延时  
            #time.sleep(0.1)  

 


    



if __name__ == '__main__':
    PM25 = PTSensor()
    PM25.sensor_init()
    PM25.data_get()

