# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/22 17:38

menus_down = []

def it_is_cooking(menus):
    while menus:
        menu = menus.pop()
        print("正在做的菜: %s" % menu)
        menus_down.append(menu)
    return menus_down

def finish_the_food(menus_down):
    for menu_down in menus_down:
        print("已经做完的菜:{}".format(menu_down))

menus = ["水煮牛肉","青椒肉丝","干锅茶树菇","清蒸鲈鱼","清炒时蔬","凉拌黄瓜","龙虎争霸","一清二白","夫妻肺片"]
it_is_cooking(menus= menus)
finish_the_food(menus_down =menus_down)
