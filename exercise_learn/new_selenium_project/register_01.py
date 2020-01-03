# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/14 3:02

import random
import time
from PIL import Image
from selenium.webdriver.common.by import By
from other_project.baidu_ai.baidu_ai_api_test import BaiduOCR
from util.browser_driver_test import driver_init


class Register(object):


    def __init__(self):

        self.driver = driver_init()
        # 邮箱
        self.email_ele = (By.ID, "register_email")
        # 用户名
        self.nickname_ele = (By.ID, "register_nickname")
        # 密码
        self.password_ele = (By.ID, "register_password")
        # 验证码输入框
        self.captcha_ele = (By.ID, "captcha_code")
        # 验证码图片
        self.captcha_pic = (By.ID, "getcode_num")
        # 登录框
        self.login_button_ele = (By.ID, "register-btn")


    def get_element(self,*loc):
        """
        元素基本定位
        :param by: 例如：By.ID
        :param selector: 定位的元素值
        :return:
        """

        return self.driver.find_element(*loc)

    def generate_data(self):
        """
        负责生产账号密码数据
        :return:
        """
        account_data = ''.join(random.sample('0123456789abcdef',8))

        return account_data


    def captcha_processing_(self):
        """
        截图处理以及验证码裁剪
        :return:
        """
        # 保存图片
        self.driver.get_screenshot_as_file(r"E:\selenium_pic\register_captcha.png")
        time.sleep(3)

        # 获取验证码图片的坐标
        captcha_element = self.get_element(*self.captcha_pic)
        left = int(captcha_element.location['x'])
        upper = int(captcha_element.location['y'])

        # 获取验证码的长和宽
        right = int(captcha_element.size['width']) + left
        lower = int(captcha_element.size['height']) + upper
        box = (left, upper, right, lower)

        # 打开大截图，进行裁切，再保存
        print('====================image重新打开截图====================')
        pic = Image.open(r"E:\selenium_pic\register_captcha.png")
        # 裁剪前，先进行灰度处理或者二值化处理(convert('1'))
        image = pic.convert('L')
        print("==========正在裁切截图===========")
        img = image.crop(box)
        img.save(r"E:\selenium_pic\register_captcha_small.png")
        print("======================验证码裁剪完成=====================")

    def baidu_ocr_captcha(self,filepath):
        """
        调用百度OCR识别验证码
        :param filepath: 验证码图片的路径
        :return:
        """
        baidu_ocr_result = BaiduOCR()
        code = baidu_ocr_result.basic_Accurate_options(filepath=filepath)

        return code

    def run_main(self):

        #先调用截图方法以及百度OCR处理验证码
        self.captcha_processing_()
        time.sleep(2)
        captcha_text = self.baidu_ocr_captcha(filepath=r"E:\selenium_pic\register_captcha_small.png")

        #定位账号密码
        email = self.get_element(*self.email_ele)
        nickname = self.get_element(*self.nickname_ele)
        password = self.get_element(*self.password_ele)
        captcha = self.get_element(*self.captcha_ele)
        button = self.get_element(*self.login_button_ele)

        #构造数据
        email_data = self.generate_data() + "@163.com"
        nickname_data = self.generate_data()
        password_data = self.generate_data()

        #输入数据
        email.send_keys(email_data)
        time.sleep(1)
        nickname.send_keys(nickname_data)
        time.sleep(1)
        password.send_keys(password_data)
        time.sleep(1)
        captcha.send_keys(captcha_text)
        time.sleep(1)

        #点击登录
        button.click()


if __name__ == '__main__':
    register = Register()
    register.run_main()