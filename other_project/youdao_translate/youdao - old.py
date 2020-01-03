#旧版有道爬虫（没有加密的）
import urllib.request
import urllib.parse
import json
import time    #为了防止被网络识别为爬虫，应该访问有一个时间差，不能在短时间达到目标网站的访问阈值

while True:
    content = input('请输入需要翻译的内容(输入"q!"退出程序)：')
    if content == 'q!':
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null'   #这个是旧版本有道翻译的URL，新版的有道是在translate_o?
    #1:通过修改headers来
    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0;\WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    '''
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1502762754306'
    data['sign'] = '556692b456d411821609d2d4c575b389'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLlCKBUTTON'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.Request(url,data)     #1:如果前面加了head字典进去，这里也加了head进去
    response.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0;\WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')  #2:在.Requset的后面动态添加headers，用这个方法：Request.add_header(key,value),.Requset里面不用加
    request = urllib.request.urlopen(response)
    html = request.read().decode('utf-8')
    # print(html)
    target = json.loads(html)
    print("翻译结果： %s" %(target['translateResult'][0][0]['tgt']))
    print(response.headers)   #顺便验证header是否加进去了
    time.sleep(5)
