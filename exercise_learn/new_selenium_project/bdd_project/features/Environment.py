# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/5 3:15

import os
from selenium import webdriver


def before_all(context):
        # 设置user-data-dir的路径
        # new_options = webdriver.ChromeOptions()
        # new_options.add_argument(r"user-data-dir=F:\data_profile")

        # 设置谷歌浏览器的驱动路径
        driver_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/browser_driver/geckodriver.exe'

        context.driver = webdriver.Firefox(executable_path=driver_path)


def after_all(context):

    context.driver.close()




