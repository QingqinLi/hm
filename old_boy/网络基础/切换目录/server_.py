import socket
import os
import subprocess

sk = socket.socket()
sk.bind(('127.0.0.1', 9090))

sk.listen()
conn, addr = sk.accept()


def send_data(conn, path):
    list_dir = os.listdir(path)
    str_dir = "--".join(list_dir)
    conn.send(str_dir.encode('utf-8'))


abs_path = conn.recv(1024).decode('utf-8')
current_dir = abs_path + '/'
# os.chdir(current_dir)

send_data(conn, current_dir)
while 1:
    result_cmd = conn.recv(1024).decode('utf-8')
    print(result_cmd, result_cmd.split(" "))
    print(result_cmd.split(" ")[0] == 'cd')
    if result_cmd.split(" ")[0] == 'cd':
        file_name = result_cmd.split(" ")[1]
        current_dir += file_name + "/"
        print(current_dir)
        cmd = "cd" + " " + current_dir
        print('test' + cmd)
        if os.path.isdir(current_dir):
            send_data(conn, current_dir)
        else:
            conn.send(b"is not a file package")
        # print(r.stdout.read().decode('utf-8'), r.stderr.read().decode('utf-8'))
    elif result_cmd.split(" ")[0] == '..':
        # 返回上一级目录
        pass

conn.close()
sk.close()