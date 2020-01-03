# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/23 3:58

import requests
import json

url = 'https://flights.ctrip.com/itinerary/api/12808/products'
headers = {
    'origin' : 'https://flights.ctrip.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    'referer': 'https://flights.ctrip.com/itinerary/oneway/can-sha?date=2019-05-24',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

json_data = '{"flightWay":"Oneway","classType":"ALL","hasChild":false,"hasBaby":false,"searchIndex":1,"airportParams":[{"dcity":"CAN","acity":"SHA","dcityname":"广州","acityname":"上海","date":"2019-05-24","dcityid":32,"acityid":2}]}'
json_data = json_data.encode('utf-8')
html = requests.post(url=url,headers=headers,data=json_data).text
html = json.loads(html)

flightInfos = html['data']['routeList']
for flightInfo in flightInfos:
    flightlegs = flightInfo['legs']
    for flightleg in flightlegs:
        #航班信息
        flight = flightleg['flight']
        #飞机编号
        flightNumber = flight['flightNumber']
        print(flightNumber)
        #航空公司
        airlineName = flight['airlineName']
        print(airlineName)
        #飞机型号
        craftTypeName = flight['craftTypeName']
        print(craftTypeName)
        #起飞时间
        departureDate = flight['departureDate']
        print(departureDate)
        #到达时间
        arrivalDate = flight['arrivalDate']
        print(arrivalDate)
        #准点率
        punctualityRate = flight['punctualityRate']
        print(punctualityRate)

        #机票价格信息
        tickets_prices = flightleg['cabins']
        for tickets_price in tickets_prices:
            ticket_price = tickets_price['price']
            #机票价格
            price = ticket_price['price']
            print('机票的价格是：%s' %price)
            #机票折扣
            rate = ticket_price['rate']
            print('机票的折扣是：%s' %rate)