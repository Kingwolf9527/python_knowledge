# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/20 2:02

'''
    单线程的演化：设置两个参数，第一个是播放的文件，第二个是播放的次数，通过for循环来控制播放的次数

'''

import time

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


if __name__ == '__main__':

    music('黑色毛衣',2)
    movie('反贪风暴3',2)
    print('all end：',time.ctime())
