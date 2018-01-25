#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 打印空心等边三角形 
#打印菱形
'''    * 
       * * 
       *   *
       * * * *
'''
#打印直角三角形。
for i in range(1,4):
    for j in range(1,4):
        if(j>i):
            break;
        else:
            print("*",end="\t")
    else:
        print("sss")
    print("",end="\n"); 
#pass语句
    #输出python的每个字母
    for letter in 'Python':
        if letter =='h':
            pass
            print("这是pass模块")
        print("这是当前的字母{0}".format(letter));
    print("good by");