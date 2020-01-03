# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/26 23:23

import csv

def write_csv1():

    header = ['name','age','height']
    values = [('老哥',18,170),('狼胸',24,180),('我罗',33,185)]

    #这里的newline=''默认是\n的换行，到账我们每写入一行数据，就会换行，要把它设置为空
    with open('new_csv.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        #把表头的数据写进去(row是行，column是列)
        writer.writerow(header)
        #把所有数据写进去
        writer.writerows(values)


def write_csv2():

    header = ['name', 'age', 'height']
    values = [
        {
            'name':'张三',
            'age':19,
            'height':180
        },
        {
            'name': '李四',
            'age': 18,
            'height': 180
        },
        {
            'name': '老哥',
            'age': 20,            'height': 160
        }
    ]
    with open('new_csv2.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,header)
        #手动写入头部数据的时候，需要调用writeheader()方法
        writer.writeheader()
        #写入所有数据
        writer.writerows(values)


if __name__ == '__main__':
    write_csv2()