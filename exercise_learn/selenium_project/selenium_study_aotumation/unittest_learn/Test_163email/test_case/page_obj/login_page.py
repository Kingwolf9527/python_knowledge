# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/31 17:20

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from test_case.page_obj.base import Page

class Login(Page):
    '''

    用户登录页面

    '''
    #切换登录iframe
    iframe_loc = (By.XPATH,'//div[@id="panel-163"]/iframe')
    def iframe_switch_login(self):
        ifarme_switch = self.find_element(*self.iframe_loc)
        self.driver.switch_to.iframe(ifarme_switch)

    #定位账号，密码，登录按钮
    login_account_loc = (By.NAME,'email')
    login_password_loc = (By.NAME,'password')
    login_button_loc = (By.ID,'dologin')

    #登录账号
    def login_useraccount(self,useraccount):
        self.find_element(*self.login_account_loc).send_keys(useraccount)

    #登录密码
    def login_userpassword(self,userpassword):

        self.find_element(*self.login_password_loc).send_keys(userpassword)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()


    #定义统一登录入口
    def user_login(self,useraccount='useraccount',userpassword='6666'):
        '''
        获取的用户名密码登陆
        :param useraccount:
        :param userpassword:
        :return:
        '''
        self.open()
        self.iframe_switch_login()
        self.login_useraccount(useraccount)
        self.login_userpassword(userpassword)
        self.login_button()
        time.sleep(2)

    #定义相关提示
    user_error_tip_loc = (By.XPATH,'//div[@class="m-nerror err_email"]/div[@class="ferrorhead"]')
    pwd_error_tip_loc = (By.XPATH,'//div[@class="m-nerror err_password"]/div[@class="ferrorhead"]')
    # user_login_success_tip_loc = (By.ID,'spnUid')   #需要切换iframe到top层，才能重新定位

    #用户名错误提示
    def user_error_tip(self):
        return self.find_element(*self.user_error_tip_loc).text()

    #密码错误提示
    def pwd_error_tip(self):
        return self.find_element(*self.pwd_error_tip_loc).text()

    #登录成功用户名(通过判断登录成功后，进入个人中心的昵称是否一致来判断登录是否成功)
    # def user_login_success_tip(self):
    #     return self.find_element(*self.user_login_success_tip_loc).text()



