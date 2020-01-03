# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/20 2:41

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
from maizi_test.loc_info import get_loc_info
from maizi_test.user_info import get_user_info
from maizi_test.log_moudle import Loginfo
from maizi_test.account_excel import Xlsx_Excel

#模块单独封装

def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

#打开浏览器(openBrower)
def openBrower():
    #驱动路径
    path = os.path.dirname(__file__)
    driver_path = path + '/driver/chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=F:\profile')
    handle_driver = webdriver.Chrome(chrome_options=options,executable_path=driver_path)
    return handle_driver

#打开url(loadUrl)
def openUrl(driver,url):
    driver.get(url)
    driver.maximize_window()

#查找元素
def findElement(driver,args):
    '''

    1.text_id
    2.account_id
    3.password_id
    4.button_id
    :return account_loc,pwd_loc,button_loc

    '''
    #登录弹框按钮
    # func = EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"sign-box fl")]/a[contains(@class,"globalLoginBtn")]'))
    loc_login = get_ele_times(driver,30,lambda d:d.find_element_by_link_text(args['text_id']))
    loc_login.click()

    #账号密码，以及登录按钮
    account_loc = driver.find_element_by_id(args['account_id'])
    pwd_loc = driver.find_element_by_id(args['password_id'])
    button_loc = driver.find_element_by_id(args['button_id'])
    return account_loc,pwd_loc,button_loc

def send_Values(loc_touple,args):
    '''

    :param loc_touple: touple
    :param args: account,password
    :return:
    '''
    list_key = ['account','password']
    i = 0
    for key in list_key:
        loc_touple[i].send_keys('')
        time.sleep(0.5)
        loc_touple[i].clear()
        time.sleep(0.5)
        loc_touple[i].send_keys(args[key])
        i += 1
    loc_touple[2].click()

def check_Result(driver,error_id,arg,log):
    #通过result返回值来判断当前的登录情况
    result = False
    time.sleep(3)
    try:
        error_loc = driver.find_element_by_id(error_id)
        print('Account And Password Error！')
        msg = 'account=%s password=%s : error: %s\n' % (arg['account'],arg['password'],error_loc.text)
        log.log_write(msg)
    except:
        print('Account And Password Right！')
        msg = 'account=%s password=%s : pass\n' % (arg['account'],arg['password'])
        log.log_write(msg)
        result = True
    return result

def logout(driver,loc_dict):

    logut_text = get_ele_times(driver,15,lambda d:d.find_element_by_link_text(loc_dict['logout']))
    logut_text.click()

def login(loc_dict,user_list):
    d = openBrower()
    log = Loginfo()
    openUrl(d,loc_dict['url'])
    loc_touple = findElement(d,loc_dict)
    for user in user_list:
        send_Values(loc_touple,user)
        time.sleep(2)
        result =  check_Result(d,loc_dict['error_id'],user,log)
        time.sleep(1.5)
        if result:
            #如果登录成功，需要先退出，才能测试其他账号的登录情况
            logout(d,loc_dict)
            time.sleep(0.5)
            #重新登录
            loc_touple = findElement(d,loc_dict)
            time.sleep(1.5)



if __name__ == '__main__':
    loc_dict = get_loc_info()
    # user_list = get_user_info()
    account_excel = Xlsx_Excel()
    user_list = account_excel.get_sheetinfo_by_index(0)
    login(loc_dict,user_list)