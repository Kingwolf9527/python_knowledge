#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2020/2/10 18:31

import time

#设置标志位
def flag():
    while True:
        breakFlag = input('''\t\t\t是否继续？(y/n)''')
        if breakFlag == 'y' or breakFlag == 'n':
            return breakFlag
        else:
            print('''\t\t\t输入有误，请重新输入！\n''')

with open('test.txt','r') as f:
    #遍历每一行信息
    info = f.readlines()
    #设置初始标志位
    breakFlag = ''
    print('''\n\t\t\t您好！欢迎来到员工信息查询系统！''')
    while breakFlag != 'n':
        while True:
            searchInfo = input('''\n\t\t\t请输入您需要查询的信息：''')
            if len(searchInfo) > 1:
                break
            else:
                print('''\n\t\t\t输入有误，请重新输入！''')
        #查询结果的数量
        countNumber = 0
        #查询结果的保存列表
        searchInfoList = []
        for i in info:
            if i.count(searchInfo) > 0:
                searchInfoList.append(i.replace(searchInfo,'''(%s) %s''' %(searchInfo,i)))
                countNumber += i.count(searchInfo)

        if countNumber > 0:
            #如果查询有结果，打印出来
            print('''\n\t\t\t总共查询到：%d 条信息''' %countNumber)
            for i in searchInfoList:
                print(i)
            #调用标志位方法，看是否继续查询
            breakFlag = flag()
        else:
            print('''\n\t\t\t没有查询到相关信息！''')
            # 调用标志位方法，看是否继续查询
            breakFlag = flag()

for i in range(3):
    print('''\n\t\t\t谢谢使用员工查询系统： %d 秒后，退出系统！''' %(3-i))
    time.sleep(2)
exit()



