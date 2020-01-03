# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/28 3:21

import os
from selenium import webdriver
import configparser
from new_maizi_aututest.utils.log import LogDetail

#定义日记对象
logger = LogDetail(logger='browserType').get_logger()

class BrowserEngine(object):


    def open_browser(self):

        '''读取配置文件'''
        con_path = os.path.dirname(os.path.dirname(__file__))
        file_path = con_path + '/config/config.ini'
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')

        '''浏览器驱动'''
        path = os.path.dirname(__file__)
        driver_path = path + '/package/chromedriver.exe'

        '''获取浏览器类型以及目标url'''
        browser = cf.get('browserType','browserName')
        logger.info('You select %s browser' %browser)
        login_url = cf.get('targetUrl','loginUrl')
        logger.info('login_url is %s' %login_url)

        '''判断浏览器对象，打开浏览器'''
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info('Starting firefox browser')
        elif browser == "Chrome":
            option = webdriver.ChromeOptions()
            option.add_argument('user-data-dir=F:\profile')
            driver = webdriver.Chrome(executable_path=driver_path,options=option)
            logger.info('Starting chrome browser')
        elif browser == "Ie":
            driver = webdriver.Ie()
            logger.info('Starting ie browser')
        else:
            print('Not found browser！')

        '''访问目标url'''
        try:
            driver.get(login_url)
            logger.info('Open url is %s' %login_url)
            driver.implicitly_wait(15)
            return driver
        except Exception as e:
            print(e)
            logger.error('url open error,error is %s' %e)


    def close_driver(self):
        logger.info('Now,Close and Quit the browser')
        self.open_browser().close()
        self.open_browser().quit()



if __name__ == '__main__':
    t = BrowserEngine()
    t.open_browser()

