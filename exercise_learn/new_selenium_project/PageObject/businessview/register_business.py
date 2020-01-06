# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/28 1:04

from new_selenium_project.PageObject.businessview.register_handle import RegisterHandle
from new_selenium_project.util.common_log import Common_Logs


#实例化logger
log_name = Common_Logs(logger='register_business')
logger = log_name.get_logger()

class Register_Business(object):

    def __init__(self,driver):

        self.register = RegisterHandle(driver)

    def common_send_keys(self,email,name,password,text_captcha):
        """
        通用的发送注册的相关信息，包括：邮箱，用户名，密码，验证码
        :param email:
        :param name:
        :param password:
        :param code:
        :return:
        """
        self.register.send_email(email)
        self.register.send_name(name)
        self.register.send_password(password)
        self.register.send_text_captcha(text_captcha)
        logger.info('----- send_keys is : %s %s %s %s' %(email,name,password,text_captcha))


    def register_success(self):
        """
        简单校验注册是否成功(注册成功，注册按钮不会存在了)
        :return:
        """
        button_text_info = self.register.get_register_button_text()
        if button_text_info == None:
            logger.info('------  the result is True   ------')

            return True

        else:
            logger.info('------  the result is False   ------')

            return False

    def register_fun(self,email,name,password,text_captcha,assertcode,asserttext):
        """
        作为主函数，简化流程
        :param email:
        :param name:
        :param password:
        :param text_captcha:
        :param assertcode:
        :param asserttext:
        :return:
        """
        self.common_send_keys(email,name,password,text_captcha)
        error_info = self.register.get_user_error_text(assertcode,asserttext)
        logger.info('----   check the assertcode is: %s ,asserttext is: %s' %(assertcode,asserttext))

        if error_info == asserttext:
            logger.info('------  the error_info is True  ------')
            return True
        else:
            logger.info('------  the  error_info is False   ------')
            return False



    def register_email_error(self,email,name,password,text_captcha):
        self.common_send_keys(email,name,password,text_captcha)
        error_info_text = self.register.get_user_error_text(type_info='email_error',error_text='请输入有效的电子邮件地址')
        #如果获取不到该元素，校验失败，邮箱符合要求
        if error_info_text == None:
            # print('邮箱校验失败！')
            return True
        else:
            return False

    def register_name_error(self,email,name,password,text_captcha):
        self.common_send_keys(email,name,password,text_captcha)
        error_info_text = self.register.get_user_error_text(type_info='name_error',error_text='字符长度必须大于等于4，一个中文字算2个字符')
        #如果获取不到该元素，校验失败，用户名符合要求
        if error_info_text == None:
            # print('用户名校验失败！')
            return True
        else:
            return False

    def register_password_error(self,email,name,password,text_captcha):
        self.common_send_keys(email,name,password,text_captcha)
        error_info_text = self.register.get_user_error_text(type_info='password_error',error_text='最少需要输入 5 个字符')
        #如果获取不到该元素，校验失败，密码符合要求
        if error_info_text == None:
            # print('密码校验失败！')
            return True
        else:
            return False

    def register_text_captcha_error(self,email,name,password,text_captcha):
        self.common_send_keys(email,name,password,text_captcha)
        error_info_text = self.register.get_user_error_text(type_info='text_captcha_error',error_text='验证码错误')
        #如果获取不到该元素，校验失败，验证码正确
        if error_info_text == None:
            # print('验证码校验失败！')
            return True
        else:
            return False
