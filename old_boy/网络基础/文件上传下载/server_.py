import socket
import json
import time

sk = socket.socket()
sk.bind(('127.0.0.1', 9090))

sk.listen()

conn, addr = sk.accept()

# 通信
str_dic = conn.recv(102400).decode('utf-8')
dic = json.loads(str_dic)
choice = dic['opt']

if choice == 'upload':
    filename = str(int(time.time())) + dic['filename']
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(dic['content'])
    pass
else:
    pass

conn.close()
sk.close()