#!usr/bin/env python
#-*- encoding:utf-8 -*-
import socket
from idlelib.iomenu import encoding
s=socket.socket();
host=socket.gethostname();
port=12345;
s.connect((host,port));
while True:
#           if len(sendMessgeTo)==0:continue;
    try:
        sendMessgeTo = input("=>:").strip() #等待客户端输入  
        if len(sendMessgeTo) == 0: continue #防止服务端死循环  
        s.send(bytes(sendMessgeTo,encoding="utf-8"));
        replaystr=str(s.recv(1024),encoding="utf-8");
        print("服务器传过来的数据为:",replaystr);
    except Exception:
        print("出项了异常");
s.close();   
