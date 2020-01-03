# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/12 1:27

import pymysql
import sys
sys.path.append('project/')

#数据库配置
# 数据库配置信息
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'python_test',
    'charset': 'utf8'
}

class Boss_zhipin_mysql(object):

    def __init__(self):

        #创建连接数据库
        self.connect = pymysql.connect(**db_config)
        #创建游标
        self.cur = self.connect.cursor()

    def boss_zhipin(self,position):

        # 使用 execute()  方法执行 SQL 插入数据
        sql = """
        
            insert into boss_zhipin(company_name,position_name,salary,city,work_year,education,positon_descs,advantage,introduce,work_address)
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        
        """
        try:
            #执行SQL插入语句
            self.cur.execute(sql,(
                                  # 'test','1','2','3','4','5','6','7','8','9'
                                  position['company_name'],
                                  position['position_name'],
                                  position['salary'],
                                  position['city'],
                                  position['work_year'],
                                  position['education'],
                                  position['positon_descs'],
                                  position['advantage'],
                                  position['introduce'],
                                  position['work_address']
                                  )

                        )
            # 提交到数据库执行
            self.connect.commit()
        except:
            # 如果发生错误则回滚
            self.connect.rollback()

        #关闭连接
        self.connect.close()

if __name__ == '__main__':

    boss_zhipin_mysql = Boss_zhipin_mysql()

