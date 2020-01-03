# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/24 3:30

from selenium.webdriver.common.by import By
import time
from .base_page import Page

class Login(Page):

    # def __init__(self):
    #     # 弹窗登录框以及退出登录
    #     self.login_window_loc = (By.LINK_TEXT, '登录')
    #     self.logout_loc = (By.LINK_TEXT,'退出')
    #     #账号密码以及登录按钮
    #     self.account_loc = (By.ID,'id_account_l')
    #     self.password_loc = (By.ID,'id_password_l')
    #     self.button_loc = (By.ID,'login_btn')
    #     #错误提示
    #     self.error_text = (By.ID,'login-form-tips')
    #     #成功的依据
    #     self.success_text = (By.XPATH,'//div[contains(@class,"personalCmainR")]/p')


    def login_window(self):
        # 弹窗登录框
        self.login_window_loc = (By.LINK_TEXT, '登录')
        self.find_element(*self.login_window_loc).click()

    def logout_loc(self):
        #退出登录
        self.logout_loc = (By.LINK_TEXT, '退出')
        self.find_element(*self.logout_loc).click()

    def login_account(self,account):
        # 登录账号
        self.account_loc = (By.ID, 'id_account_l')
        self.find_element(*self.account_loc).clear()
        self.find_element(*self.account_loc).send_keys(account)

    def login_password(self,password):
        #登录密码
        self.password_loc = (By.ID,'id_password_l')
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def login_button(self):
        # 登录按钮
        self.button_loc = (By.ID,'login_btn')
        self.find_element(*self.button_loc).click()

    def error_text(self):
        #错误提示
        self.error_text = (By.ID,'login-form-tips')
        error_text = self.find_element(*self.error_text).text()
        return error_text

    def success_text(self):
        # 成功的依据
        self.success_text = (By.XPATH,'//div[contains(@class,"personalCmainR")]/p')
        success_text = self.find_element(*self.success_text).text()
        return success_text

    #定义统一登录入口
    def user_login(self,account='111',password='11111'):

        self.login_window()
        self.login_account(account)
        self.login_password(password)
        self.login_button()
        time.sleep(2)