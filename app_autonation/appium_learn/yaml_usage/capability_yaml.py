# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/3 3:39

import yaml_usage
from appium import webdriver


with open('capability.yaml_usage','r',encoding='utf-8') as f:
    #把yaml数据类型转为python数据类型
    data = yaml_usage.load(f)

    #capability配置读取
    desire_caps = {}
    desire_caps['platformName'] = data['platformName']
    desire_caps['platformVersion'] = data['platformVersion']
    desire_caps['deviceName'] = data['deviceName']
    desire_caps['udid'] = data['udid']
    desire_caps['appPackage'] = data['appPackage']
    desire_caps['appActivity'] = data['appActivity']
    desire_caps['newCommandTimeout'] = data['newCommandTimeout']
    desire_caps['noReset'] = data['noReset']
    desire_caps['app'] = data['app']
    desire_caps['platformVersion'] = data['platformVersion']

    #启动应用
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub',desire_caps)
    driver.implicitly_wait(5)
