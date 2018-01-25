#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
import os
document = open("testfile.txt","w+",1,"utf-8");#w+用于读写
document.write("我是一颗小小的种子");
print(document.tell());document.seek(0,os.SEEK_SET);
print(document.tell());#context=document.read();print(context);
print(document.readlines());
document.close();
try:
    testint=int("123");
except:
    print("我抛出异常了")
else:
    print("我 是对的")
