# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/24 3:18

from selenium import webdriver
import os

#打开浏览器(openBrower),获取浏览器驱动
def openBrower():
    #驱动路径
    path = os.path.dirname(os.path.dirname(__file__))
    driver_path = path + '/driver/chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=F:\profile')
    handle_driver = webdriver.Chrome(chrome_options=options,executable_path=driver_path)
    return handle_driver
