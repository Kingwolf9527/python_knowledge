# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/3 5:48

import time
import subprocess
import multiprocessing

class Multi_process_appium(object):

    def appium_start(self,host,port):

        '''启动appium server'''
        bootstarp_port = str(port + 1)
        #appium启动的命令
        cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstarp_port)
        print('%s run at %s' %(cmd,time.ctime()))
        #执行subprocess方法
        subprocess.Popen(cmd,shell=True,stdout=open('./appium_log/'+str(port)+'.log','a'),\
                         stderr=subprocess.STDOUT)

    def multi_process(self):
        #设置appium_process进程组
        appium_process = []
        #加载appium_process进程
        for i in range(2):
            host = '127.0.0.1'
            port = 4723 + 2*i
            appium_processed = multiprocessing.Process(target=self.appium_start,args=(host,port))
            appium_process.append(appium_processed)
        return appium_process


if __name__ == '__main__':
    # host = '127.0.0.1'
    # # port = 4723
    # # dd = appium_start(host=host,port=port)
    # #启动多个appium服务
    # for i in range(2):
    #     port = 4723 + 2*i
    #     appium_start(host=host, port=port)

    #多进程并发启动appium服务
    dd = Multi_process_appium()
    appium_process = dd.multi_process()
    for appium_processed in appium_process:
        appium_processed.start()
    for desired in appium_process:
        appium_processed.join()