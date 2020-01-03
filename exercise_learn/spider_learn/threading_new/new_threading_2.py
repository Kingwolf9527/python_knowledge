# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/29 1:25

import time
import threading


#为了更好的封装，采用继承类的方式写
class CodingThread(threading.Thread):

    def run(self):
        for x in range(3):
            # 查看当前线程的名字
            print('正在coding：%s' % x, threading.current_thread())
            time.sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            # 查看当前线程的名字
            print('正在drawing：%s' % x, threading.current_thread())
            time.sleep(1)


def main():
    #创建线程对象
    t1 = CodingThread()
    t2 = DrawingThread()

    #启动线程
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()