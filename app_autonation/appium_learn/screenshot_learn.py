# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/30 4:08

import os
from appium_learn.capability_simple import driver

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('kingwolfbook14')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('12345678')

driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

#保存截图到脚本对应文件路径下
driver.save_screenshot('error_login.png')

#保存截图到指定路径下
img_ = os.path.dirname(__file__)
img_path = img_ + '/images/'
isexsists = os.path.exists(img_path)
if not  isexsists:
    try:
        os.makedirs(img_path)
    except FileExistsError as e:
        print(e)
img_name = img_path + 'error_login.png'
driver.get_screenshot_as_file(img_name)
