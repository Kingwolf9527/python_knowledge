# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/12 4:24


import time

from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util import browser_driver_test


def download_captcha_pic():

    driver = browser_driver_test.Webdriver_Browser('Browser','chrome_browser')
    driver.get_init_url('Register_url','url')
    #确认是否正确进入注册页面
    varify_register_ele = (By.ID,"getcode_num")
    WebDriverWait(driver,5).until(EC.presence_of_element_located(varify_register_ele))

    """
    
        通过类似爬虫的下载方法处理图片，但是由于验证码的刷新机制，每次请求都会刷新，因此这里不适用
    
    """
    #
    # #直接获取验证码(下载验证码图片)
    # captcha_ele = driver.find_element_by_id("getcode_num")
    # url = captcha_ele.get_attribute('src')
    # urlretrieve(url,"captcha_1.png")

    """
    
        通过裁切图片，获取验证码
    
    """
    #保存图片
    driver.get_screenshot_as_file(r"E:\selenium_pic\register_captcha.png")
    time.sleep(3)

    #获取验证码图片的坐标
    captcha_element = driver.find_element_by_id("getcode_num")
    left = int(captcha_element.location['x'])
    upper = int(captcha_element.location['y'])

    #获取验证码的长和宽
    right = int(captcha_element.size['width']) + left
    lower = int(captcha_element.size['height']) + upper
    box = (left,upper,right,lower)

    #打开大截图，进行裁切，再保存
    print('====================image重新打开截图====================')
    pic = Image.open(r"E:\selenium_pic\register_captcha.png")
    #裁剪前，先进行灰度处理或者二值化处理(convert('1'))
    image = pic.convert('L')
    print("==========正在裁切截图===========")
    img = image.crop(box)
    img.save(r"E:\selenium_pic\register_captcha_small.png")
    print("======================验证码裁剪完成=====================")


download_captcha_pic()