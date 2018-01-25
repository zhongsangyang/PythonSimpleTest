#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
''' unny想学python

  139***38053@163.com

Python变量类型：

（1）Numbers

（2）String

（3）List  []

（4）Tuple（元祖）(),相当于只读列表，不可以二次赋值

（5）dictionary（字典）{}，key值对

sunny想学python
   sunny想学python

  139***38053@163.com

7个月前 (06-14)'''
from com.ht.video.Person import Person
from math import *
sunddy=Person();
#print(sunddy("test"));print(repr(sunddy));
print(sunddy.getName("sunndy"));n="我是一个字符串";print(type(n));
print(range(5));a=1; print(isinstance(a, int));
a=20;
b=10;c=0;c=a+b;print("1-c的值为",c);c=a-b;print("2-c的值为:",c);c=a*b;print("3-c的值为",c);
c=a/b;print("4-c的值为",c);c=a%b;print("5-c的值为",c);
a=10;b=5;c=a/b;print("7-c的值为",c);c=2;c**=3;print(c);
#11111100
#0*2^0+0*2^1+1*2^2+1*2^3+1*2^4+1*2^5+1*2^6+1*2^7+1*2^8
#　　=0+0+4+8+16+32+64+128
#　　=252
test="00001101";
#print(0*2**0+0*2**1+1*2**2+1*2**3+1*2**4+1*2**5+1*2**6+1*2**7);
print(len(test));
i=0;dict={};j=len(test)-1;sum1=0;
#list=['1','2','3'];
list=list(test)#>>['1', '1', '1', '1', '1', '1', '0', '0']

for l in list:
    sum1+=int(l)*2**j;
    print(j,int(l),"调试的值看对不对");#print(0*2**7+0*2**6+0*2**5+0*2**4+1*2**3+1*2**2+0*2**1+1*2**0)
    j-=1;
print(sum1);print(set(test),"把字符串变成了一个set");
for l in test:
    dict[i]=l;
    i+=1;
print(dict,"吧字符串变成了一个字典");
#print(0*2**7+0*2**6+0*2**5+0*2**4+1*2**3+1*2**2+0*2**1+1*2**0)
#a=00111100;
#b=00001101;print((a&b));#0000 1100
#print(00111100|00001101);
