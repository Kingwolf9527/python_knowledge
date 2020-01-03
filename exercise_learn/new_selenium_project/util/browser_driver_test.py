# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/12 3:21


import time
import os
from selenium import webdriver
from util.read_config import Read_Config
from util.common_log import Common_Logs

#实例化logger
log_name = Common_Logs(logger='browser_driver')
logger = log_name.get_logger()


class Webdriver_Browser(object):


    def __init__(self,selection,key):

        """
        打开浏览器
        :param selection:
        :param key:
        :return:
        """
        self.browser = Read_Config().get_value(selection,key)

        if self.browser == 'chrome':

            """
            
                谷歌浏览器的设置
            
            """
            #设置user-data-dir的路径
            new_options = webdriver.ChromeOptions()
            new_options.add_argument(r"user-data-dir=F:\data_profile")

            #设置谷歌浏览器的驱动路径
            driver_path = os.path.dirname(os.path.dirname(__file__)) + '/browser_driver/chromedriver.exe'

            self.driver = webdriver.Chrome(executable_path=driver_path,options=new_options)
            logger.info('-----------------open the browser:Chrome--------------------')

        elif self.browser == 'firefox':

            """
            
                火狐浏览器的设置
            
            """
            # #设置火狐浏览器驱动路径
            driver_path = os.path.dirname(os.path.dirname(__file__)) + '/browser_driver/geckodriver.exe'

            self.driver = webdriver.Firefox(executable_path=driver_path)
            logger.info('-----------------open the browser:Firefox--------------------')

        else:

            """
            
                edge浏览器的设置
            
            """
            # #设置edge浏览器驱动路径
            driver_path = os.path.dirname(os.path.dirname(__file__)) + '/browser_driver/MicrosoftWebDriver.exe'

            self.driver = webdriver.Edge(executable_path=driver_path)
            logger.info('-----------------open the browser:Edge--------------------')

    def get_init_url(self,selection,key):
        """
        输入url地址
        :param selection:
        :param key:
        :return:
        """
        self.register_url = Read_Config().get_value(selection,key)

        self.driver.get(self.register_url)
        logger.info('---------------------open the url: %s -----------------------' %self.register_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


if __name__ == '__main__':

    dd = Webdriver_Browser('Browser','chrome_browser')
    dd.get_init_url('Register_url','url')

