#!/usr/bin/env python
#-*- encoding:utf-8 -*-
from idlelib.iomenu import encoding
import time
def repale_file(filename,rep_word,new_word):
    content=[];count=0;
    with open("F:\\test\\test1.txt","rb+",1) as f_read :
        #f_read.write("I am from China,Where are you from");
        print(f_read);
        for item in f_read:
            if rep_word in item:
                count=count+item.count(rep_word);
                item=str(item,encoding="utf-8");#把字节转化成str;
                rep_word=bytes.decode(rep_word);#吧字节转换成str
                item=item.replace(rep_word,new_word);
                item=bytes(item,encoding="utf-8");#吧字符串变成字节
            content.append(item);
            print(time.clock());
        f_read.writelines(content);
rep_word = input('请输入需要替换的单词或字符：');
rep_word=bytes(rep_word,encoding="utf-8");
new_word= input('请输入新的单词或字符：');
repale_file("F:\\test\\test1.txt", rep_word, new_word);
