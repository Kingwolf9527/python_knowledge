# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/18 23:18

from urllib import request

#不使用代理的情况
#这个url会返回当前连接的IP地址
# url = 'http://httpbin.org/ip'

# res = request.urlopen(url)
# print(res.read())
#返回的结果是：b'{\n  "origin": "183.53.191.183"\n}\n'，这个是本机地址


'''
    ProxyHandler(代理)的原理：在请求目的网站之前，先请求代理服务器，然后让代理服务器去请求目标网站，代理服务器拿到目的网站的数据后，在转发给我们
    使用代理的情况下：
    1.使用Proxyhandler，传入代理创建一个handler，代理必须是一个字典，字典的key是协议，http或者https，字典的value是ip:port
    2.使用上面的handler构建一个opener，使用build_opener(handler)
    3.使用构建的opener去发送请求,使用opener.open()

'''
url = 'http://httpbin.org/ip'
#使用Proxyhandler，传入代理创建一个handler，代理必须是一个字典
handler = request.ProxyHandler({'http':'61.142.72.154:40175'})

#使用上面的handler构建一个opener
opener = request.build_opener(handler)

#使用构建的opener去发送请求
res = opener.open(url)
print(res.read())
#结果是：b'{\n  "origin": "61.142.72.154"\n}\n'，返回的是代理的ip地址