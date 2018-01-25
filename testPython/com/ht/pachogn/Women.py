#!/usr/bin/env python
#-*- encdoing:utf-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':  
    url = 'http://jandan.net/ooxx'  
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }   
    req = requests.get(url,headers=headers)  
    req.encoding = 'utf-8'  
    html = req.text
    soup = BeautifulSoup(html, 'lxml')  
    #print(soup.prettify());
   
    '''
    targets_url = soup.find_all('a',limit=2) 
    for i in targets_url:
        print(type(i));
#       print(i.get('href'));
#         print(i.attrs);
        print(i.get('class'));
    '''
    allA=soup.find_all('a');
    #print(allA);
    for i in allA:
        #print(i,end="\n");
        print(i.get('href'));
        
        
    
    
  
    
