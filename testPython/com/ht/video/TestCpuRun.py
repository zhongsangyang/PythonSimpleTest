#!usr/bin/env python
# -*- encoding:utf-8 -*-
'''
import time
def testCpu():
    t0=time.clock();
    for i in range(0,100):
        print(i);
    t1=time.clock();   
    print(t1-t0);   
testCpu(); '''
import sys
import traceback

def bar():
    foo()
 
def foo():
    for _, frame in sys._current_frames().items():
        for line in traceback.extract_stack(frame):
            print (line);print(_);
 
bar()