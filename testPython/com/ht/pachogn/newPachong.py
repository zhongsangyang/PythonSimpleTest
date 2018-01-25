#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import urllib
import json
import re
import os
from urllib import request
class createImage(object):
    def __init__(self,search_word):
        self.search_word=search_word;
    def create_data(self,offset):
        url = 'http://www.toutiao.com/search_content/?offset={0}&format=json&keyword={1}&autoload=true&count=20&cur_tab=1'.format(offset, urllib.parse.quote(self.search_word))
        try:
            with urllib.request.urlopen(url,timeout=10) as response:
                content=response.read();
        except Exception as e:
            content = None
            print("create data request error",str(e));
        return content;
    def parse_data(self,content):
        if content is None:
            print("内容是空None");
            return;
        try:
            data_list = json.loads(content)['data']
            print(data_list);
            list=[];
            for item in data_list:
                result_dict={'title':item['title']}
                #result_dict = {'article_title': item['title']}
                #print(item,end="\n");
                url_list=[];
                for img in item['image_detail']:
                    url_list.append(img['url']);
                result_dict['imgurl']=url_list;
                list.append(result_dict);
                '''
                ['title':******,'iamge':[1,2,3]]
                '''
        except Exception as e:
            print("parse Error",str(e));
        return list;
    def  save_picture(self,fileTitle,imgurl):
        if imgurl is None or fileTitle is None:
            print("图片地址为空","或者查找的文件名称为空");
            return;
        reg_str = r"[\/\\\:\*\?\"\<\>\|]" 
        fileTitle=re.sub(reg_str,"",fileTitle);
        save_dir='./out/{0}/{1}/'.format(self.search_word, fileTitle);
        if os.path.exists(save_dir) is False:
            os.makedirs(save_dir);
        save_file=save_dir+imgurl.split("/")[-1]+'.png';
        print(save_file);
        if os.path.exists(save_file):
            return
        try:
            with request.urlopen(imgurl,timeout=30) as response,open(save_file,"wb") as fle_save:
                print(imgurl);
                fle_save.write(response.read())
            print("Image is saving {0} fileTitle={1} save_file={2}".format(self.search_word,fileTitle,save_file));
        except Exception as e:
            print("save file error",str(e));
    def go(self):
        while True:
            offset=0;
            listall=self.parse_data(self.create_data(offset)) ;
            if listall is None or len(listall)<=0:
                break;
            try:
                print(listall);
                for i in listall:
                    for li in i['imgurl']:
                        self.save_picture(i['title'], li);
            except Exception as e:
                print("go Exception ",str(e));
            finally:
                offset+=10;
#TO Test isExists Success
test=createImage('美女');
test.go();  