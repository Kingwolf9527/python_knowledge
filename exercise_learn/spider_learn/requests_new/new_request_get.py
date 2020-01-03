# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/19 1:25

import requests

#get请求方式不带其他参数的情况

# res = requests.get('https://www.baidu.com')
#
# print(type(res.text))
# #结果是;<class 'str'>，经过解码的(是Unicode的字符串)
#
# print(type(res.content))
# #结果是：<class 'bytes'>，经过编码的
#
# print(res.text)
# #它按照自己的猜测进行解码，容易出现乱码，如果需要，用这种方式：res.content.decode('utf-8')
#
# print(res.content)
# #因为是没有经过解码的，是经过编码后的数据，是bytes数据类型，因为在计算机网络中，保存的类型都是bytes类型，它是可以直接存储在我们的硬盘当中的
# print(res.content.decode('utf-8'))
#
# #还有其他的形式，例如：返回当前的url，状态码，编码方式
# print(res.url)
# print(res.status_code)
# print(res.encoding)
#
# # https://www.baidu.com/
# # 200
# # ISO-8859-1


#get请求方式，带有其他参数的情况

url = 'https://www.baidu.com/s'

params = {
    'wd' : 'C罗'
}

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
res = requests.get(url,params=params,headers=headers)

with open('baidu.html','w',encoding='utf-8') as f:
    f.write(res.content.decode('utf-8'))

print(res.url)