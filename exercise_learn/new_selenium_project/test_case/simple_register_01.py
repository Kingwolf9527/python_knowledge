# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/28 2:31

import sys
sys.path.append(r'F:\GitExtensions_python\project_spider\exercise_learn\new_selenium_project')

from businessview.register_business import Register_Business
from util.browser_driver_test import driver_init
import unittest
import os

class Register_test(unittest.TestCase):

    # def __init__(self,driver):
    #
    #     self.reg = Register_Business(driver)

    def setUp(self):
        self.driver = driver_init(0)
        self.reg = Register_Business(self.driver)

    def tearDown(self):
        # # 捕获异常
        # for method_name, error in self._outcome.errors:
        #     if error:
        #         case_name = self._testMethodName
        #         #截图保存位置
        #         image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
        #         file_name_path = os.path.join(image_path,case_name)
        #         image_name = file_name_path + '.png'
        #         self.driver.get_screenshot_as_file(image_name)
        self.driver.close()

    def test_register_email_error(self):
        """
        本条case，验证邮箱错误
        :return:
        """
        email_error_ = self.reg.register_email_error('111@163.com','test01','test01','415263')
        self.assertFalse(email_error_,'邮箱符合要求，本条case执行失败！')
        # if email_error_ == True:
        #     print('邮箱符合要求，本条case执行失败！')

    def test_register_name_error(self):
        """
        本条case，验证用户名错误
        :return:
        """
        name_error_ = self.reg.register_name_error('118511@163.com','test01','test01','415263')
        self.assertFalse(name_error_,'用户名符合要求，本条case执行失败')
        # if name_error_ == True:
        #     print('用户名符合要求，本条case执行失败！')

    def test_register_password_error(self):
        """
        本条case，验证密码错误
        :return:
        """
        password_error_ = self.reg.register_password_error('11175111@163.com','test01','test010','415263')
        self.assertFalse(password_error_,'密码符合要求，本条case执行失败！')
        # if password_error_ == True:
        #     print('密码符合要求，本条case执行失败！')

    def test_register_text_captcha_error(self):
        """
        本条case，验证验证码错误
        :return:
        """
        text_captcha_error_ = self.reg.register_text_captcha_error('115711111111@163.com','test01','te44st01','415263')
        self.assertFalse(text_captcha_error_,'验证码输入正确，本条case执行失败')
        # if text_captcha_error_ == True:
        #     print('验证码输入正确，本条case执行失败！')

    def test_register_success(self):
        """
        本条case，验证注册成功
        :return:
        """
        success_ = self.reg.common_send_keys('test125284@163.com','test963','test963','dgy123')
        self.assertFalse(success_,'注册成功！')
        # if self.reg.register_success() == True:
        #     print('注册成功！')



if __name__ == '__main__':
    # driver = driver_init(0)
    # simple_case = Register_test(driver)
    # simple_case.test_register_email_error()
    # simple_case.test_register_name_error()
    # simple_case.test_register_password_error()
    # simple_case.test_register_text_captcha_error()
    # simple_case.test_register_success()
    unittest.main()

