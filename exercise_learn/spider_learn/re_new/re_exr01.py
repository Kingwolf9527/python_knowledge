# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/24 23:44

import re


# #1.验证手机号码
# text = '13752858856'
#
# re_test = re.match('1[34578]\d{9}',text)
# print(re_test.group())
# #结果是：13752858856


#2.验证邮箱，邮箱的规则是邮箱名称死用数字，字母和下划线组成的，然后加上"@"符号，然后加上域名
# test = 'kingwolf_book14@gmail.com'

# #因为“.”是关键字，需要转义
# re_test = re.match('\w+@[a-z0-9]+\.[a-z]+',test)
# print(re_test.group())
# #结果是：kingwolf_book14@gmail.com


# #3.验证URL，URL的规则是http/https/ftp 加上冒号，再加上双斜杠，在后面就是可以出现任意非空白字符串了(https://www.douyu.com)
# test = 'http://www.runoob.com/python/python-reg-expressions.html'
#
# re_test = re.match('(http|https|ftp)://[^\s]+',test)
# print(re_test.group())
# #结果是：http://www.runoob.com/python/python-reg-expressions.html


# #4.验证省份证，身份证是前面17位都是数字，第18位，可能是数字，可能是x，也有可能是X
# test = '440981199201235647'
#
# re_test = re.match('\d{17}[\dxX]',test)
# print(re_test.group())
# #结果是：440981199201235647

# #匹配0-100的数字
# #合法的一些数据：1,2,10,20,80,100等的；不合法的数字：02,09,102,200等等；3位的数据只能是100
# test = '100'
# #100的情况，?后面需要加上$符合，否则，它只会匹配到10，而不是100
# re_test = re.match('([1-9]\d?$|100)',test)
# print(re_test.group())
# #结果是：99

# #匹配出所有的价格
# test = "mac's price $1000,ipone's price $899"
#
# re_test = re.search('.*(\$\d+).*(\$\d+)',test)
# # print(re_test.group(2))
# # print(re_test.groups())


#findall的用法
# test = "mac's price $1000,ipone's price $899"
#
# re_test = re.findall('\$\d+',test)
# print(re_test)
# #结果是：['$1000', '$899']

# #sub函数：主要用在替换字符串中
# test = "mac's price $1000,ipone's price $899"
# #sub函数的第一个参数是正则表达式，第二个参数是要替换为什么字符串，第三个参数是目标字符串
# re_test = re.sub('\$\d+','$0',test)
# print(re_test)
# #结果是：mac's price $0,ipone's price $0
# #匹配HTML中的文本，思路是把所有的标签替换为空，<.+?>


# #split函数：主要用于分割
# test = 'hello kingwolf ni hao'
# #以空格分割，返回的是一个列表
# re_test = re.split(' ',test)
# print(re_test)
# #结果是：['hello', 'kingwolf', 'ni', 'hao']


#compile函数：多次正则匹配，可以用compile函数进行编译，提高执行效率
#需求是提取出数字
test = 'the number is 20.50'

#进行编译，因为小数点可有可无，没有就是没有小数点，小数点后面的数字也是可有可无
r = re.compile('\d+\.?\d*')

re_test = re.search(r,test)
print(re_test.group())
#结果是：20.50