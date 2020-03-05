from smtplib import SMTP
from poplib import POP3
from time import sleep
import timeit


SMTPADR = 'smtp.mail.qq.com'

smp = SMTP(SMTPADR, 587)
smp.login("1589369708@qq.com", "291518lq")
body_msg = """
From:"1589369708@qq.com"
To:"13263106808@163.com"
Subject: test msg

Hello World!
"""
errs = smp.sendmail("1589369708@qq.com","13263106808@163.com", [body_msg,])
smp.quit()
print(errs)

t = timeit.Timer("s[:8]=='subject:'", 's="subject:xxx"')
print(t.timeit())
