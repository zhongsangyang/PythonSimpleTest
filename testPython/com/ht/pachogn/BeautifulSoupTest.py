#!/usr/bin/env python
#-*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<div>
<p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...<a href="javaScript:void(0)">!!!!!!!!!!!!!!!!!!!!!!!!!!</a></p>
</div>
"""
def dayin(arg):
    print(arg);
def callback():
    print("I am a BeautifulSoupTest's callback function");
soup1=BeautifulSoup(html_doc,"html.parser");
'''
print(soup.prettify());print(soup.title);print(soup.title.string);
print(soup.title.parent.name);print(soup.p);'''
dayin(soup1.find_all(["div"],recursive=False));
'''\w  匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。'''
email_id_example = """<br/> 
<div>The below HTML has the information that has email ids.</div>  
abc@example.com
<div>xyz@example.com</div> 
<span>foo@example.com</span> 
"""  
soup2=BeautifulSoup(email_id_example,"lxml");
email_id_regax=re.compile("\b*\w+@\w+\.\w+");
first_email_id=soup2.find(text=email_id_regax);dayin(first_email_id);
all_email=soup2.find_all(text=email_id_regax,limit=2);print(all_email);
print(re.match('com','comwww.runcomoob').group())
print(re.match('com','Comwww.runcomoob',re.I).group())
a = "123abc456"
print(re.search("([0-9]*)(ab|[a-b]*)([0-9]*)",a).group(2))
tt="Tina is a good girl,she is cool,clerver and so on";
rr=re.compile(r"\w*oo\w*");ls=""" "1","2","3","4","5",
"6sfsd" """;
lsnew=ls.split(',')[-1][:-2];print(lsnew);