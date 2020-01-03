# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/20 1:39

'''

    单线程的案例

'''
import time

#听音乐任务
def music():
    print('I was listening to music！ %s' % time.ctime())
    time.sleep(2)


#看电影任务
def movie():
    print('I was watching the movies！ %s' % time.ctime())
    time.sleep(5)


if __name__ == '__main__':
    music()
    movie()
    print('all end：',time.ctime())
