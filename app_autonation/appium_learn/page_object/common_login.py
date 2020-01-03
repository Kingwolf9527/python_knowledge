# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/7 4:16

from appium_learn.utils.driver import Driver
from appium_learn.utils.common_logs import Common_log
from appium_learn.page_object.common_view import Common_view
from selenium.webdriver.common.by import By
import time

logger = Common_log(logger='login_check').get_logger()

class Common_login(Common_view):

    username_loc = (By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_loc = (By.ID,'com.tal.kaoyan:id/login_password_edittext')
    login_botton_loc = (By.ID,'com.tal.kaoyan:id/login_login_btn')

    def login_check(self,username,password):

        time.sleep(3)
        #打开app时候，调用跳过按钮的检测方法
        self.check_skipbtn()

        #打印相关log
        logger.info('========================login==========================')
        logger.info('input username: %s' %username)
        #调用二次封装的元素定位方法
        self.driver.find_element(*self.username_loc).send_keys(username)

        logger.info('input password: %s' %password)
        self.driver.find_element(*self.password_loc).send_keys(password)

        logger.info('======================click login_button==================')
        self.driver.find_element(*self.login_botton_loc).click()

        logger.info('=======================login finish=======================')


if __name__ == '__main__':
    driver = Driver().read_caps()
    login = Common_login(driver)
    login.login_check(username='kingwolfbook14',password='922521dfxs')
