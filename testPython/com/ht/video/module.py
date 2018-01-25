#!usr/bin/env python
# -*- encoding:utf-8 -*-
import sys
import os
import glob
import random
from com.ht.function.support import print_func
from urllib.request import urlopen
from idlelib.iomenu import encoding
one ="1";two='2';three=3;
os.system("cd E:\\EclipseWork\\testPython\\com\\ht\\function");print_func("我是");
print(sys.path);print(glob.glob("E:\\EclipseWork\\testPython\\com\\ht\\function\\*.py"));
print(sys.argv);print(random.choice(['pear','apple','banana']));
print(random.sample(["1","2","3","4","5","6","7","8","9","10",],5));#potion arg可以是set，或者list，list效率大于set，
#也可以是range
for line in urlopen("http://blog.csdn.net/weixin_39142498/article/details/79083552"):
    if bytes("EST",encoding="utf-8") in line or bytes("EDT",encoding="utf-8") in line:
        print(line);
    