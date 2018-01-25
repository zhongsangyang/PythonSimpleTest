#!/usr/bin/env python
#-*- encoding:utf-8 -*-
from calendar import *
import time
print(calendar(2018,2,1,6));
test=time.localtime();
print(monthcalendar(2018,1));print(test[2]);mothArry=monthcalendar(2018,1);
count=0;nowlist=[];
for i in mothArry:
    print(i,end="\t");
    for j in i:
        if test[2]==j:
            count+=1;
            print(count,">>");nowlist=i;print(nowlist);
print(nowlist);print(nowlist[0]);