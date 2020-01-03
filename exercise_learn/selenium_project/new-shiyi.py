# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/12 0:57
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://panpartner.com/')
driver.maximize_window()
time.sleep(2)

driver.find_element_by_link_text('登录').click()
time.sleep(2)

driver.find_element_by_name('userAccount').clear()
driver.find_element_by_name('userAccount').send_keys('13726212990')
time.sleep(2)

driver.find_element_by_name('userPassword').clear()
driver.find_element_by_name('userPassword').send_keys('123456')
time.sleep(2)

driver.find_element_by_name('btn_login').click()
time.sleep(5)





