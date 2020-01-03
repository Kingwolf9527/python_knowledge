# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/29 0:56

import time
import threading

def coding():
    for x in range(3):
        # 查看当前线程的名字
        print('正在coding：%s' % x,threading.current_thread())
        time.sleep(1)


def drawing():
    for x in range(3):
        # 查看当前线程的名字:threading.current_thread()
        print('正在drawing：%s' % x,threading.current_thread())
        time.sleep(1)

# 常规的方式，非多线程的方式
# def main():
#     #这种方式总共花费了6秒
#     coding()
#     drawing()


#多线程的方式
def mul_threading_main():

    #创建子线程(target对象就是创建好的线程对应要执行的函数是哪一个，这里需要指定好，而且注意，这里target指定的是函数的名字(也就是函数本身)而不是函数的返回值,例如：target=coding，而不是包含括号的：target=coding())
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    #启动线程
    # 这种方式总共花费了3秒，明显速度快了很多，因为两个函数几乎同时执行，不像传统方式那样等待一个函数执行完毕才执行另外的函数
    t1.start()
    t2.start()

    #查看线程数(记住：主进程那里有一个主线程):threading.enumerate()
    thread_num = threading.enumerate()
    print(thread_num)


if __name__ == '__main__':
    # main()
    mul_threading_main()