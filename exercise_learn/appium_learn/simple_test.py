# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/12 4:26

from appium import webdriver

caps = {

    'platformName':'Android',
    'deviceName': 'eac4b4a4',
    'platformVersion': '9.0',
    'appPackage': 'com.ss.android.article.news',
    'appActivity': 'com.ss.android.article.news.activity.SplashBadgeActivity'

}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/h'
                          'ub',caps)