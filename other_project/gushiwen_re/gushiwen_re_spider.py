# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/26 1:20

import requests
import re

def parse_page(url):

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    text = res.text
    #使用正则表达式来匹配内容
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.S)
    dynasties = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.S)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?><a.*?>(.*?)</a>',text,re.S)
    content_tags = re.findall(r'<div\sclass="contson".*?>(.*?)</div>',text,re.S)
    #完整的诗词内容
    contents = []
    for content in content_tags:
        content = re.sub(r'<.*?>','',content)
        contents.append(content.strip())

    #组装完整的古诗词，包括诗词的名称，朝代，诗人，内容
    poems = []
    #使用到zip()函数，返回元祖的形式，例如：a=[1,2] ,b=['a','b'],c=zip(a,b)----[(1,'a'),(2,'b')]
    #例子：value=(1,2,3) -----a,b,c = value,这样，它会自动的把a等于1，b等于2，c等于3，相当于解压
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        #在组装成字典
        poem = {

            'title' : title,
            'dynasty' : dynasty ,
            'author' : author,
            'content' : content

        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print('='*80)



def main():

    base_url = 'https://www.gushiwen.org/default_{}.aspx'
    for x in range(1,101):
        url = base_url.format(x)
        parse_page(url)


if __name__ == '__main__':
    main()