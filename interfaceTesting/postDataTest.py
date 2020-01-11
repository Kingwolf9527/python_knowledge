#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2020/1/11 15:47

import requests
import json

url = 'https://flights.ctrip.com/itinerary/api/12808/products'
headers = {
    'origin' : 'https://flights.ctrip.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    'referer': 'https://flights.ctrip.com/itinerary/oneway/can-sha?date=2020-01-24',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

json_data = {
        "flightWay":"Oneway","classType":"ALL","hasChild":False,"hasBaby":False,"searchIndex":1,\
        "airportParams":[
            {"dcity":"CAN","acity":"SHA","dcityname":"广州",\
             "acityname":"上海","date":"2020-01-24","dcityid":32,"acityid":2
             }
                        ]
            }

# #这里传参是json格式的数据，跟传统的form表单不同
#第一种方式，data参数传参，把数据json.dumps()反序列化为json处理
html = requests.post(url=url,headers=headers,data=json.dumps(json_data)).text

#第二种方式，json参数传递，会把字典对象自动转为json格式
# html = requests.post(url=url,headers=headers,json=json_data).text
print(html)
