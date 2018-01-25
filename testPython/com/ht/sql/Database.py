#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
import pymysql
db = pymysql.connect("127.0.0.1","root","mysql","pythontest");
# conn = pymysql.Connect(host='192.168.255.255',user='laicheng',passwd='135246',db='test_sql') 
cursor=db.cursor();cursor.execute("select version()");data=cursor.fetchone();
print("现在的版本是%s"%data);
#cursor.execute("Create Database If Not Exists pythonTest Character Set UTF8 ");
sql="""create table employee(
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float)"""
#cursor.execute(sql);
insertsql="""insert into employee
    (first_name,last_name,
    age,sex,income) 
    values('zsy','xyz','20','0','3000');
    """
#cursor.execute("select * from employee");jilu=cursor.fetchone();print(jilu);
try:
    cursor.execute(insertsql);
    db.commit();
    print(">>>>>");
except Exception:
    db.rollback();
db.close();
