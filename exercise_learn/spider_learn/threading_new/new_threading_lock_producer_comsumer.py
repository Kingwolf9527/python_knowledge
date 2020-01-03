# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/29 6:03
"""


    多线程的生产者模式和消费者模式：
    对修改全局变量加锁


"""
import threading
import random
import time

#全局金钱
global_money = 1000

#全局锁
global_lock = threading.Lock()

#全局定义生产所需要的次数
global_times = 10
#初始化的生产次数
global_time = 0

class Producer(threading.Thread):

    def run(self):
        #声明全局变量
        global global_money
        global global_time
        global global_times
        # 生产者不断生成钱，用死循环，否则生产者线程执行完后，就不会再生产钱了
        while True:
            money = random.randint(100,1000)
            #上锁
            global_lock.acquire()
            #再生产金钱之前，我们需要判断当前的生产次数是否超过了我们所需要的次数，如果到达了，就退出，但是记住，退出前，记得先释放锁，否则会出现死锁
            if global_time >= global_times:
                #先释放锁，否则会出现死锁
                global_lock.release()
                break
            #生产金钱
            global_money += money
            print("%s生产了%d元钱，总金钱是%d元钱" % (threading.current_thread(),money,global_money))
            #生产次数的叠加
            global_time += 1
            #释放锁
            global_lock.release()
            time.sleep(0.5)

class Consumer(threading.Thread):

    def run(self):
        #声明全局变量
        global global_money
        #不断消费金钱，用死循环
        while True:
            money = random.randint(100,1000)
            #上锁
            global_lock.acquire()
            #消费金钱的时候，需要做判断，所消费的钱跟总金额做比较
            if global_money >= money:
                global_money -= money
                print('%s消费了%d元钱，剩余的总金额还剩余%d元钱' %(threading.current_thread(),money,global_money))
            else:
                #消费者这边也是同样处理，当生产者的次数到达global_times设置的次数，就先释放锁，退出当前线程
                if global_time >= global_times:
                    global_lock.release()
                    break
                print('%s消费者准备消费%d元钱，剩余的总金额%d元钱，不足！'%(threading.current_thread(),money,global_money))
            #释放锁
            global_lock.release()
            time.sleep(0.5)

def main():

    # 设置3个消费者
    for x in range(3):
        # 可以知道类对象的名字
        t = Consumer(name="消费者线程%d" % x)
        t.start()

    #设置5个生产者
    for x in range(5):
        #可以知道类对象的名字
        t = Producer(name="生产者线程%d" %x)
        t.start()


if __name__ == '__main__':
    main()