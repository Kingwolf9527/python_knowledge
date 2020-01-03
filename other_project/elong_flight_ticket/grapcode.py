# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/23 0:22

import requests
from lxml import html
import js2py

url_list = 'http://flight.elong.com/flightsearch/list?departCity=CAN&arriveCity=SHA&departdate=2019-05-23&backdate=&searchType=0'

html_list = requests.get(url_list).text
html_list = html.etree.HTML(html_list)

js = html_list.xpath('//input[@id="tsd"]/@value')[0]
js = js.replace('/\)\^-1/gm', ')&-1')
code = js2py.eval_js(js)
print(code)