# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/27 18:46
#coding:utf-8

from appium_learn.capability_simple import driver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#登录流程
# 账号
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('kingwolfbook14')
driver.implicitly_wait(1)

# 密码
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('12345678')
driver.implicitly_wait(1)

# login按钮
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
time.sleep(5)

#错误消息提示
# error_msg = "用户名或者密码错误"
# error_msg = "用户名或者密码错误,你还可以尝试2次"
# limit_msg = "验证失败次数过多，请15分钟后再试"

#提示信息的元素定位，常规定位是无法获取toast消息的，需要指定uiautomator2
# msg = '//*[contains(@text,\'{}\')]'.format(error_msg)
# msg = '//*[@text=\'{}\']'.format(error_msg)
msg = (By.XPATH,'.//*[contains(@text,"用户名或者密码错误")]')

try:
    toast_element = WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(msg))
    # toast_element = WebDriverWait(driver,10,0.1).until(lambda x:x.find_element_by_xpath(msg))
    print(toast_element.text)
    # toast_element = WebDriverWait(driver,15,0.1).until(lambda x:x.find_element_by_android_uiautomator('new UiSelector().text(\'%s\')' %msg))
except TimeoutException:
    print('Time Out')
else:
    text = '用户名或者密码错误'
    assert text in toast_element.text

