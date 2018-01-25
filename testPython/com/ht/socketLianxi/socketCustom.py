#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import socket
s=socket.socket();
host=socket.gethostname();
s.connect((host,12345));
print (s.recv(1023));
s.close();
