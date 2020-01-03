# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/5 5:56

from appium_learn.kyb_project_test.config.read_configparser import Config_paser
from appium import webdriver
from appium_learn.kyb_project_test.utils.common_logs import Common_log
import os

logger = Common_log(logger='driver').get_logger()

class Driver(object):

    def __init__(self):

        self.cf = Config_paser()

    def read_caps(self):

        #读取capability配置
        desired_caps = {}
        desired_caps['platformName'] = self.cf.get_selectoin('capability','platformName')
        desired_caps['platformVersion'] = self.cf.get_selectoin('capability','platformVersion')
        desired_caps['deviceName'] = self.cf.get_selectoin('capability','deviceName')
        # desired_caps['udid'] = self.cf.get_selectoin('capability','udid')  #米8用的
        desired_caps['appPackage'] = self.cf.get_selectoin('capability','appPackage')
        desired_caps['appActivity'] = self.cf.get_selectoin('capability','appActivity')
        desired_caps['newCommandTimeout'] = self.cf.get_selectoin('capability','newCommandTimeout')
        desired_caps['noReset'] = self.cf.get_selectoin('capability','noReset')
        #app的apk包
        app_apk_dir = os.path.dirname(os.path.dirname(__file__)) + '/app/'
        app_apk_name = os.path.join(app_apk_dir,self.cf.get_selectoin('capability','app'))
        desired_caps['app'] = app_apk_name

        logger.info('.................start app .............')
        #建立APP连接
        self.driver = webdriver.Remote('http://' + str(self.cf.get_selectoin('capability','ip')) \
                                       + ':' + str(self.cf.get_selectoin('capability','port')) + '/wd/hub',desired_caps)
        return self.driver


if __name__ == '__main__':
    dd = Driver()
    dd.read_caps()