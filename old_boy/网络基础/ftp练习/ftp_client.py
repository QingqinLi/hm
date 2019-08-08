import socket
import hashlib
from menu import Menu

sk = socket.socket()
sk.connect_ex(("127.0.0.1", 8080))

menu_dict = {
             '1': '上传文件',
             '2': '下载文件',
             }
menu = Menu()
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
        pass
    elif choice == '2':
        pass
    elif choice.upper() == 'Q':
        sk.send(b'q')
        break
    else:
        # 是否为系统命令，执行操作
        operation(sk, choice)


sk.close()

