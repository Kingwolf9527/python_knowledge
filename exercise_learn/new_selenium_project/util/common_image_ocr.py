# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/2 3:38

import sys
sys.path.append(r'F:\GitExtensions_python\project_spider\exercise_learn\new_selenium_project')

import random
import time
from PIL import Image
from baseview.element_processing import Elemnet
from baidu_ai.baidu_ai_api_test import BaiduOCR
from util.browser_driver_test import Webdriver_Browser


class Common_image(object):

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