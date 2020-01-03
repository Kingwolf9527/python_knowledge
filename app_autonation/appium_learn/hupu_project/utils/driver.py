# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/6/5 20:32

import os
from hupu_project.utils.read_config import Read_config
from appium import webdriver
import time

class Driver(object):

    def __init__(self):

        self.cf = Read_config(file='hupu_app_config.ini')

    def read_caps(self):

        #读取配置信息
        desire_caps = {}
        desire_caps['platformName'] = self.cf.get_selection('capability_app','platformName')
        desire_caps['platformVersion'] = self.cf.get_selection('capability_app','platformVersion')
        desire_caps['deviceName'] = self.cf.get_selection('capability_app','deviceName')
        desire_caps['udid'] = self.cf.get_selection('capability_app','udid')
        desire_caps['appPackage'] = self.cf.get_selection('capability_app','appPackage')
        desire_caps['appActivity'] = self.cf.get_selection('capability_app','appActivity')
        desire_caps['newCommandTimeout'] = self.cf.get_selection('capability_app','newCommandTimeout')
        desire_caps['noReset'] = self.cf.get_selection('capability_app','noReset')
        desire_caps['ip'] = self.cf.get_selection('capability_app','ip')
        #app文件这里需要处理一下
        path = os.path.dirname(os.path.dirname(__file__))
        file = os.path.join(path,'app',self.cf.get_selection('capability_app','app'))
        desire_caps['app'] = file
        desire_caps['port'] = self.cf.get_selection('capability_app','port')

        driver = webdriver.Remote('http://' + self.cf.get_selection('capability_app','ip') \
                                  + ':' + str(self.cf.get_selection('capability_app','port')) + '/wd/hub',desire_caps)
        time.sleep(5)
        return driver



if __name__ == '__main__':
    d = Driver()
    d.read_caps()