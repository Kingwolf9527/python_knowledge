# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/20 2:14

'''

    通过：1.先创建线程数组：threads = []
         2.接着创建线程threading.Thread(target=,args=())    --------target:是可执行的函数/方法
         3.把创建的线程添加到线程组中
         4.启动线程，先遍历所以线程，然后启动(start())：    for i in threads:
                                                    i.start()
         5.守护线程：等待线程终止(join())(如果没有这个守护线程，当主线程退出后，所以的子线程不管它们是否在工作，都会被强行退出):    for i in threads:
                                                                                                                    i.join()
'''

import time
import threading

#音乐播放器
def music(func,loop):
    for i in range(loop):
        print('I was listening to %s！%s' % (func,time.ctime()))
        time.sleep(2)


#视频播放器
def movie(func,loop):
    for i in range(loop):
        print('I was watching the %s！%s' % (func,time.ctime()))
        time.sleep(5)


#创建线程数组
threads = []

#创建线程k1，并且添加到线程数组中
k1 =threading.Thread(target=music,args=('黑色毛衣',2))
threads.append(k1)

#创建线程k2，并且添加到线程数组中
k2 =threading.Thread(target=movie,args=('反贪风暴3',2))
threads.append(k2)


if __name__ == '__main__':

    #启动线程
    for i in threads:
        i.start()

    #守护线程
    for i in threads:
        i.join()

    print('all end：',time.ctime())
