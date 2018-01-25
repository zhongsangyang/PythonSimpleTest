#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
import json
import demjson
ls=[];
a='a';
start=ord(a);
c=start+5;
dict={};
k=1;
for i in range(start,c):
    dict[chr(i)]=k;
    k+=1;
ls.append(dict);
print(ls); nls=[{'a':'中','b':'国'}];
z = json.dumps(ls);text=json.loads(z);
print (json.dumps(nls, sort_keys=True,ensure_ascii=False, indent=4, separators=(',', ': ')));
print(text);
thirdJson=demjson.encode(ls,'gbk');print(thirdJson);
thirdDecode=demjson.decode(thirdJson, "utf-8");print(thirdDecode);
