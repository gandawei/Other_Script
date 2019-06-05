# Script Name   : url_check.py
# Author        : Gan Dawei
# Created       : 2019.4.21
# Version       : 1.0
# Description   : Check repeat url in mysql,recommand first one.

#本程序作用是用于数据库去重，提供两个方法，方法需提供数据库表名和去重的列名。
#推荐使用第一个方法，更快更强
#第二个方法设置条件需谨慎，以防多删数据。
#2019.04.21 甘大伟写

import pymysql.cursors
import datetime
import time

class mysql():
    def __init__(self):
        self.connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123',
            db='test_db',
            charset='utf8')
        print('connect finish')
    def ex(self,table):
        self.cursor=self.connect.cursor()
        self.cursor.execute('{}'.format(table))
        print('Print finish')
    def exx(self,str):
        sql = 'select * from movie_list_copy where name_movie=%s'
        self.cursor.execute(sql,str)
    def save(self,id):
        sql ='INSERT INTO movie_list_copy(repeat_times) VALUES %s where id =%s'
        var=[id]
        self.cursor.execute(sql,var)
        self.connect.commit()
    def remove(self,table,id):
        self.cursor = self.connect.cursor()
        sql='delete from %s where id =%s'%(table,id)
        self.cursor.execute(sql)
        self.connect.commit()
        print('删除成功')
    def close(self):
        self.cursor.close()
        self.connect.close()
        print('close')
class check_repeat():
    def database_repeat_check(self, table, field):
        a = 0  # 总数据条数
        b = 0  # 重复数据条数
        c=[]
        original_id = []
        id = []
        u = mysql()
        sql = 'select id from %s order by id desc' % table
        u.ex(sql)
        content = u.cursor.fetchall()
        for i in content:
            original_id.append(i[0])
        sql_1 = 'select id from %s group by %s' % (table, field)
        u.ex(sql_1)
        content_1 = u.cursor.fetchall()
        start = time.time()
        for j in content_1:
            id.append(j[0])
        for i in original_id:
            a = a + 1
            if i not in id:
                u.remove(table,i)
                b = b + 1
                print('id为{}的数据重复了，已删除'.format(i))
            else:
                print('id为{}的数据未重复'.format(i))
        end = time.time()
        print('该数据库总数据条数为{}，其中{}重复了，已全部删除'.format(a, b))
        print('整个过程耗时{}s'.format(end - start))
        c.append(a)
        c.append(b)
        c.append(end-start)
        return c
class check_repeat_demo():
    def database_repeat_check(self,table,field):
        times = 0
        number = 0
        id = []
        u = mysql()
        u1 = mysql()
        sql='select * from %s order by id desc'%table
        u.ex(sql)
        content = u.cursor.fetchall()
        sql='select * from %s group by %s'%(table,field)
        u.ex(sql)
        content_after = u.cursor.fetchall()
        start = time.time()
        for i in content:
            number = number + 1
            for j in content_after:
                if i[1] == j[1]:
                    if i[0] != j[0] and i[2]==j[2]:
                        # print('id is not same')
                        u.remove(table,i[0])
                        times = times + 1
                    else:
                        pass
        end = time.time()
        print('一共{}条数据，共查出重复数据{}条'.format(number, times))
        print('所花时间为{}'.format(end - start))
        u.close()

if __name__=="__main__":
    check = check_repeat()
    check.database_repeat_check('dy_db','name_movie,url_movie')

