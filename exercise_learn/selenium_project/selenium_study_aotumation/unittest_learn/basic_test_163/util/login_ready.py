# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/19 16:54

from basic_test_163.config.account_config import get_account_info
from basic_test_163.util.driver import browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(driver):

    accounts,passwords = get_account_info()

    for useraccount,userpassword in zip(accounts,passwords):

        # 定位frame必须写入循环函数中，因为每次退出之后登陆都需要
        xpath = driver.find_element_by_xpath('//div[@id="panel-163"]/iframe')
        driver.switch_to.frame(xpath)

        #定位账号密码，按钮
        account_loc = driver.find_element_by_name('email')
        password_loc = driver.find_element_by_name('password')
        button_loc = driver.find_element_by_id('dologin')

        #输入账号密码，点击按钮
        account_loc.clear()
        account_loc.send_keys(useraccount)

        password_loc.clear()
        password_loc.send_keys(userpassword)

        button_loc.click()

        # 因为登陆进入之后网页改变，需要切换页面
        driver.switch_to_default_content()

        print(useraccount,userpassword)

if __name__ == '__main__':
    url = 'https://email.163.com/'
    driver = browser()
    driver.get(url)
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//section[@id="main"]/h2')))
    login(driver)