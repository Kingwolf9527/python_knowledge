# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/18 14:48

with open(r'F:\HTML_report\2018-09-18 14_44_28result.html','rb') as f:
    test = f.read().decode('utf-8')
    print(test)