#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

my_sender="1850148339@qq.com";#发送人
my_pass ="ecikdbwwsldjeagg";#密码
my_user='1850148339@qq.com';#接收者
def mail():
    ret=True;
    content="""
    <p>这是一个测试的文件发送</p>
    <a href="http://www.baidu.com">百度。com</a>
    """;
    type=('plain','html');
    try:
        msg = MIMEMultipart();
        msg['From']=formataddr(['zsy',my_sender]);
        '''括号里的对应发件人邮箱昵称、发件人邮箱账号'''
        msg['To']=formataddr(['xyz',my_user]);
        msg['Subject']='菜鸟教程的标题';
        msg.attach(MIMEText('python发送附件测试…', 'plain', 'utf-8'));
        attch1=MIMEText(open("F:\\test\\test1.txt","rb").read(),"base64","utf-8");
        attch1['Content-Type']='application/octet-stream';
        attch1['Content-Disposition']="attachment";filename="test1.txt";
        msg.attach(attch1);
        # 构造附件2，传送当前目录下的 runoob.txt 文件
        att2 = MIMEText(open("F:\\test\\test2.txt","rb").read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="test2.txt"'
        msg.attach(att2);
        
        server=smtplib.SMTP_SSL("smtp.qq.com",465);
        ''' 发件人邮箱中的SMTP服务器，端口是 25'''
       
        server.login(my_sender, my_pass);
        print(".......");
       
        ''' 括号中对应的是发件人邮箱账号、邮箱密码'''
        server.sendmail([my_sender], [my_user], msg.as_string())
        '''括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件'''
        server.quit();
        
    except Exception:
        ret=False;
        print("出错了");
    return ret;
ret=mail();  
if ret:
    print("发送成功");
else:
    print("发送失败");
