# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/23 23:29

from pyecharts import Bar

#创建Bar柱形图对象
bar = Bar(title='狼胸_主标题',subtitle='kingwolf_副标题')

#使用主题
bar.use_theme('dark')

# 主要方法，用于添加图表的数据和设置各种配置项:第一个参数是name，放在图形的右上角展示，第二个参数是X轴参数，显示的是列表或者元祖，第三个参数是Y轴参数，显示的是列表或者元祖
bar.add("鞋袜",["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

#打印输出图表的所有配置项
# bar.print_echarts_options()

#默认将会在根目录下生成一个 render.html 的文件，支持 path 参数，设置文件保存位置，如 render(r"e:\my_first_chart.html")，文件用浏览器打开。
bar.render('render2.html')