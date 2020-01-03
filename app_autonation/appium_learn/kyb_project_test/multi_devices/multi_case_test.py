# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/12 3:32

from selenium.common.exceptions import NoSuchElementException
import time

class Multi_case(object):

    def __init__(self,driver):

        self.driver = driver

    def skip_btn(self):
        print('check skip button')
        try:
            # '跳过'按钮的定位
            time.sleep(2)
            skip_btn = self.driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
        except NoSuchElementException:
            print('no skip button！')
        else:
            skip_btn.click()

    def execute_guide(self):
        self.skip_btn()