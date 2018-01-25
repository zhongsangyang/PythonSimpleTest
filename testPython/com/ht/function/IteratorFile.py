#!/usr/bin/env python
#-*- encoding:UTF-8 -*-
from os.path import os
ls=[];
def getFileIterator(path,ls):
    fileList=os.listdir(path);
    try:
        for item in fileList:
            filepath=os.path.join(path,item);
            print(filepath);
            if(os.path.isdir(filepath)==True):
                getFileIterator(filepath, ls);
            elif filepath[filepath.rfind('.')+1:].upper()=='TXT':
                ls.append(item);
    except PermissionError:
        print("没有权限")
    print(filepath);  
path=os.path.normpath("F:/test");
getFileIterator(path, ls);
print(ls);print(len(ls));
        
