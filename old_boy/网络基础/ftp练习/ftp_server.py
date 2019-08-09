# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""

import socketserver
import subprocess
import os
import json

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
            file_name = "upload_" + option[1]
            file_size = int(option[2])
            # 接收文件具体内容
            if os.path.exists(file_name):
                self.request.send(b"file is already exists,retry!")
            else:
                with open(file_name, 'wb') as f:
                    while file_size:
                        content = self.request.recv(1024)
                        f.write(content)
                        file_size -= len(content)
                self.request.send(b"upload success!")
        elif t == '2':
            file_name = option[1]
            file_path = os.path.join('/Users/qing.li/Desktop', file_name)
            print(file_path)
            if os.path.exists(file_path):
                # 文件存在，告诉客户端文件大小
                file_size = os.path.getsize(file_path)
                info = {'is_exist': 1,
                        'file_size': file_size,
                        }
                self.request.send(json.dumps(info).encode('utf-8'))
                with open(file_path, 'rb') as f:
                    while file_size:
                        content = f.read(1024)
                        self.request.send(content)
                        file_size -= len(content)

            else:
                info = {'is_exist': 2,
                        }
                self.request.send(json.dumps(info).encode('utf-8'))

        else:
            cmd = option[1]
            ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if ret.stdout:
                self.request.send(ret.stdout.read())
            else:
                self.request.send(ret.stderr.read())


server = socketserver.TCPServer(('127.0.0.1', 8080), MySocket)
server.serve_forever()

