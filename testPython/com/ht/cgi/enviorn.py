#!C:/Users/Administrator/AppData/Local/Programs/Python/Python36/python.exe  

import os
print("Content-type:text/html");
print();
print('<meta charset=\"utf-8\">');
print("<b>环境变量设置</b><br>");
print("<ul>");
for key in os.environ.keys():
    print('<li><span style="color:green">%30s</span>:%s</li>'%(key,key[os.environ[key]]));
print("<ul>");