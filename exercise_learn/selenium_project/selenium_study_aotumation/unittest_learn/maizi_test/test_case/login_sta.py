# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/24 4:04

import unittest
from maizi_test.page_object.login_page import Login
from maizi_test.util import unit_common

class Login_maizi(unit_common.Mytest):

    #测试用户登录
    def user_login_verify(self,account='',password=''):
        Login(self.driver).user_login(account,password)

    def test_login1(self):
        '''账号密码为空，登录'''
        self.user_login_verify()
        d = Login(self.driver)
        self.assertEqual(d.error_text,'账号不能为空')

    def test_login2(self):
        '''账号正确，密码为空'''
        self.user_login_verify(account='13726229967')
        d = Login(self.driver)
        self.assertEqual(d.error_text,'密码不能为空')

    def test_login3(self):
        '''用户名错误格式，密码随意'''
        self.user_login_verify(account='15245')
        d = Login(self.driver)
        self.assertEqual(d.error_text,'该账户格式不正确')

    def test_login4(self):
        '''账号正确，密码错误'''
        self.user_login_verify(account='13726229967',password='525445')
        d = Login(self.driver)
        self.assertEqual(d.error_text,'账号或者密码错误，请重新输入')

    def test_login5(self):
        '''账号，密码正确'''
        self.user_login_verify(account='13726229967',password='922521dfxs')
        d = Login(self.driver)
        self.assertEqual(d.success_text,'已报名课程')

if __name__ == '__main__':
    unittest.main()