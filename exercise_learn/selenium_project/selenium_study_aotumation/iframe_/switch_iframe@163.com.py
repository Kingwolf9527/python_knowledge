# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/11 22:03

from selenium import webdriver
import time
import os

def email_163_login():

    #设置user-data-dir路径
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('user-data-dir=F:\data_profile')
    driver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chromedriver.exe')
    driver = webdriver.Chrome(options=chrome_option, executable_path=driver_path)

    driver.get('https://email.163.com/')

    #让浏览器的窗口最大化
    driver.maximize_window()

    #然后，等待5秒，再输入账号密码
    time.sleep(5)

    '''
        输入账号密码，输入前，先清除输入框中的文字提示,因为163邮箱的input标签的ID是自动生成的，每次都不一样，因此不能用ID取定位,可以用name定位，它是不变的，还有记住，登录框是iframe的，需要切换到iframe，不然，后面是找不到定位的
    
    '''
    #找到邮箱账号登录框对应的iframe,因为iframe这里对应登录框的id是动态的，不唯一，所以，解决的方法是先用xpath定位到iframe的位置，再切换iframe到iframe中
    xpath = driver.find_element_by_xpath('//div[@id="urs163Area"]/iframe')
    driver.switch_to.frame(xpath)

    #先清除提示，输入账号

    driver.find_element_by_name('email').clear()
    driver.find_element_by_name('email').send_keys('lccr777')
    time.sleep(2)

    #先清除提示，再输入密码
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('922521dfxscr7')
    time.sleep(2)

    #点击登陆
    driver.find_element_by_id('dologin').click()
    time.sleep(5)

    '''
                查看是否登录成功
                
    '''
    #想操作其他元素的定位，需要先退出iframe，去到相应的iframe层级
    driver.switch_to.default_content()
    time.sleep(3)

    #判断登陆是否成功(定位这里的内容：<span id="spnUid">lccr777@163.com</span>)
    username = driver.find_element_by_id('spnUid').text
    print(username)
    if username == 'lccr777@163.com':
        print('登录成功')
        # 退出登录，退出浏览器
        driver.find_element_by_link_text('退出').click()
        time.sleep(1)
    else:
        print('登录失败')

    #关闭窗口
    driver.quit()

if __name__ == '__main__':
    email_163_login()