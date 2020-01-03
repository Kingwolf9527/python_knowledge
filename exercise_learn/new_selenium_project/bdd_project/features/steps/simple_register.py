# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/5 3:10

import sys
sys.path.append(r'F:\GitExtensions_python\project_spider\exercise_learn\new_selenium_project\bdd_project\features')

from behave import given,when,then,step_matcher


#调用正则处理
step_matcher('re')

@when('I open the register website')
def step_register_browser(context):

    context.driver.get('http://www.5itest.cn/register?goto=/')


@then(u'I expect that the title is "([^\s]*)"')
def step_register_get_title(context,title_name):

    title = context.driver.title
    assert title_name in title