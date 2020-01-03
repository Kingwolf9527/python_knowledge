# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/1 2:57

import time
import unittest
import random
from test_case.page_obj.login_page import Login
from test_case.util import myunit,screenshot_img
from test_case.util.driver import browser

class LoginTest(myunit.Mytest):
    '''163邮箱登录'''

    def __init__(self):
        self.driver = browser()


    #测试用户登录
    def user_login_verify(self,useraccount='',userpassword=''):
        Login(self.driver).iframe_switch_login()


    def test_login1(self):
        '''用户名，密码为空登录'''
        self.user_login_verify()
        k = Login(self.driver)
        self.assertEqual(k.user_error_tip(),'账号不能为空')
        self.assertEqual(k.pwd_error_tip(),'密码不能为空')
        screenshot_img.insert_img(self.driver,'user_pwd_empty.jpg')

    def test_login2(self):
        '''用户名正确，密码为空登录'''
        self.user_login_verify(useraccount='lccr777@163.com')
        k = Login(self.driver)
        self.assertEqual(k.pwd_error_tip(),'密码不能为空')
        screenshot_img.insert_img(self.driver,'pwd_empty.jpg')

    def test_login3(self):
        '''用户名为空，密码正确'''
        self.user_login_verify(userpassword='922521dfxscr7')
        k = Login(self.driver)
        self.assertEqual(k.user_error_tip(),'账号不能为空')
        screenshot_img.insert_img(self.driver,'user_empty.jpg')

    def test_login4(self):
        '''用户名与密码不匹配'''
        self.user_login_verify(useraccount='lccr777@163.com',userpassword='1111111')
        k = Login(self.driver)
        self.assertEqual(k.pwd_error_tip(),'密码与账号不匹配')
        screenshot_img.insert_img(self.driver,'user_pwd_error.jpg')

    # def test_login5(self):
    #     '''用户名，密码正确'''
    #     self.user_login_verify(useraccount='lccr777@163.com',userpassword='922521dfxscr7')
    #     k = Login(self.driver)
    #     self.assertEqual(k.user_login_success_tip(),'lccr777@163.com')