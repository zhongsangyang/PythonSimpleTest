#!/usr/bin/env python
#-*- encoding:UTF-8 -*-
import urllib.request
#网址
url="http://www.douban.com/";
#请求
request=urllib.request.Request(url);
response=urllib.request.urlopen(url);
data=response.read();data=data.decode("utf-8");
print(data);print(type(response))  
print(response.geturl())  
print(response.info())  
print(response.getcode())

