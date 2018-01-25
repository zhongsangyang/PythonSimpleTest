#!/usr/bin/env python
#-*- encoding:utf-8 -*-
from urllib import request, response
import chardet
if __name__=="__main__":
    response=request.urlopen("http://www.baidu.com");
    html=response.read();
    html=html.decode("utf-8");
    html=chardet.detect(bytes(html,encoding="utf-8"));
    print(html);
    

