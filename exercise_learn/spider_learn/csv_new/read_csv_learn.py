# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/26 22:59

import csv

def read_csv1():

    with open(r'F:\local_repository\Spider-learn\new-spider-and-python\new exercise\spider and visual\lianjia\lianjia1.csv','r') as f:
        reader = csv.reader(f)    #返回的是一个列表
        next(reader)    #这样会跳过标题的数据，从第一行开始
        #reader是一个迭代器
        print(type(reader))
        #结果是：<class '_csv.reader'>
        for x in reader:
            print(x)      #可以通过下标去获取指定的列数据

def read_csv2():
    with open(r'F:\local_repository\Spider-learn\new-spider-and-python\new exercise\spider and visual\lianjia\lianjia1.csv','r') as f:
        #把读取的数据转为字典，而且也不会包含标题那行的数据
        reader = csv.DictReader(f)    #返回的是一个字典
        for x in reader:
            print(x)    #可以通过key去获取指定的列数据


if __name__ == '__main__':
    read_csv2()