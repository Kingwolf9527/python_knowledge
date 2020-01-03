# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/30 3:01

import socket
from concurrent import futures
import time

def blocking_way():
    sock = socket.socket()
    #blocking
    first_time = time.ctime()
    print(first_time)
    sock.connect(('www.pptv.com',80))
    request = 'HTTP/1.1 ok\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    return response

def sync_way():
    worker = 10
    with futures.ThreadPoolExecutor(max_workers=worker) as executor:
        fults = [executor.submit(blocking_way) for i in range(10)]
    return len(fults)
    second_time = time.ctime()
    print(second_time)

if __name__ == '__main__':
    sync_way()