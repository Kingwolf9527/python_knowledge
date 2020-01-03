# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/30 3:01

import socket
import time

def blocking_way():
    sock = socket.socket()
    #blocking
    first_time = time.ctime()
    print(first_time)
    sock.connect(('www.pptv.com',80))
    request = 'GET /HTTP/1.1\r\nHost: www.pptv.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    return response

def sync_way():
    res = []
    for i in range(10):
        res.append(blocking_way())
    return len(res)
    second_time = time.ctime()
    print(second_time)
sync_way()
