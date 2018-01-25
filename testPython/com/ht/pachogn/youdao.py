#!/usr/bin/env python
#-*- encoding:utf-8 -*-
from urllib import request

if __name__=="__main__":
    req=request.Request("http://www.baidu.com/")
    response=request.urlopen(req);
    #request=urllib.request.urlopen("http://www.baidu.com");
    print("geturl打印信息：%s"%(response.geturl()));
    print('**********************************************');
    print("info打印 信息:%s"%(response.info()));
    print("gcode()打印信息%s"%(response.getcode()));
    