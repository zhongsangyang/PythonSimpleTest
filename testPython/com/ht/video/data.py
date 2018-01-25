#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
import time
from time import struct_time
from calendar import *
from datetime import *
ticks= time.time();#时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。
print("当前时间戳为：{0}".format(ticks));
print("当地时间是:{0}".format(time.asctime(time.localtime(ticks))));

print("格式化时间2--{0}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(ticks))));
print ("格式化时间是:"+time.strftime("%y-%m-%d %I:%M:%S", time.localtime()));
'''
    %y 两位数的年份表示（00-99）%Y 四位数的年份表示（000-9999）%m 月份（01-12）%d 月内中的一天（0-31）%H 24小时制小时数（0-23）%I 12小时制小时数（01-12）%M 分钟数（00=59）%S 秒（00-59）%a 本地简化星期名称%A 本地完整星期名称%b 本地简化的月份名称%B 本地完整的月份名称%c 本地相应的日期表示和时间表示%j 年内的一天（001-366）%p 本地A.M.或P.M.的等价符%U 一年中的星期数（00-53）星期天为星期的开始%w 星期（0-6），星期天为星期的开始%W 一年中的星期数（00-53）星期一为星期的开始%x 本地相应的日期表示%X 本地相应的时间表示%Z 当前时区的名称%% %号本身
'''
cal =month(2016,1);
print(cal);    print(time.clock());
'''
返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
'''
print(calendar(2017,w=2,l=1,c=6));#12月与下一行的可以发现是个单层嵌套的星期列表原来它只打印到2058年的
print(type(len("1234")));
t=len(calendar(2017,w=2,l=1,c=6));
for i in range(t-2058+12):
   print("i={0}".format(i));
   if(i<=11):
       print("{0} -- {1}".format(monthcalendar(2017,i+1),i+1),end="\n"); 
print(monthcalendar(2017,12));#[[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 0, 0, 0]]
print(monthrange(2017, 12));#第二个是一年中一个月的末天。
print(time.ctime());#等价于print(time.asctime(time.localtime()));
print("{0},{1}".format(time.gmtime(time.time()),time.time()));
print(time.mktime(time.localtime()))
print(time.strptime("30 Nov 14","%d %b %y"));

