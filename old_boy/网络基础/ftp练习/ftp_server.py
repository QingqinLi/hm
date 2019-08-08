# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""

import socketserver
import subprocess
import os

os.chdir("/Users/qing.li/Desktop")


class MySocket(socketserver.BaseRequestHandler):

    def handle(self):
        # 逻辑代码
        while 1:
            flag = self.check_login()
            if not flag:
                self.request.send(b"error, try again~~~")
                # self.check_login()
                continue
            else:
                self.request.send(b'login successful!!!')
                break
        while 1:
            rec_msg = self.request.recv(1024).decode("utf-8")

            if rec_msg == 'q':
                break
            else:
                option = rec_msg.split(" ")
                t = option[0]
                self.opration(t, option)

    def check_login(self):
        msg = self.request.recv(1024).decode('utf-8')
        msg_login = msg.strip().split(" ")
        name = msg_login[0]
        psw = msg_login[1]
        flag = 0
        with open('/Users/qing.li/PycharmProjects/hm/old_boy/网络基础/ftp练习/user_info') as f:
            data = f.readline()
            user_name = data.split("|")[0]
            user_password = data.split("|")[1]
            if name == user_name:
                if user_password == psw:
                    flag = 1
        return flag

    def opration(self, t, option):
        if t == '1':
            pass
        elif t == '2':
            pass
        else:
            cmd = option[1]
            ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if ret.stdout:
                self.request.send(ret.stdout.read())
            else:
                self.request.send(ret.stderr.read())


server = socketserver.TCPServer(('127.0.0.1', 8080), MySocket)
server.serve_forever()

