# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/28 1:06

from new_selenium_project.PageObject.businessview.register_ele import Register_ele
from selenium.common.exceptions import NoSuchElementException
from new_selenium_project.util.common_log import Common_Logs

#实例化logger
log_name = Common_Logs(logger='register_handle')
logger = log_name.get_logger()

class RegisterHandle(object):

    def __init__(self,driver):

        self.register_e = Register_ele(driver)

    def send_email(self,email):
        """
        发送所需要注册的邮箱
        :param email:
        :return:
        """
        self.register_e.get_email_ele().send_keys(email)

    def send_name(self,name):
        """
        发送所需要注册的用户名
        :param name:
        :return:
        """
        self.register_e.get_name_ele().send_keys(name)

    def send_password(self,password):
        """
        发送所需要注册的密码
        :param password:
        :return:
        """
        self.register_e.get_password_ele().send_keys(password)

    def send_text_captcha(self,text_captcha):
        """
        发送所需要注册的验证码
        :param text_captcha:
        :return:
        """
        self.register_e.get_text_captcha_ele().send_keys(text_captcha)

    def get_user_error_text(self,type_info,error_text):
        """
        获取错误文字信息：观察输入是否符合要求，不符合要求，红色提示文字
        :param type_info: 用来区分不同错误类型的
        :param error_info:    错误提示的文字信息
        :return:
        """
        if type_info == 'user_email_error':
            logger.info('------ assertcode is: user_email_error    ------')
            try:
                text_info = self.register_e.get_email_error_ele()   #这个需要存在value属性才能这样取值，否则，建议采用text
            except NoSuchElementException:
                logger.error('------  the element:  user_email_error is not found      ------')
                text = ''
            else:
                text = text_info.text
                logger.info('------ text is:    %s    ------' %text)

        elif type_info == 'user_nickname_error':
            logger.info('------ assertcode is: user_nickname_error    ------')
            try:
                text_info = self.register_e.get_name_error_ele()
            except NoSuchElementException:
                logger.error('------  the element:  user_nickname_error is not found      ------')
                text = ''
            else:
                text = text_info.text
                logger.info('------ text is:    %s    ------' %text)

        elif type_info == 'user_password_error':
            logger.info('------ assertcode is: user_password_error    ------')
            try:
                text_info = self.register_e.get_password_error_ele()
            except NoSuchElementException:
                logger.error('------  the element:  user_password_error is not found      ------')
                text = ''
            else:
                text = text_info.text
                logger.info('------ text is:    %s    ------' %text)

        else:
            logger.info('------ assertcode is: captcha_code-error    ------')
            try:
                text_info = self.register_e.get_text_captcha_error_ele()
            except NoSuchElementException:
                logger.error('------  the element:  captcha_code-error is not found      ------')
                text = ''
            else:
                text = text_info.text
                logger.info('------ text is:    %s    ------' %text)

        return text

    def click_register_button(self):
        """
        点击注册按钮
        :param register_button:
        :return:
        """
        self.register_e.get_register_button_ele().click()
        logger.info('------ click the register_button    ------')

    def get_register_button_text(self):
        """
        用于简单校验，注册是否成功
        :return:
        """
        button_text = self.register_e.get_register_button_ele().text
        return button_text