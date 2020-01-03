# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/8/2 16:13

"""

    字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"


"""

import re

a = "not 404 found 张三 99 深圳"

#先转为list处理
list_a= a.split(' ')
print('原列表：',list_a)
#结果是：
# ['not', '404', 'found', '张三', '99', '深圳']

#正则匹配要过滤掉的数字和字母
filter_list = re.findall('[a-zA-Z]+|\d+',a)
print('匹配到的列表：',filter_list)

#把匹配到的列表元素跟原列表进行比较,相同就移除
for i in filter_list:
    if i in list_a:
        list_a.remove(i)
print('处理后的list_a:',list_a)
#在按照格式输出字符串内容
output_str = ' '.join(list_a)
print('最后输出的内容:',output_str)


"""
    使用re.sub()，替换
    a="张明 98分"，用re.sub，将98替换为100

"""

import re

a = "张明 98分"
b = re.sub('\d+','100',a)
print('修改后的成绩是：',b)
#结果是：
# 修改后的成绩是： 张明 100分


"""

    正则匹配，匹配日期2018-03-20

"""

url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'

result = re.findall('.*dateRange=(.*?)%7C(.*?)&.*',url)
print(result)
#结果是：
# [('2018-03-20', '2018-03-20')]