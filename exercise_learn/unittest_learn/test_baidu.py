# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/17 1:59

from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.url = "http://www.baidu.com"

    def test_baidu(self):
        driver = self.driver
        driver.get(self.url + '/')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('unittest')
        driver.find_element_by_id('su').click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title,"unittest_",msg="Result is not our expected!")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()