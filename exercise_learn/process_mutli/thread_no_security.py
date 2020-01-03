#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2019/12/20 0:15

import threading
import time

class Thread_no_security(object):

    def __init__(self,account,balance):

        self.account = account
        self.balance = balance

    def draw(self,draw_monney):
        # 账户余额大于取钱数目
        if self.balance >= draw_monney:
            # 吐出钞票
            print(threading.current_thread().name + '==>'\
              +  "取钱成功！吐出钞票:" + str(draw_monney))

            #加上延时，采用多线程，就会出现线程安全问题，未及时减去余额
            time.sleep(0.05)

            # 修改余额
            self.balance -= draw_monney
            print("\t余额为: " + str(self.balance))

        else:
            print(threading.current_thread().name + '==>'\
                  + "取钱失败！余额不足！")

    def thread_processing(self):


        threading.Thread(name='KING',target=self.draw,args=(600,)).start()
        threading.Thread(name='WOLF',target=self.draw,args=(600,)).start()



if __name__ == '__main__':
    # 初始化
    test = Thread_no_security(account='9527', balance=1000)
    test.thread_processing()
