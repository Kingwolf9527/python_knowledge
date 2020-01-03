# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/12 21:31

import re
import time
from selenium import webdriver
from PIL import Image,ImageEnhance
import pytesseract
from selenium.webdriver.common.action_chains import ActionChains

def baidu_login():

    username = '1069645896@qq.com'
    password = '922521dfxs5619'

    login_url = 'https://passport.baidu.com/v2/?login'

    #截图或者验证码的保存地址
    full_screen_pic = r'F:\local_repository\Spider-learn\new-spider-and-python\new exercise\selenium\full_screen_pic.png'

    try:

        #驱动以及打开浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(login_url)
        driver.implicitly_wait(3)

        #定位到用户名登录的按钮上，用用户名登录
        driver.find_element_by_id('TANGRAM__PSP_3__footerULoginBtn').click()
        time.sleep(1)

        #提交账号密码
        driver.find_element_by_id('TANGRAM__PSP_3__userName').clear()
        driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys(username)
        time.sleep(2)
        driver.find_element_by_id('TANGRAM__PSP_3__password').clear()
        driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys(password)
        time.sleep(2)

        #获取验证码URL地址
        img_src = driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeImg').get_attribute('src')
        print(img_src)

        #如果匹配验证码路径成功（说明有提示输入验证码），则需读取验证码！(因为正常登录页面虽然没有验证码出现，但是也是存在验证码图片的，只是一个点而已，它的URL是：https://passport.baidu.com/passApi/img/small_blank.gif)
        if re.match(r'https://passport.baidu.com/cgi-bin/genimage?.*',img_src):
            print('需要输入验证码')
            #登录页面的浏览器整个截图
            driver.get_screenshot_as_file(full_screen_pic)

            # 定位验证码位置及大小
            location = driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeImg').location
            size = driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeImg').size
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            buttom = location['y'] + size['height']

            # 从文件读取截图，截取验证码位置再次保存
            img = Image.open(full_screen_pic).crop((left,top,right,buttom))
            # 转换模式：L | RGB
            img = img.convert('L')
            # 增强对比度
            img = ImageEnhance.Contrast(img)           # 增加饱和度
            img = img.enhance(2.0)
            img.save(full_screen_pic)

            # 再次读取识别验证码
            new_img = Image.open(full_screen_pic)

            #在.py文件配置中指定tessdata - dir
            tessdata_dir_config = '--tessdata-dir "F:\\tesseract-ocr\\tessdata"'
            code = pytesseract.image_to_string(new_img,config=tessdata_dir_config).strip()
            #打印验证码
            print(code)
            time.sleep(3)
            driver.find_element_by_id('TANGRAM__PSP_3__verifyCode').send_keys(code)


        #提交登录
        driver.find_element_by_id('TANGRAM__PSP_3__submit').click()

        #判断是否登录成功
        nickname = driver.find_element_by_id('displayUsername').text
        print(nickname)

        if nickname == 'C罗费德勒':
            print('登录成功')
            #悬停到右上角的昵称
            nick = driver.find_element_by_xpath('//span[@class="left"]')
            ActionChains(driver).move_to_element(nick).perform()

            #再定位到退出登录的链接
            logut = driver.find_element_by_link_text(u'退出')
            logut.click()

    except Exception as e:
        print('Error is :',e)
        time.sleep(2)
        driver.quit()


if __name__ == '__main__':
    baidu_login()




