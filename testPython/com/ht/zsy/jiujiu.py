#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
class PrintTable(object):
    def __init__(self):
        print("打印九九乘法表格")
        self.print99();
    
    def print99(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print("{0} * {1} = {2}".format(j, i,i*j),end="\t");
            print("",end="\n")
if __name__ == '__main__':
    pt=PrintTable();