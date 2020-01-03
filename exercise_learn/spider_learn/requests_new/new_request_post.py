# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/19 1:50

import requests

#拉勾网的相关信息是通过ajax的异步加载的，通过js嵌入
url = "https://www.lagou.com/jobs/positionAjax.json?city=%E7%8F%A0%E6%B5%B7&needAddtionalResult=false"

#典型的反扒措施，验证信息头，而且不单单验证UA，如果只有UA，还是会默认为爬虫程序，需要添加额外的信息
headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer' : 'https://www.lagou.com/jobs/list_%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95?city=%E7%8F%A0%E6%B5%B7&cl=false&fromSearch=true&labelWords=sug&suginput=%E6%B8%97%E9%80%8F',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
}

data = {
    'first':'true',
    'pn': 1,
    'kd':'渗透测试'
}

res = requests.post(url,data=data,headers=headers)

# print(res.content.decode('utf-8'))

#因为返回的数据是一个json字符串，可以直接调用res.json()，把json字符串转换为字典的形式

print(type(res.json()))
#结果是：<class 'dict'>
print(res.json())