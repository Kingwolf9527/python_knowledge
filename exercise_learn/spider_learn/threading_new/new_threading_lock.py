# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/29 1:43

"""
    多线程与进程：
    多线程就比如火车的每一节车厢，进程就是火车，车厢没有火车是启动不了的，同时，火车是可以有多节车厢的

    多线程共享全局变量的问题：
    多线程都是在同一个进程中运行的，因此在进程中的全局变量所有线程都共享的，这就导致了一个问题，因为线程的执行顺序是无序的，有可能造成数据错误(当数据量很很大的时候，不同的线程同时执行同一个代码的概率就很高了，从而容易导致数据错误)

    在函数里面修改全局变量，必须要引用全局变量的关键字(global)去指定全局变量

    为了解决共享全局变量的问题，引进了锁的概念，对需要处理的数据，先上锁(acquire())，再释放(release())【这里上锁的对象是修改了全局变量，访问全局变量是不需要上锁的】

"""

import threading

#全局变量
Value = 0

#引进锁概念，对需要处理的数据，先上锁(acquire())，再释放(release())
get_Lock = threading.Lock()

def add_value():

    #在函数里面修改全局变量，必须要引用全局变量的关键字(global)去指定全局变量
    global Value
    #先上锁
    get_Lock.acquire()

    for x in range(1000000):
        Value += 1

    #再释放
    get_Lock.release()
        # print('value : %d' % Value)    #这里打印的是每一次执行后，value的值：从1开始，一直到第一个线程结束(1-10000)
    print('value : %d' % Value)          #这里打印的是每一个线程结束后，value的值(10000)

def main():
    for x in range(3):
        t1 = threading.Thread(target=add_value)
        t1.start()


if __name__ == '__main__':
    main()
