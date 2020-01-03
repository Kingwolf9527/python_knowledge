# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/19 2:12

# import requests

# url = 'https://www.baidu.com'
#
# res = requests.get(url)
# print(res.cookies)
# print(res.cookies.get_dict())
# #结果是：
# # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
# # {'BDORZ': '27315'}


#通过session模块是实现登陆，cookie保持(但是这里的session跟web开发中的那个session是不同的，要注意)

import requests

mail_url = 'https://mail.163.com/'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

data = {
    'email' : 'lccr777',
    'password' : ''
}

#登录,先创建session对象，再通过session去发送post的登录请求
session = requests.Session()
session.post(mail_url,data=data,headers=headers)     #但是163邮箱的登录是嵌套在iframe里面的，在selenium里面好处理，这里不好处理

#前往邮件的收件箱
recei_url = 'https://mail.163.com/js6/s?sid=yCehZmvHtmRBaLrOZzHHTUHCLImuGWAa&func=mbox:listMessages&LeftNavfolder1Click=1&mbox_folder_enter=1'
data_new = {
    'var' : '<?xml version="1.0"?><object><int name="fid">1</int><string name="order">date</string><boolean name="desc">true</boolean><int name="limit">20</int><int name="start">0</int><boolean name="skipLockedFolders">false</boolean><string name="topFlag">top</string><boolean name="returnTag">true</boolean><boolean name="returnTotal">true</boolean></object>'
}

res = session.post(recei_url,data=data_new,headers=headers)
print(res.content.decode('utf-8'))