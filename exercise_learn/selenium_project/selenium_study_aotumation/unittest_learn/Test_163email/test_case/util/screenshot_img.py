# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/31 16:55

from selenium import webdriver
import os
import time


#截图函数
def insert_img(driver,file_name):
    # 处理截图的保存路径
    file_path = os.path.dirname(os.path.dirname(__file__))
    file_path = str(file_path)
    file_path = file_path.replace('\\', '/')
    base = file_path.split('/test_case')[0]
    image_path = base + "/report/image/" + file_name
    #截图
    driver.get_screenshot_as_file(image_path)

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=F:\profile')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.baidu.com')
    insert_img(driver,'baidu.jpg')
    time.sleep(3)
    driver.quit()