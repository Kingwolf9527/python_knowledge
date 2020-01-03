# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/21 4:58
import sys
sys.path.append(r'F:\GitExtensions_python\project_spider\exercise_learn\new_selenium_project')

import random
import time
from PIL import Image
from baseview.element_processing import Elemnet
from other_project.baidu_ai.baidu_ai_api_test import BaiduOCR
from util.browser_driver_test import driver_init


class Register_new(object):

    def __init__(self,driver):

        self.driver = driver

    def get_element(self,selection,key):
        """
        读取封装好的元素，获取元素
        :param selection:
        :param key:
        :return:
        """
        ele_ = Elemnet(self.driver)
        ele = ele_.ele_processing(selection,key)

        return ele

    def generate_data(self):
        """
        负责生产账号密码数据
        :return:
        """
        account_data = ''.join(random.sample('0123456789abcdef',8))

        return account_data

    def send_user_info(self,selection,key,data):
        """
        定位元素后，发送数据
        :param selection:
        :param key:
        :param data:
        :return:
        """
        self.get_element(selection,key).send_keys(data)


    def captcha_processing_(self,selection,key):
        """
        截图处理以及验证码裁剪
        :return:
        """
        # 保存图片
        self.driver.get_screenshot_as_file(r"E:\selenium_pic\register_captcha.png")
        time.sleep(3)

        # 获取验证码图片的坐标
        captcha_element = self.get_element(selection,key)
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

    def baidu_ocr_captcha(self,selection,key,filepath):
        """
        调用百度OCR识别验证码
        :param filepath: 验证码图片的路径
        :return:
        """
        #先调用截图以及裁剪验证码方法
        self.captcha_processing_(selection,key)
        baidu_ocr_result = BaiduOCR()
        code = baidu_ocr_result.basic_Accurate_options(filepath=filepath)

        return code

    def run_main(self):

        #先调用识别验证码方法，获取验证码
        text_captcha = self.baidu_ocr_captcha('RegisterElement','code_captcha',r"E:\selenium_pic\register_captcha_small.png")

        #设置数据
        user_email = self.generate_data() + "@163.com"
        user_nickname = self.generate_data()
        user_password = self.generate_data()

        #调用发送数据方法
        self.send_user_info('RegisterElement','user_email',user_email)
        self.send_user_info('RegisterElement','user_nickname',user_nickname)
        self.send_user_info('RegisterElement','user_password',user_password)
        #发送验证码
        self.send_user_info('RegisterElement','text_captcha',text_captcha)

        #点击登录按钮
        self.get_element('RegisterElement','login_button').click()

        #判断验证码输入是否正确,错误进行截图保存
        captcha_code = self.get_element('RegisterElement','captcha_code-error')
        if captcha_code == None:
            print('注册成功！')
        else:
            self.driver.get_screenshot_as_file(r'E:\selenium_pic\captcha_error.png')
            print('注册失败！')

        time.sleep(5)
        #关闭浏览器
        self.driver.close()


if __name__ == '__main__':

    for i in range(3):
        #实例化driver以及验证码的路径
        driver = driver_init(i)
        register = Register_new(driver=driver)
        register.run_main()