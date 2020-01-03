# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/22 3:11

import requests
import json
import js2py
import time
from lxml import html

def ticket_api():


    url = 'http://flight.elong.com/search/ly/rest/list'

    headers = {
        'Host' : 'flight.elong.com',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept' : 'application/json; charset=utf-8',
        'Accept-Language' : 'zh-CN,zh;q=0.9',
        'X-Requested-With' : 'XMLHttpRequest',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Referer' : 'http://flight.elong.com/flightsearch/list?departCity=CAN&arriveCity=SHA&departdate=2019-05-23&backdate=&searchType=0',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    data = {

        'p' : '{"departCode":"CAN","arriveCityCode":"SHA","departDate":"2019-05-23","searchType":"0","classTypes":null,"isBaby":0}',
        'grabCode' : get_grapcode()

    }

    html = requests.post(url,headers=headers,data=data).text
    print(type(html))
    print(html)

def get_grapcode():

    url_list = 'http://flight.elong.com/flightsearch/list?departCity=CAN&arriveCity=SHA&departdate=2019-05-23&backdate=&searchType=0'
    time.sleep(5)

    html_list = requests.get(url_list).text
    html_list = html.etree.HTML(html_list)

    js = html_list.xpath('//input[@id="tsd"]/@value')[0]
    js = js.replace('/\)\^-1/gm', ')&-1')
    code = js2py.eval_js(js)
    print(code)
    return code

if __name__ == '__main__':
    # a = 'CAN'
    # b = 'SHA'
    # c = '2019-05-23'
    # # ticket_api(a,b,c)
    # get_grapcode(a,b,c)
    ticket_api()
    # get_grapcode()