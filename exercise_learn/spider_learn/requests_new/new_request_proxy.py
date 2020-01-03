# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/19 1:59

import requests

url = 'http://httpbin.org/ip'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

proxy = {
    'http':'175.168.136.31:53281'         #代理的ip地址，尽量用高匿名的，如果是透明的代理ip地址，一样会被服务器识别到真实ip的
}

#这里主要，连接代理的参数是proxies，而不是proxy
res = requests.get(url,headers=headers,proxies=proxy)
print(res.text)

# 结果是：
# {
#   "origin": "175.168.136.31"     返回的是代理ip，符合目标
# }