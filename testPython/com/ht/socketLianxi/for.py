#!/usr/bin/env python
#-*- encoding:utf-8 -*-
ls=[];
for a in range(1,4):
    for b in range(1,5):
        for c in range(1,4):
            if a!=b and b!=c and a!=c:
                ls.append([a,b,c]);
print("总数量",len(ls));
print(ls);
print(">>>>>>>>>>>>>>>>");
line=[];
for i in range(123,433):
    a=i%10;
    b=(i%100)//10;
    c=(i%1000)//100;
    if a!=b and b!=c and a!=c and 0<a<5 and 0<b<5 and 0<c<5:
        print(i);
        line.append(i);
print("the total is :",len(line));

