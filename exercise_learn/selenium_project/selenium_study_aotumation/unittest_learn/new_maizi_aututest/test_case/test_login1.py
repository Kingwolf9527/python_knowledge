# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/5 7:37

import unittest
from new_maizi_aututest.utils.log import LogDetail
from new_maizi_aututest.utils.jump_login import Jump_login
import time
from new_maizi_aututest.utils.Unit_common import Mytest
from new_maizi_aututest.page_object.error_tips import Error_tip


class login_test(Mytest):

    def test_a(self):
        """用户名格式错误"""
        #jump_login实例
        t1 = Jump_login(self.driver)
        t1.jump()
        t1.login('1372622997','922521dfxs')
        #调用错误信息的方法，截图和比较
        error_text = Error_tip(self.driver)
        text = error_text.error_text()
        self.assertEqual(text,'该账号格式不正确')

    def test_b(self):
        '''用户名为空'''
        # jump_login实例
        t2 = Jump_login(self.driver)
        t2.jump()
        t2.login('', '922521dfxs')
        # 调用错误信息的方法，截图和比较
        error_text2 = Error_tip(self.driver)
        text2 = error_text2.error_text()
        self.assertEqual(text2, '账号不能为空')

    def test_c(self):
        '''用户名正确，密码为空'''
        # jump_login实例
        t3 = Jump_login(self.driver)
        t3.jump()
        t3.login('13726229967','')
        # 调用错误信息的方法，截图和比较
        error_text3 = Error_tip(self.driver)
        text3 = error_text3.error_text()
        self.assertEqual(text3, '密码不能为空')

    def test_d(self):
        '''用户名正确，密码错误'''
        # jump_login实例
        t4 = Jump_login(self.driver)
        t4.jump()
        t4.login('13726229997', '8763873')
        # 调用错误信息的方法，截图和比较
        error_text4 = Error_tip(self.driver)
        text4 = error_text4.error_text()
        self.assertEqual(text4, '账号或者密码错误，请重新输入')

if __name__ == '__main__':
    unittest.main()
