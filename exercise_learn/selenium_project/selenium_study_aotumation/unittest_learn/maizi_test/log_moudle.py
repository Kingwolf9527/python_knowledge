# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/21 19:38

import time
import os

class Loginfo(object):

    def __init__(self):
        self.file_path = os.path.dirname(__file__) + '/log/'
        #把时间元祖转为格式化时间
        self.file_time = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime()).replace('\\','/') + '.txt'
        self.file = os.path.join(self.file_path,self.file_time)

    def log_write(self,msg):
        with open(self.file,'a+',encoding='utf-8') as f:
            f.write(msg)


if __name__ == '__main__':
    d = Loginfo()
    d.log_write('test 测试')