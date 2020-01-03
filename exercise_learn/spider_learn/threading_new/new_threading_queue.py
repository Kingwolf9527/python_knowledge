# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/29 21:39

"""

    Queue是python标准库中的线程安全的队列（FIFO）实现,提供了一个适用于多线程编程的先进先出的数据结构，即队列，用来在生产者和消费者线程之间的信息传递

        队列：FIFO(First in First Out)--先进先出
        栈：LIFO--后进先出

        队列的相关函数：
            1.初始化Queue(maxsize):创建一个先进先出的队列,maxsize是个整数，指明了队列中能存放的数据个数的上限
            2.qsize():返回队列的大小,也就是队列中有多少个元素
            3.empty():判断队列是否为空
            4.full():判断队列是否满了
            5.get():从队列中获取最后一个数据，也就是最先进入队列的数据
            6.put():将一个数据放到队列中

            get()和put()的block模块：
                get(block=True):默认都是true的，表示阻塞状态，如果这个队列没有值，会一直阻塞在这个地方
                put(block=True):默认都是true的，表示阻塞状态，一直往队列里面添加数据，如果队列满了，会一直处于阻塞状态，知道队列不满为止

"""

from queue import Queue
import time
import threading

# #创建队列
# q = Queue(4)

# #put():将一个数据放到队列中
# q.put(1)
# q.put(2)
# q.put(777)
#
# #qsize():返回队列的大小
# size = q.qsize()
# print(size)
#
# #empty():判断队列是否为空
# bool_empty = q.empty()
# print(bool_empty)
#
# #full():判断队列是否满了
# # for x in range(4):
# #     q.put(x)
# bool_full = q.full()
# print(bool_full)

#get():从队列中获取最后一个数据，先进先出
# for x in range(4):
#     q.put(x)
#
# for x in range(4):
#     print(q.get())
# data_first_get = q.get()
# print(data_first_get)


#get()和put()的block模块：
def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(2)

def get_value(q):
    while True:
        print(q.get())

def main():

    # 创建队列
    q = Queue(4)
    t1 = threading.Thread(target=set_value,args=[q])
    t2 = threading.Thread(target=get_value,args=[q])

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()