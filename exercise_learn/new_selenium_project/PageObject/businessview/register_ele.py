# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/28 1:22

from new_selenium_project.PageObject.baseview.element_processing import Elemnet

class Register_ele(object):

    def __init__(self,driver):

        self.get_ele = Elemnet(driver)

    def get_email_ele(self):
        """
        获取配置文件，注册邮箱元素
        :return:
        """
        email_ele = self.get_ele.ele_processing('RegisterElement','user_email')
        return email_ele

    def get_name_ele(self):
        """
        获取配置文件，注册用户名元素
        :return:
        """
        name_ele = self.get_ele.ele_processing('RegisterElement','user_nickname')
        return name_ele

    def get_password_ele(self):
        """
        获取配置文件，注册密码元素
        :return:
        """
        password_ele = self.get_ele.ele_processing('RegisterElement','user_password')
        return password_ele

    def get_text_captcha_ele(self):
        """
        获取配置文件，注册验证码元素
        :return:
        """
        text_captcha_ele = self.get_ele.ele_processing('RegisterElement','text_captcha')
        return text_captcha_ele

    def get_register_button_ele(self):
        """
        获取配置文件，注册登录按钮元素
        :return:
        """
        register_button_ele = self.get_ele.ele_processing('RegisterElement','register_button')
        return register_button_ele

    def get_email_error_ele(self):
        """
        获取配置文件，注册邮箱错误元素
        :return:
        """
        email_error_ele = self.get_ele.ele_processing('RegisterElement','user_email_error')
        return email_error_ele

    def get_name_error_ele(self):
        """
        获取配置文件，注册用户名错误元素
        :return:
        """
        name_error_ele = self.get_ele.ele_processing('RegisterElement','user_nickname_error')
        return name_error_ele

    def get_password_error_ele(self):
        """
        获取配置文件，注册密码错误元素
        :return:
        """
        password_error_ele = self.get_ele.ele_processing('RegisterElement','user_password_error')
        return password_error_ele

    def get_text_captcha_error_ele(self):
        """
        获取配置文件，注册验证码错误元素
        :return:
        """
        text_captcha_error_ele = self.get_ele.ele_processing('RegisterElement','captcha_code-error')
        return text_captcha_error_ele




