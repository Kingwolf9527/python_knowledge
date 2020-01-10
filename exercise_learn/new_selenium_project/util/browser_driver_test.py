# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/12 3:21


import os
from selenium import webdriver
from util.read_config import Read_Config
from util.common_log import Common_Logs

#实例化logger
log_name = Common_Logs(logger='browser_driver')
logger = log_name.get_logger()


class WebdriverBrowser(object):


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
            newOptions = webdriver.ChromeOptions()
            newOptions.add_argument(r"user-data-dir=F:\data_profile")

            #设置谷歌浏览器的驱动路径
            driverPath = os.path.dirname(os.path.dirname(__file__)) + '/browser_driver/chromedriver.exe'

            self.driver = webdriver.Chrome(executable_path=driverPath,options=newOptions)
            logger.info('-----------------open the browser:Chrome--------------------')

        elif self.browser == 'firefox':

            """
            
                火狐浏览器的设置
            
            """
            # #设置火狐浏览器驱动路径
            driverPath = os.path.dirname(os.path.dirname(__file__)) + '/browser_driver/geckodriver.exe'

            self.driver = webdriver.Firefox(executable_path=driverPath)
            logger.info('-----------------open the browser:Firefox--------------------')

        else:

            """
            
                edge浏览器的设置
            
            """
            # #设置edge浏览器驱动路径
            driverPath = os.path.dirname(os.path.dirname(__file__)) + '/browser_driver/MicrosoftWebDriver.exe'

            self.driver = webdriver.Edge(executable_path=driverPath)
            logger.info('-----------------open the browser:Edge--------------------')

    def getDriver(self):
        """
        返回driver
        :return:
        """
        return self.driver

    def getUrl(self,selection,key):
        """
        输入url地址
        :param selection:
        :param key:
        :return:
        """
        self.registerUrl = Read_Config().get_value(selection,key)

        self.getDriver().get(self.registerUrl)
        logger.info('---------------------open the url: %s -----------------------' %self.registerUrl)
        self.getDriver().implicitly_wait(10)
        self.getDriver().maximize_window()


if __name__ == '__main__':

    dd = WebdriverBrowser('Browser','chrome_browser')
    dd.getUrl('Register_url','url')

