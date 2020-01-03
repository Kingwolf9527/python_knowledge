# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/7 4:29

from multi_devices.multi_appium_sync import Multi_process_appium
from multi_devices.multi_devices_sync import Multi_devices
from multi_devices.check_port import Check_port
import time
import multiprocessing

class Multi_sync(object):

    def __init__(self):
        #初始化参数，调用检测端口的方法
        self.check_port = Check_port()
        #调用启动appium服务
        self.appium_server = Multi_process_appium()
        #调用启动设备的方法
        self.device_start = Multi_devices()
        #获取多台模拟器的udid
        self.devices_udid = self.device_start.devices_udids
        #获取多台模拟器的安卓版本
        # self.platformVersion = self.device_start.platformVersions

    def start_appium_action(self,host,port):
        """
        检测端口是否被占用，如果有，就释放；如果没有，就启动appium服务
        :param host:
        :param port:
        :return:
        """
        if self.check_port.check_ports(host,port):
            #调用启动appium服务的方法
            self.appium_server.appium_start(host,port)
            return True
        else:
            print('appium(port：%s) start failed' %port)
            return False

    def start_device_action(self,udid,port):
        """
        先检测appium服务启动是否成功，启动成功再启动设备，否则，释放被占用的端口
        :param host:
        :param port:
        :return:
        """
        host = '127.0.0.1'
        if self.start_appium_action(host,port):
            #调用启动设备的方法
            self.device_start.read_caps(udid,port)
            print('===========start device===============')
        else:
            #调用释放被占用端口的方法
            self.check_port.release_ports(port)
            print('============release ports=============')

    def start_appium_sync(self):
        """
        并发启动appium服务
        :param host:
        :param port:
        :return:
        """
        print('==========start appium sync============')
        #构建appium_desires进程组
        appium_desires = []

        #加载appium_desires进程组
        for i in range(len(self.devices_udid)):
            #设置host和port
            host = '127.0.0.1'
            port = 4723 + 2 * i
            #调用多进程方法
            appium_desired = multiprocessing.Process(target=self.start_appium_action,args=(host,port))
            appium_desires.append(appium_desired)

        #启动多进程
        for appium_desire in appium_desires:
            appium_desire.start()
        for appium_desire in appium_desires:
            appium_desire.join()

        #设置启动服务后，延时3秒(这个延时很重要，太短，服务启动失败；太长，导致check_ports方法再次调用，导致出错)
        time.sleep(3)

    def start_device_sync(self):
        """
        并发启动设备
        :param udid:
        :param port:
        :return:
        """
        print('=========start device sync============')
        #构建device_desires进程组
        device_desires = []

        #加载device_desires进程组
        for i in range(len(self.devices_udid)):
            port = 4723 + 2 * i
            #调用多进程方法
            device_desiresd = multiprocessing.Process(target=self.start_device_action,args=(self.devices_udid[i],port))
            device_desires.append(device_desiresd)

        #并发启动app
        for device_desire in device_desires:
            device_desire.start()
        for device_desire in device_desires:
            device_desire.join()

if __name__ == '__main__':
    dd = Multi_sync()
    dd.start_appium_sync()
    dd.start_device_sync()





