import socket
import os
import json
import struct

sk = socket.socket()

sk.connect_ex(("127.0.0.1", 9090))

menu = {
        '1': "upload",
        '2': "downloads",
        }
for k, v in menu.items():
    print(k, v)

num = input("choice>>>")

if num == '1':
    dic = {"opt": menu.get(num),
           "filename": None,
           "filesize": None,
           }
    file_path = input("请输入一个绝对路径>>>")
    filename = os.path.basename(file_path)
    filesize = os.path.getsize(file_path)
    dic["filename"] = filename
    dic["filesize"] = filesize
    str_dic = json.dumps(dic)
    len_dic = len(str_dic)
    b_len_dic = struct.pack('i', len_dic)
    sk.send(b_len_dic + str_dic.encode("utf-8"))

    with open(file_path, 'rb') as f:
        while filesize:
            content = f.read(1024)
            sk.send(content)
            filesize -= len(content)

elif num == '2':
    dic = {'opt': menu.get(num),
           'filename': None,
           }
    filename = input("请输入文件名称>>>")
    dic["filename"] = filename
    str_dic = json.dumps(dic)
    len_dic = len(str_dic)
    b_len_dic = struct.pack('i', len_dic)
    sk.send(b_len_dic + str_dic.encode('utf-8'))

    b_result_dic_len = sk.recv(4)
    print(b_result_dic_len)
    result_dic_len = struct.unpack('i', b_result_dic_len)[0]

    result_dic = sk.recv(result_dic_len)
    filesize = json.loads(result_dic.decode('utf-8'))['filesize']
    result = json.loads(result_dic.decode('utf-8'))['result']
    if result == 'success':
        with open(filename, 'ab+') as f:
            while filesize:
                content = sk.recv(1024)
                f.write(content)
                filesize -= len(content)
    else:
        print("文件不存在")

else:
    print("输入错误")