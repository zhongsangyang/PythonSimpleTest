#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
from os.path import os, join
def test():
    testStr="1234isobis";
    print(testStr[3]);
    print(testStr.rfind("is",0,len(testStr)));
    toStr=os.path.join('F:/test/test1.txt','F:/hello/test2.txt','F:/test/test3.txt');
    print(toStr);sq4=("yuanzu1","yuanzu2","yuanzu3");print(":".join(sq4));
def print_func(name):
    pass
    return name
