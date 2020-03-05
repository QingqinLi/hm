# import os
#
# filesize = os.path.getsize('__init__.py')
#
# with open('__init__.py', 'rb') as f:
#     while filesize:
#         content = f.read(1024)
#         sk.send(content)
#         filesize -= len(content)

import socket
import struct
import json
import time
import os

sk = socket.socket()
sk.bind(('127.0.0.1', 9090))

sk.listen()

conn, addr = sk.accept()

b_len_dic = conn.recv(4)
len_dic = struct.unpack('i', b_len_dic)[0]
dic = conn.recv(len_dic)
opt = json.loads(dic.decode('utf-8'))['opt']
filename = json.loads(dic.decode('utf-8'))['filename']

if opt == 'upload':
    filezise = json.loads(dic.decode('utf-8'))['filesize']
    filename = 'uploads_' + filename
    with open(filename, 'ab+') as f:
        while filezise:
            content = conn.recv(1024)
            f.write(content)
            filezise -= len(content)
elif opt == 'downloads':
    file_name_list = os.listdir("/Users/qing.li/PycharmProjects/hm/old_boy/网络基础/大文件的传输下载/")
    for i in range(len(file_name_list)):
        if 'uploads_' in file_name_list[i]:
            file_name_list[i] = file_name_list[i][8:]
    print(file_name_list)
    reply = {}
    if filename in file_name_list:
        reply['result'] = 'success'
        reply['filesize'] = os.path.getsize('uploads_'+filename)
        print('test', reply)
        reply_dic = json.dumps(reply)
        len_reply = len(reply_dic)
        b_len_dic = struct.pack('i', len_reply)
        conn.send(b_len_dic + reply_dic.encode('utf-8'))
        filezise = reply['filesize']

        with open('uploads_'+filename, 'rb') as f:
            while filezise:
                content = f.read(1024)
                conn.send(content)
                filezise -= len(content)

    else:
        reply['result'] = 'failed'
        reply_dic = json.dumps(reply)
        len_reply = len(reply_dic)
        b_len_dic = struct.pack('i', len_reply)
        print("hhhshsh")
        conn.send(b_len_dic + reply_dic.encode('utf-8'))




conn.close()
sk.close()




# a = struct.pack('i', 123)
# print(len(a), struct.unpack('i', a))
