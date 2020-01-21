#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2020/1/20 1:58

"""

编写登陆接口
    1.输入用户名，密码
    2.认证成功后，显示欢迎信息
    3.输错三次后锁定

"""

import sys



def loginTimes():

    # 输错限制次数
    limitTimes = 3
    # 初始化输错次数
    accountErrorTime = 0
    # 输入用户名
    username = input('Please inout username:')

    while accountErrorTime < limitTimes:

        #先检查输入的用户名是否被锁住了
        with open('lock_account.txt','r') as f:
            #循环lock文件
            for line in f.readlines():
                #用户名取第一个值
                infoLine = line.split()
                if username == infoLine[0]:
                    #如果lock了，就直接退出
                    sys.exit('Your account: %s is locked' %username)

        #输入密码
        password = input('Please input password:')
        # 设置一个数据匹配的标志位
        matchFlag = False
        #打开账号文件
        with open('account.txt','r') as ff:
            for line in ff.readlines():
                #提取处理每一行的账号以及密码
                user = line.strip('\n').split(':')[0]
                pwd = line.strip('\n').split(':')[1]
                if username == user and password == pwd:
                    #判断输入数据是否匹配
                    print('input data is matched')
                    matchFlag = True
                    #匹配成功，直接退出
                    break
        #如果数据不匹配，错误次数加1
        if matchFlag == False:
            print('data unmatched')
            accountErrorTime += 1
        else:
            print('Welcome login learning system')

    #如果while循环正常执行到条件不满足
    else:
        print('Your account: %s is locked' %username)
        #把账号追加到lock信息里面
        with open('lock_account.txt','a') as fff:
            fff.write('\n'+username)



loginTimes()
