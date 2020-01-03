# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/20 23:57

from bs4 import BeautifulSoup

html = """

<table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45741&amp;keywords=&amp;tid=87&amp;lid=0">SA-腾讯社交广告Java开发工程师（上海）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-11-19</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45730&amp;keywords=&amp;tid=87&amp;lid=0">TEG11-数据挖掘研究员(深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2018-11-19</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45732&amp;keywords=&amp;tid=87&amp;lid=0">S2-Java应用开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-19</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45733&amp;keywords=&amp;tid=87&amp;lid=0">CSIG16-地图政企研发工程师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>北京</td>
					<td>2018-11-19</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45734&amp;keywords=&amp;tid=87&amp;lid=0">TEG06-C/C++高级后台开发工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2018-11-19</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45735&amp;keywords=&amp;tid=87&amp;lid=0">21557-Android音视频研发工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-19</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45727&amp;keywords=&amp;tid=87&amp;lid=0">25928-AI客户端开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-19</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45720&amp;keywords=&amp;tid=87&amp;lid=0">29777-金融云区块链高级研发工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-19</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45726&amp;keywords=&amp;tid=87&amp;lid=0">WXG01-117 微信iOS基础优化工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>广州</td>
					<td>2018-11-19</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45717&amp;keywords=&amp;tid=87&amp;lid=0">29777-金融云区块链高级研发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-19</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">1383</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a">2</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=20#a">3</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=30#a">4</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=40#a">5</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=50#a">6</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=60#a">7</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=70#a">...</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=1380#a">139</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </tbody></table>

"""


'''
    ::获取所有tr标签
    ::获取第二个tr标签
    ::获取所有class属性等于even的tr标签
    ::将所有id等于test，class也等于test的a标签提取出来
    ::获取所有a标签的href属性
    ::获取所有职位信息(纯文本) 

'''

#创建 beautifulsoup 对象,指定解析器，如果不指定，它就会用默认自带的解析器，指定编码，可以直接在里面设置:from_encoding
bs = BeautifulSoup(html,'lxml',from_encoding='utf-8')

# #格式化输出，美观,使用prettify()方法
# print(bs.prettify())

#1.获取所有tr标签，查找所有，可以用find_all()方法，返回的也是一个列表
# trs = bs.find_all('tr')
# for tr in trs:
#     print(type(tr))
#     #结果是：<class 'bs4.element.Tag'>    这个tr不是字符串，是一个tag对象，但是它会通过"__repr__"这个方法，把tag对象，通过字符串的形式返回
#     print(tr)
#     print('=='*30)

# #2.获取第二个tr标签(通过第二个参数limit，可以控制输出的标签数量)，而且在bs中，不能直接获取到第几个标签，只能通过列表去获取
# tr = bs.find_all('tr',limit=2)[1]
# print(tr)

# #3.获取所有class属性等于even的tr标签(获取class的属性有点区别，因为class在Python中是一个关键字，bs中加以区别用这个表示："class_",还有一种方法，是通过attrs={'class':'even'},里面是一个字典，key是属性，value是属性值)
# trs = bs.find_all('tr',class_='even')
# trs = bs.find_all('tr',attrs={'class':'even'})
# for tr in trs:
#     print(tr)
#     print('='*30)

#4.将所有id等于test，class也等于test的a标签提取出来,我推崇第二种写法
# alist = bs.find_all('a',id='test',class_='test')
# alist = bs.find_all('a',attrs={'id':'test','class':'test'})
# for a in alist:
#     print(a)

#5.获取所有a标签的href属性
# alist = bs.find_all('a')
# for a in alist:
#     #第一种方法：通过下标的方式获取
#     href = a['href']
#     print(href)
    # #第二种方法：通过attrs的属性方法获取
    # href = a.attrs['href']
    # print(href)

#6.获取所有职位信息(纯文本)(这里做一个切片，因为第一个tr标签，我们是不要的)
trs = bs.find_all('tr')[1:]
movies = []
for tr in trs:
    movie = {}
#     #在获取tr下的td标签
#     tds = tr.find_all('td')
#
#     title = tds[0].string
#     #标签的内容,用string方法
#     # print(title)
#
#     type = tds[1].string
#     # print(type)
#
#     num = tds[2].string
#     # print(num)
#
#     place = tds[3].string
#     # print(place)
#
#     pubtime = tds[4].string
#     # print(pubtime)
#
#     movie['title'] = title
#     movie['type'] = type
#     movie['num'] = num
#     movie['place'] = place
#     movie['pubtime'] = pubtime
#     movies.append(movie)
#
# print(movies)

#也可以这样，利用tr.stripped_strings去提取，stripped_strings方法是去匹配非标签型的字符串全部拿出来,并且会处理掉空白字符串
    infos = list(tr.stripped_strings)
    movie['title'] = infos[0]
    movie['type'] = infos[1]
    movie['num'] = infos[2]
    movie['place'] = infos[3]
    movie['pubtime'] = infos[4]
    movies.append(movie)
print(movies)