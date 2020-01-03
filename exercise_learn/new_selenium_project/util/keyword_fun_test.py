# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/12 3:21


import time
import os
from selenium import webdriver
from baseview.element_processing import Elemnet


class KeyWord_function(object):

    def __init__(self,browser):

        self.browser = browser

    def driver_init(self):
        """
        打开浏览器
        :param browser:
        :return:
        """

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

        elif self.browser == 'firefox':

            """
            
                火狐浏览器的设置
            
            """
            # #设置火狐浏览器驱动路径
            driver_path = os.path.dirname(os.path.dirname(__file__)) + '/browser_driver/geckodriver.exe'

            self.driver = webdriver.Firefox(executable_path=driver_path)

        else:

            """
            
                edge浏览器的设置
            
            """
            # #设置edge浏览器驱动路径
            driver_path = os.path.dirname(os.path.dirname(__file__)) + '/browser_driver/MicrosoftWebDriver.exe'
            self.driver = webdriver.Edge(executable_path=driver_path)

        return self.driver


    def get_init_url(self,url):
        """
        输入url地址
        :param browser:
        :param url:
        :return:
        """
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def get_element(self,selection,key):
        """
        定位元素
        :param selection:
        :param key:
        :return:
        """
        get_ele = Elemnet(self.driver)
        element = get_ele.ele_processing(selection,key)
        return element

    def send_keys_element(self,selection,key,value):
        """
        输入元素
        :param selection:
        :param key:
        :param value:
        :return:
        """
        element = self.get_element(selection,key)
        element.send_keys(value)

    def click_element(self,selection,key):
        """
        点击元素
        :param selection:
        :param key:
        :return:
        """
        self.get_element(selection,key).click()

    def sleep_time(self):
        """
        延时处理
        :return:
        """
        time.sleep(3)

    def close_driver(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.close()


if __name__ == '__main__':

    dd = KeyWord_function('chrome')
    dd.driver_init()
    dd.get_init_url("http://www.5itest.cn/register?goto=/")


