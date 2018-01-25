#!/usr/bin/env python
#-*- encoding:UTF-8 -*-

'''
try:
    x=int(input("请输入一个数字"));
except Exception:
    print('An exception flew by!')
    raise
try:
    raise KeyboardInterrupt
finally:
    print("good bye,world")
'''
from com.ht.zsy.ruoob2 import name
from os.path import os
from com.ht import function
import shutil

class Myerror(Exception):
    def __init__(self,value):
#       self.value=repr(value);
        self.value=str(value);
try:
    raise Myerror(1000);
except Myerror as e:
    print("Myerroe exception occured,value:",e.value)

def divide(x,y):
    try:
        result=x/y;
    except ZeroDivisionError:
        print("除数为0");
    except Exception:
        print("str can't cast to int");
    else:
        print("除数不为0y运行正常");
divide(1, 0);
with open("C:\\Users\\Administrator\\Desktop\\testfile.txt","r+",1,"utf-8") as f:
    print(f.tell());
    print(f.read());
    for i in f:
        print(i,end="")
        
class Person:
    name="";
    age=0;
    __weight="";#私有属性
    def __init__(self,n,a,w):
        self.name=n;
        self.age=a;
        self.__weight=w;
    def speak(self):
        print("%s 说: 我  %d 岁了。" %(self.name,self.age));
    
class Student(Person): 
    grade="";
    def __init__(self,n,a,w,g):
        Person.__init__(self, n, a, w) ;
        self.grade=g;
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我%d岁了。我上%d年纪了"%(self.name,self.age,self.grade));
#s=Student("zhang",10,60,3);s.speak();

class speaker():
    name="";
    age=0;
    def __init__(self,n,a):
        self.name=n;
        self.age=a;
    def speak(self):
        print("%s 说：我%d岁了"%(self.name,self.age));
class simpler(speaker,Student):
    name="";
    age=0;
    weight=""
    grade1=0;
    def __init__(self,n,a,w):
        Person.__init__(self,n, a,w);
        self.weight=w;
    def speak(self):
        print("%s 说：%d岁了 体重为:%s" %(self.name,self.age,self.weight));
         
simpler=simpler("张三",20,"60斤");
simpler.speak();

class Jcounter:
    __count=0;
    publiccount=0;
    def count(self):
        self.__count+=1;
        self.publiccount+=1;
        print(self.__count);
#j=Jcounter();j.count();print(j.__count)#不能在类外面访问私有属性
#私有方法
class Site:
    name="";
    __age=0;
    def __init__(self,name,age):
        self.name=name;
        self.__age=age;
    def __foo(self):
        return self.name,">>>",self.__age,;
    def foo(self):
        print("这是共有方法",self.__age,end="\n");
        print(self.__foo());
    
site=Site("zsy",20);site.foo();#s.__foo();不能在类的外面调用__foo即私方法
'''
    类的专有方法：
 __init__ : 构造函数，在生成对象时调用__del__ : 
析构函数，释放对象时使用__repr__ : 打印，转换__setitem__ : 
按照索引赋值__getitem__: 按照索引获取值__len__: 获得长度__cmp__:
 比较运算__call__: 函数调用__add__: 加运算__sub__: 
 减运算__mul__: 乘运算__div__: 除运算__mod__:
 求余运算__pow__: 乘方
 '''
os.system('cd E:');print(dir());import shutil;
#copyshutili=shutil.copy("C:\\Users\\Administrator\\Desktop\\testfile.txt", "C:\\Users\\Administrator\\Desktop\\Newtestfile.txt");
#print(copyshutili);    
#os.remove("C:\\Users\\Administrator\\Desktop\\Newtestfile.txt");
testRfind="Theisabcis";
print(testRfind.rfind("is",0,10));print(testRfind[8]);