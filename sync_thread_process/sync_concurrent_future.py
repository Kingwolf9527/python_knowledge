# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/5/19 4:54

from flask import Flask
import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()
app = Flask(__name__)

@app.route('/')
def update_redis():
    executor.submit(do_update)
    return 'OK'

def do_update():
    time.sleep(1)
    print('start update cache')
    time.sleep(3)
    print('end')


if __name__ == '__main__':
    app.run(debug=True)