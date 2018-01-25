#!/usr/bin/env python
#-*- encoding:Utf-8 -*-
import pymysql
db=pymysql.connect("127.0.0.1","root","mysql","pythontest");
cursor=db.cursor();
'''
cursor.execute("select *from employee");
data=cursor.fetchone();
db.close();'''

'''
sql="""
    create table t_login(
    name char(20) not null,
    age int)engine=InnoDB default charset=utf8;
"""
cursor.execute(sql);
name="zsy";
age=20;
'''
name1="xyz";
age1=30;

insertArgsql="""
    insert into t_login
    (name,age)
    values('%s','%d');
"""%(name1,age1);
# cursor.execute('insert into t_login values("%s", "%d")' % \
#              (name, age))
try:
    cursor.execute(insertArgsql);
    db.commit();
except Exception:
    db.rollback();
print(".........");