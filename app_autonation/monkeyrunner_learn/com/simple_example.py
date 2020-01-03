# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/19 3:04

#不能再代码中运行文件，需要在命令行下执行monkeyrunner .py文件
from com.android.monkeyrunner import MonkeyRunner as MR
from com.android.monkeyrunner import MonkeyDevice as MD
from com.android.monkeyrunner import MonkeyImage as MI


print('Connect devices......')
#等待连接设备
device = MR.waitForConnection()

# print('installing App.......')
# #安装app
# device.installPackage(r"D:\appium_apk_test\kaoyanbang.apk")

#app的包名和activity名
package = 'com.tal.kaoyan'
activity = 'com.tal.kaoyan.ui.activity.SplashActivity'
runComponent = package + '/' + activity

#启动Activity
print("launch App...")
device.startActivity(component=runComponent)

# #点击“跳过”按钮
# print("touch skip button")
# device.touch(961,104,'DOWN_AND_UP')
# MR.sleep(3)

#点击账号密码，并且输入账号密码
print("input username and password")
device.touch(314,557,'DOWN_AND_UP')
MR.sleep(2)
device.type('kingwolfbook14')

device.touch(306,685,'DOWN_AND_UP')
MR.sleep(2)
device.type('922521dfxs')

#点击登录按钮
print("touch login button")
device.touch(529,892,'DOWN_AND_UP')

#截图
print("takeSnapshot")
screenshot=device.takeSnapshot()
screenshot.writeToFile(r"F:\GitExtensions_python\project_spider\app_autonation\monkeyrunner_learn\com\dd.png",'png')



