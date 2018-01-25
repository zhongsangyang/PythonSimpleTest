'''
Created on 2018年1月16日

@author: 钟桑扬
'''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys;
from pip._vendor.distlib.compat import raw_input
from _ast import Expression
from parser import suite

print("hello world");print("你好世界");
total="1"+\
    "2"+\
    "3";
if True:
    print("true")
else:
    print("false");
print("没有严格缩进就会报错"+total);
#单词不正确竟然会有提示错误。
''' 
    这是一个多行注释 使用单引号
'''
""" 
    这个是一个多行注释使用双引号
"""
days=['Monday','TuesDay','Wednesday','Thursday',
  'Friday','Saturday'];
print(days);    raw_input("按下enter键退出，其它键显示。。。。、/n");

x='runoob'; sys.stdout.write(x+"\n");
x="a"
y="b"
print (x)
print (y)
print(x),
print(y),
if Expression:
    suite
elif Expression:
    suite
else :
    suite