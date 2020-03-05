import socket
import os

sk = socket.socket()
sk.connect_ex(('127.0.0.1', 9090))

abs_path = input("请输入您的根目录:")
sk.send(abs_path.encode('utf-8'))

current_dir = sk.recv(1024).decode('utf-8')
print(current_dir.split("--"))

while 1:
    cmd = input(">>>")
    if cmd == 'cd':
        filename = input("filename>>>")
        sk.send((cmd + " " + filename).encode('utf-8'))
        result = sk.recv(1024).decode("utf-8").split("--")
        print(result)
    else:
        print("error")

sk.close()