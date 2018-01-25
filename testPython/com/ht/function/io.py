#!/usr/bin/env python
#-*- encoding:Utf-8 -*-
from pip._vendor.distlib.compat import raw_input
from os.path import os
print("test");
'''str=raw_input("请输入：");print("你输入的内容是:",str);
str1=input("请输入");print("我输入的内容是:",str1);'''
fo=open("ai.py", "r", 1, "utf-8");
#open(file, mode, buffering, encoding, errors, newline, closefd, opener)
print("这个文件的文件名称是：",fo.mode);

fo1=open("testFile.py","wb+");
fo1.close();
fo2=open("testFile.py","wb");
fo2.close();
fo3=open("ai.py","a+",1,"utf-8");
fo3.write("我是追加的数据啊");#把数据追加到文件末尾
str=fo3.read(1);position=fo3.tell();print("我读取到的文件内容是个字符串是",str);
print("当前文件位置：",position);position=fo3.seek(0,0);newStr=fo3.read(10);print("把文件指针重新定义到开头:",position);
# print(fo1.name,fo2.name);os.rename("ai.py","buai.py");
print("我新读到文件内容是:",newStr);
#os.remove("C:\\Users\\Administrator\\Desktop\\test.txt");
print(fo3.name);print(os.getcwd());
fo3.close();