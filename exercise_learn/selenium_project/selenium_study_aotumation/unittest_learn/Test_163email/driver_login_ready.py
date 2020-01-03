# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/31 0:02

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver_login(object):

    def __init__(self):
        self.url = 'https://email.163.com/'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=F:\profile')
        self.driver = webdriver.Chrome(
            executable_path=r'F:\GitExtensions_python\project_spider\exercise_learn\selenium\selenium_study_aotumation\unittest_learn\Test_163email_case\driver\chromedriver.exe', \
            chrome_options=self.options)
        self.driver.maximize_window()

    def switch_login(self):

        self.driver.get(self.url)
        # 设置显式等待
        WebDriverWait(self.driver, 15).until(\
            EC.presence_of_element_located((By.XPATH, '//ul[@id="nav"]/li[contains(@class,"item item-163")]/b')))

        # 切换iframe到登录页面
        login_iframe = self.driver.find_element_by_xpath('//div[@id="panel-163"]/iframe')
        self.driver.switch_to.frame(login_iframe)
        return self.driver
if __name__ == '__main__':
    login_ready = Driver_login()
    login_ready.switch_login()

