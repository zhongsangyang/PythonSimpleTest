#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import requests
import chardet
from bs4 import BeautifulSoup
#response=requests.get("http://ww.baidu.com");
#soup=BeautifulSoup(response.text);
#chardet.detect(soup);
'''
print(soup.title.text);
print(soup.body.text)
print(">>>>>>>>>>>>>");
for x in soup.findAll("a"):
    print(x['href'])
'''
soup = BeautifulSoup(requests.get("http://www.zhihu.com").text)
print(soup.findAll("input", {"name": "_xsrf"})['value'])
