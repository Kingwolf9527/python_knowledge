# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/11 21:52

from selenium import webdriver
import time

#确定用什么浏览器，确认浏览器实例
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#根据id定位输入框以及点击按钮
driver.find_element_by_id('kw').send_keys('马云宣布退位')
driver.find_element_by_id('su').click()

#退出语句
time.sleep(10)
driver.quit()