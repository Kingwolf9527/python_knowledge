# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/31 16:18

from selenium import webdriver
import os
import time

#启动浏览器
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=F:\profile')
    #找到driver的路径
    file_path = os.path.dirname(os.path.dirname(__file__))
    file_path = str(file_path)
    file_path = file_path.replace('\\','/')
    base = file_path.split('/test_case')[0]
    driver_path = base + "/driver/chromedriver.exe"
    driver = webdriver.Chrome(
        executable_path=driver_path, \
        chrome_options=options)
    driver.maximize_window()
    return driver

if __name__ == '__main__':
    dr = browser()
    url = 'https://email.163.com/'
    dr.get(url)
    time.sleep(5)
    dr.quit()