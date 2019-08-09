import socket
import hashlib
import os
import json
from menu import Menu

# menu.show_menu(menu_dict)

# choice = input("\033[34m >>>your choice:\033[0m")
# print(menu_dict[choice])
# while 1:
#     pass


def login(sk):
    name = input("input your name:")
    password_pre = input("input your password:")
    print("*"*50)

    obj5 = hashlib.md5()
    obj5.update(password_pre.encode('utf-8'))
    password = obj5.hexdigest()

    info = (name + " " + password).encode('utf-8')
    sk.send(info)


def operation(sk, cmd):
    info = "3" + " " + cmd
    sk.send(info.encode('utf-8'))
    s_result = sk.recv(10240).decode('utf-8')
    print(s_result)


def upload(sk):
    file_path = input(">>>input filepath:")
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    info = '1 '+file_name+' '+str(file_size)
    sk.send(info.encode('utf-8'))

    # 发送文件的具体内容
    with open('/Users/qing.li/PycharmProjects/hm/README.md', 'rb') as f:
        while file_size:
            content = f.read(1024)
            sk.send(content)
            file_size -= len(content)

    # 接收上传结果
    print(sk.recv(1024).decode('utf-8'))
    print("*" * 50)


def download(sk):
    file_name = input(">>>input filename you want to download:")
    info = '2 ' + file_name
    sk.send(info.encode('utf-8'))
    # 服务端告诉客户端结果：文件是否存在，文件大小等
    s_result = json.loads(sk.recv(1024).decode('utf-8'))
    print(s_result, s_result['is_exist'])
    code = s_result['is_exist']
    if code == 1:
        size = s_result['file_size']
        print(size)
        with open(file_name, 'wb') as f:
            while size:
                content = sk.recv(1024)
                f.write(content)
                size -= len(content)
        print("downloads success!!")
    else:
        print("this file is not exists!")
    print("*" * 50)


if __name__ == '__main__':

    sk = socket.socket()
    sk.connect_ex(("127.0.0.1", 8080))

    menu_dict = {
        '1': '上传文件',
        '2': '下载文件',
    }
    menu = Menu()

    print("connected, please login first!")
    print("=" * 50)

    login(sk)

    while 1:
        s_login = sk.recv(1024).decode("utf-8")

        if not s_login == 'login successful!!!':
            login(sk)
            continue
        else:
            menu.show_menu(menu_dict)
            break
    while 1:
        choice = input(">>>your choice:")
        # 选择操作
        if choice == '1':
            upload(sk)
        elif choice == '2':
            download(sk)
        elif choice.upper() == 'Q':
            sk.send(b'q')
            break
        else:
            # 是否为系统命令，执行操作
            operation(sk, choice)

    sk.close()
