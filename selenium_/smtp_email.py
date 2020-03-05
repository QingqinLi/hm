# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header

sender_email = '1589369708@qq.com'
sender_pwd = 'timpokbtnauxfidb'
receiver = ["2323270399@qq.com", 'qing.li@moji.com']

server = smtplib.SMTP('smtp.qq.com', 25)


now = time.strftime('%Y-%m-%d %H:%M:%S')
msg = MIMEMultipart()

msg['Subject'] = now + "Test邮件主题"
msg["From"] = sender_email
msg["To"] = Header(",".join(receiver))

text = MIMEText("收到请回复哦")
msg.attach(text)
server.ehlo()
server.login(sender_email, sender_pwd)
result = server.sendmail(sender_email, receiver, msg.as_string())
server.close()
print(result)
"""
1、在发邮件的邮箱中，设置开启smtp服务，获取客户端授权密码
2、邮件群发设置：
    from email.header import Header
    msg["To"] = Header(",".join(receiver))
3、设置服务器：
    server = smtplib.SMTP('smtp.xx.com', 25)
    server.ehlo()
    server.login(sender_email, sender_pwd)
    result = server.sendmail(sender_email, receiver, msg.as_string())
    server.close()
"""
