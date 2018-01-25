#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
a=10;
b=20;
if(a and b):
    print("a和b的值都是true")
else:
    print("1，变量a或者b有一个不为true");
if(a or b):
    print("a和b至少有一个为true");
else:
    print("两个都是不为真");
#修改a的值
a=0;
if(a and b):
    print ("3 - 变量 a 和 b 都为 true");
else:
    print("至少有一个不为true");
if(a or b):
    print("a和b至少有一个为true");
else:
    print("两个都是不为真");
if not( a and b ):
   print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print ("5 - 变量 a 和 b 都为 true")
list=[1,2,3,4,5];a=6;
if(a in list):
    print("a在list中");
elif(a not in list):
    print("a不在list中");
    
    #is y有is not
#a=b=20;
a=20;
b=20;
if(a is b):
    print("a 和   b有相同的标识");
else:
   print("a 和   b没有相同的标识");
if(a is not b):
 print("a 和   b没有相同的标识");
else:
   print("a 和   b有相同的标识");
   # 修改变量 b 的值
b=30;
if(a is b):
    print("a 和 b有相同的标识");
else:
    print("a 和 b没有相同的标识");
if(a is not b):
    print("a 和 b没有相同的标识");
else:
    print("有相同的标识 ");