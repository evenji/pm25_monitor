#!/usr/bin/env python3
# -*- coding: utf-8 -*
class SensorInfo(object):
    pass

class PTInfo(SensorInfo):

    __info = {'pm1_0_sp':0, 'pm2_5_sp':0, 'pm10_sp':0, 'pm1_0_ae':0, 'pm2_5_ae':0, 'pm10_ae':0, 'p03um':0, 'p05um':0, 'p10um':0, 'p25um':0, 'temp':0, 'humi':0}

    def __init__(self):
        pass
    def info_set(self, pm1_0_sp, pm2_5_sp, pm10_sp, pm1_0_ae, pm2_5_ae, pm10_ae, p03um, p05um, p10um, p25um, temp, humi):
        self.__info['pm1_0_sp'] = pm1_0_sp
        self.__info['pm2_5_sp'] = pm2_5_sp
        self.__info['pm10_sp'] = pm10_sp
        self.__info['pm1_0_ae'] = pm1_0_ae
        self.__info['pm2_5_ae'] = pm2_5_ae
        self.__info['pm10_ae'] = pm10_ae
        self.__info['p03um'] = p03um
        self.__info['p05um'] = p05um
        self.__info['p10um'] = p10um
        self.__info['p25um'] = p25um
        self.__info['temp'] = temp
        self.__info['humi'] = humi



    def print_info(self):
        print("")
        #print("pm1_0_sp = %d, pm2_5_sp = %d, pm10_sp = %d, pm1_0_ae = %d, pm2_5_ae = %d, pm10_ae = %d, p03um = %d, p05um = %d, p10um = %d, p25um = %d, temp = %d, humi = %d", % (self.__pm1_0_sp, self.__pm2_5_sp, self.__pm10_sp, self.__pm1_0_ae, self.__pm2_5_ae, self.__pm10_ae, self.__p03um, self.__p05um, self.__p10um, self.__p25um, self.__temp, self.__humi))
        #print("pm1_0_sp = %d" %(self.__pm1_0_sp))
        #print("pm2_5_sp = %d" %(self.__pm2_5_sp))
        #print("pm10_sp = %d" %(self.__pm10_sp))
        #print("pm1_0_ae = %d" %(self.__pm1_0_ae))
        print("pm2_5_ae = %d" %(self.__info['pm2_5_ae']))
        #print("pm10_ae = %d" %(self.__pm10_ae))
        #print("p03um = %d" %(self.__p03um))
        #print("p05um = %d" %(self.__p05um))
        #print("p10um = %d" %(self.__p10um))
        #print("p25um = %d" %(self.__p25um))
        print("temp = %d" %(self.__info['temp']))
        print("humi = %d" %(self.__info['humi']))
        print("")

    def get_info(self):
        return self.__info

