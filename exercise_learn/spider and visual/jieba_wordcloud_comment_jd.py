# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/4 1:33

import matplotlib.pyplot as plt
from wordcloud import  WordCloud
import jieba
from PIL import Image
import numpy as np

#读取需要做词云的文件
with open(r'F:\local_repository\Spider-learn\new-spider-and-python\new exercise\page.txt','rb') as f:
    kw = f.read()

#分割成词语,参考一下列子，分割模式的区别
# sen = '今天来到了北京天安门看追风筝的人'
# words1 = jieba.cut_for_search(sen)#搜索引擎模式，false为精准模式，默认为全模式
# words2 = jieba.cut(sen,cut_all=False)#精准模式
# words3 = jieba.cut(sen,cut_all=True)#默认模式，全模式
# words4 = jieba.cut(sen)#默认模式

wordlist = jieba.cut(kw,cut_all=True)
# for i in wordlist:
#     print(i)
word_str = " ".join(wordlist)
# print(word_str)
#指定作为词云背景图
# mask_pic = np.array(Image.open("kw.jpg"))

#设置词云
#my_wordcloud = WordCloud().generate(word_str) 默认构造函数

my_word = WordCloud(
                            #设置背景颜色
                            background_color='black',
                            #设置背景图片
                            # mask=mask_pic,
                            #设置最大显示的字数
                            max_words=100,
                            #设置中文字体,不设置这个，中文词云无法显示，默认的字体不支持中文
                            # font_path=r'‪C:\Windows\Fonts\simhei.ttf',
                            #设置字体的最大值
                            max_font_size=150,
                            #设置有多少种随机生成状态，即是有多少种配色方案
                            random_state=50,
                            #输出画布的宽度,高度等等的设置
                            width=2048,   #1024是像素
                            height=2048,
                            margin=3
                        )

#生成词云
my_wordcloud = WordCloud().generate(word_str)
#保存词云图片
my_wordcloud.to_file('ciyun.jpg')

#展示图片
plt.imshow(my_wordcloud)
plt.axis('off')
ciyun_pic = plt.show()
print(ciyun_pic)
