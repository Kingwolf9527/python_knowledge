#新版的有道翻译爬虫，需要破解动态验证码的
import urllib.request
import urllib.parse
import json
import time
import random
import hashlib

content = input('请输入需要翻译的内容：')
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='

head = {}
head['Referer'] = 'http://fanyi.youdao.com/'
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0;\WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

data = {}
u = 'fanyideskweb'
d = content
f = str(int(time.time()*1000) + random.randint(0,10))
c = "rY0D^0'nM0}g5Mm1z%1G4"
sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = f
data['sign'] = sign
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLlCKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url,data= data,method='POST',headers=head)
response = urllib.request.urlopen(request)

html = response.read().decode('utf-8')
target = json.loads(html)
print("翻译结果： %s" %(target['translateResult'][0][0]['tgt']))

