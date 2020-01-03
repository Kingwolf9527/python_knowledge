# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/7 4:16

import time
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium_learn.kyb_project_test.utils.common_logs import Common_log
from appium_learn.kyb_project_test.utils.driver import Driver
from appium_learn.kyb_project_test.page_object.baseView.common_view import Common_view

logger = Common_log(logger='login_check').get_logger()

class Common_login(Common_view):

    #账号密码，登录按钮
    username_loc = (By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_loc = (By.ID,'com.tal.kaoyan:id/login_password_edittext')
    login_botton_loc = (By.ID,'com.tal.kaoyan:id/login_login_btn')

    #下线通知提醒
    comit_tip = (By.ID,'com.tal.kaoyan:id/tip_commit')

    #个人中心和昵称
    myself_button = (By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    nickname = (By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    #退出登录
    setting_button = (By.ID,'com.tal.kaoyan:id/myapptitle_RightButtonWraper')
    logut_button = (By.ID,'com.tal.kaoyan:id/setting_logout_text')
    logut_commit_button = (By.ID,'com.tal.kaoyan:id/tip_commit')


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
        time.sleep(2)

        logger.info('=======================login finish=======================')

    def commit_tip_alert(self):
        """
        检测账号登录后，是否有下线通知提醒
        :return:
        """
        logger.info('========================check commit tip alert=========================')
        try:
            ele = self.driver.find_element(*self.comit_tip)
        except NoSuchElementException:
            logger.info('===========================No alert================================')
            pass
        else:
            logger.info('=============================click commit button=======================================')
            ele.click()

    def login_status_check(self):
        """
        检查登录状态
        :return:
        """
        logger.info('===========================login_status_check==============================')
        #调用登陆后，是否出现下线通知提醒
        self.commit_tip_alert()
        time.sleep(5)
        try:
            self.driver.find_element(*self.myself_button).click()
            # os.system('adb shell input tap 981 2082')   #米8定位
            time.sleep(3)
            self.driver.find_element(*self.nickname)
        except NoSuchElementException:
            logger.error('===========================login failed===============================')
            self.get_screenshot_image('Login Failed')
            return False
        else:
            logger.info('=============================login success=============================')
            self.get_screenshot_image('Login success')
            #退出登录
            self.logut()
            return True

    def logut(self):
        """
        退出登录
        :return:
        """
        logger.info('==================================logut=====================================')
        self.driver.find_element(*self.setting_button).click()
        time.sleep(1)
        self.driver.find_element(*self.logut_button).click()
        time.sleep(1)
        self.driver.find_element(*self.logut_commit_button).click()


if __name__ == '__main__':
    driver = Driver().read_caps()
    login = Common_login(driver)
    login.login_check(username='kingwolfbook14',password='922521dfxs')
    login.login_status_check()
