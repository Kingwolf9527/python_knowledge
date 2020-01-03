# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/21 1:18

from appium_learn.capability_simple import NoSuchElementException,driver,check_skipbtn

class Login(object):

    def __init__(self):
        self.driver = driver

    #正常的登录页面(首次登录的场景)
    def login(self):
        #account element
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('kingwolfbook14')
        self.driver.implicitly_wait(2)
        #password element
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').clear()
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('922521dfxs')
        self.driver.implicitly_wait(2)
        #login_button element
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
        self.driver.implicitly_wait(1)

    #非首次登录的用户场景
    def not_first_login(self):
        try:
            # self.driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
            self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tal.kaoyan:id/mainactivity_button_mysefl")')
        except NoSuchElementException:
            self.login()
        else:
            #myself element
            self.driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
            # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tal.kaoyan:id/mainactivity_button_mysefl")').click()
            self.driver.implicitly_wait(2)
            #next login_button
            self.driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
            self.driver.implicitly_wait(2)
            self.login()

if __name__ == '__main__':
    dd = Login()
    dd.not_first_login()
