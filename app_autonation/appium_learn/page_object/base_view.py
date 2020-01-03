# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/5 6:33


class Base(object):

    def __init__(self,driver):

        self.driver = driver


    def find_element(self,*loc):

        self.driver.find_element(*loc)


    def find_elements(self,*loc):

        self.driver.find_elements(*loc)