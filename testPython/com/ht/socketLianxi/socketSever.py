#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import socket
s=socket.socket();
host=socket.gethostname();
port=12345;
s.bind((host,port));
s.listen(5);
while True:
    c,addr = s.accept();
    c.send('zzz');
    c.close();
    


    