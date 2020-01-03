# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/20 6:28

'''

    当线程较多的时候，如果每一个线程都要手工一个一个的添加，就会很不方便，因此要优化这种方法，对前面一个案例的优化

'''

import time
import threading

#超级播放器(什么都可以播放，包括音乐和电影):file_play--是等待播放的文件，包括音乐和电影   duration--是播放的时长，例如播放几秒
def super_player(file_play,duration):
    #每个文件都播放两次
    for i in range(2):
        print('Start Playing：%s ！ %s' % (file_play,time.ctime()))
        time.sleep(duration)      #这里设置播放的时长

#等待播放的文件和相应的时长(file_play和duration的数据来源这里)
dicts = {'黑色毛衣.mp3':5,'功夫.mp4':3,'逃学威龙.mp4':8,'演员.mp3':7}

#创建线程数组
threads = []

#线程的个数(判断键值对的个数)
thread_count = len(dicts)

#创建线程(先遍历所有资源，也就是dicts.items()，它的key值就是file_play文件名，value值就是duration时长)
for file_play,duration in dicts.items():
    t = threading.Thread(target=super_player,args=(file_play,duration))
    threads.append(t)


if __name__ == '__main__':

    #启动线程
    for i in range(thread_count):
        threads[i].start()

    #守护线程
    for i in range(thread_count):
        threads[i].join()

    print('all end：',time.ctime())





