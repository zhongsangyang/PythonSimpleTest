#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from builtins import str
counter = 100#赋值整形变量
miles =1000.0#浮点型变量
name ="john"#字符串
"""
    
标准数据类型
在内存中存储的数据可以有多种类型。

例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。

Python 定义了一些标准类型，用于存储各种类型的数据。

Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
print -------------
Python支持四种不同的数字类型：
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）
int    long    float    complex
10    51924361L    0.0    3.14j
100    -0x19323L    15.20    45.j
-786    0122L    -21.9    9.322e-36j
080    0xDEFABCECBDAECBFBAEl    32.3e+18    .876j
-0490    535633629843L    -90.    -.6545+0J
-0x260    -052318172735L    -32.54e100    3e+26J
0x69    -4721885298529L    70.2E-12    4.53e-7j
"""
print(counter);print(miles);print(name);a=b=c=1;print(a);
var1=1;var2=2;#此时number对象已经创建了 del var1[,var2[,var3[....,varN]]]]del var1; del var1,var2;
print(var1+var2);print(var1+var2);str="hello world";
list=['runoob',786,2.23,'join',70.2];tinylist = [123, 'john']#python列表
print(str);#输出完整字符串
print(list+tinylist);#打印组合的列表
#以下是元组的数据
tuple=('ruoob',786,2.23,'join',70.2);print(tuple);print(tuple[0]);
#元组不允许更新，而列表是允许更细的
for listnew in list:
    print("当前列表的值为:",listnew);
'''tuple[0]='菜鸟';#错误'''
#以下是字典
dict={};
dict['one']="This is one";
dict[2]="This is two";
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict['one']);
print(dict[2]);print(dict.keys());print(tinydict.keys());print(tinydict.values());print(tinydict)
testParsetInt="123";newtestParsetInt=int(testParsetInt);
if newtestParsetInt==123:
    print("用int(x)把x转换成一个整数成功了")
elif newtestParsetInt.__eq__("123"):
    print("fail");
 
