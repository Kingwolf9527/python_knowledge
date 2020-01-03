# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/3 4:13

from appium_learn.kyb_project_test.config.read_configparser import Config_paser
from appium import webdriver
from appium_learn.kyb_project_test.utils.common_logs import Common_log
import os
import time

logger = Common_log(logger='multi_devices').get_logger()

class Driver(object):

    def __init__(self):

        self.cf = Config_paser()

    def read_caps(self,udid,port):

        #读取capability配置
        desired_caps = {}
        desired_caps['platformName'] = self.cf.get_selectoin('capability','platformName')
        desired_caps['platformVersion'] = self.cf.get_selectoin('capability','platformVersion')
        desired_caps['deviceName'] = self.cf.get_selectoin('capability','deviceName')   #设置了udid，这里任意
        desired_caps['udid'] = udid
        desired_caps['appPackage'] = self.cf.get_selectoin('capability','appPackage')
        desired_caps['appActivity'] = self.cf.get_selectoin('capability','appActivity')
        desired_caps['newCommandTimeout'] = self.cf.get_selectoin('capability','newCommandTimeout')
        desired_caps['noReset'] = self.cf.get_selectoin('capability','noReset')
        #app的apk包
        app_apk_dir = os.path.dirname(os.path.dirname(__file__)) + '/app/'
        app_apk_name = os.path.join(app_apk_dir,self.cf.get_selectoin('capability','app'))
        desired_caps['app'] = app_apk_name

        logger.info('.................start app .............')
        logger.info('appium port %s start,device(%s) run at %s' %(port,udid,time.ctime()))
        #建立APP连接
        self.driver = webdriver.Remote('http://' + str(self.cf.get_selectoin('capability','ip')) \
                                       + ':' + str(port) + '/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)
        return self.driver


if __name__ == '__main__':
    #设置不同模拟器的udid
    devices_udids = ['127.0.0.1:62001', '127.0.0.1:62025']
    dd = Driver()
    dd.read_caps(udid=devices_udids[0],port=4723)
    dd.read_caps(udid=devices_udids[1],port=4725)
