#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
import smtplib
sender="1850148339@qq.com";
revicer=['185014833@qq.com'];
message=MIMEText('Python测试发送内容','plain','utf-8');
message['From']=Header("菜鸟教程",'utf-8');
message['To'] =  Header("测试", 'utf-8')
subject='Python SMTP测试邮件';message['Subject']=Header(subject,'utf-8');
try:
    smtepobj=smtplib.SMTP();
    smtepobj.connect("smtp.qq.com", 25);
    smtepobj.login(sender, "5217079zsy");
    smtepobj.send(sender,revicer,message.as_stirng());
except Exception:
    print("Error 无法发送邮件");
