#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import socket
s=socket.socket();
host =socket.gethostname();
port=12345;
s.bind((host,port));
s.listen(5);
conn,addr=s.accept();#连接线路
while True:
    try:
        print(addr,"等待中");
        client_data1=conn.recv(1024);
        print("客户端:",client_data1);
        send_data1=client_data1.upper();
        conn.send(send_data1);
    except Exception:
        break;#异常直接退出
conn.close();