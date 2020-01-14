#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2020/1/14 23:21

import time

#通过time.time()方法来统计程序运行时间
def programRunStatisticsTime():
    #运行前的时间统计
    startTime = time.time()
    for i in range(1000):
        j = 2 * i
        for k in range(j):
            t = k
            # print(t)
            #未注释print，程序运行的时间是： 12.382403373718262
            #注释print后，程序运行的时间是： 0.05788922309875488
            #提升性能，要注意精简不必要的开销
    endTime = time.time()
    print('程序运行的时间是： %s' %(endTime-startTime))

# programRunStatisticsTime()


#通过time.clock()方法，看看程序执行过程中CPU执行了多长时间
def cpuRunStatisticsTime():
    #运行前的时间统计
    startTime = time.clock()
    for i in range(1000):
        j = 2 * i
        for k in range(j):
            t = k
            # print(t)
            #未注释print，CPU运行的时间是： 12.292278405818342
            #注释print后，CPU运行的时间是： 0.03342401913392392
            #提升性能，要注意精简不必要的开销
    endTime = time.clock()
    print('CPU运行的时间是： %s' %(endTime-startTime))

cpuRunStatisticsTime()