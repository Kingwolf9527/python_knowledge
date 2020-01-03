# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/4 4:00

import socket
import os

class Check_port(object):

    def check_ports(self,host,port):
        #创建socket对象，采用ipv4(AF_INET)，TCP连接(SOCK_STREAM)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((host,port))
            s.shutdown(2)
        except OSError as msg:
            print('port %s is available' %port)
            # print(msg)
            return True
        else:
            print('port %s already be in used' %port)
            return False

    def release_ports(self,port):
        """
        释放指定的端口
        :param port:
        :return:
        """
        #获取端口的pid值
        cmd_find = 'netstat -ano | findstr %s' %port
        print(cmd_find)
        result = os.popen(cmd_find).read()
        print(result)

        if str(port) and 'LISTENING' in result:
            #获取LISTENING的索引值
            listen_index = result.index('LISTENING')
            #获取pid的开始索引值(7--是'LISTENING'和pid值直接的距离差7)
            start_index = listen_index + len('LISTENING') + 7
            #获取pid的结束索引值
            end_index = result.index('\n')
            #做切片处理
            pid = result[start_index:end_index]

            #关闭被占用的端口
            cmd_release = 'taskkill -f -pid %s' %pid
            print(cmd_release)
            os.popen(cmd_release)

        else:
            print('port %s is avaliable' %port)

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4725
    # check_ports(host=host,port=port)
    dd = Check_port()
    dd.release_ports(port=port)