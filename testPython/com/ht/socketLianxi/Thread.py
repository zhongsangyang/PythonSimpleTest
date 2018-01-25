#-*- encoding:utf-8 -*-
import time
import _thread
def print_def(theadName,deplay):
    count=0;
    while count<5:
        time.sleep(deplay);
        count += 1
        
        print("%s: %s",(theadName,time.ctime(time.time())));
        
#创建两个线程
try:
    _thread.start_new_thread(print_def,("thread-1", 2));
    _thread.start_new_thread(print_def,("thread-2", 4));

except:
    print("发生了异常");
while 1: 
    pass