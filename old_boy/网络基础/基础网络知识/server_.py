import socket
import time

sk = socket.socket()  # 默认为网络类型的的，TCP协议

sk.bind(('192.168.38.162', 9999))  # 端口的范围是0-65535， 但是0-1023不能用
sk.listen()  # 监听
# 接收客户端的连接
while 1:
    conn, addr = sk.accept()
    while 1:

        msg = conn.recv(1024)  # 接收10个字节的数据
        print(msg.decode('utf-8'))

        if msg.decode('utf-8') == 'q':
            break
        print(conn, addr)
        msg_my = input(">>>")
        conn.send(msg_my.encode("utf-8"))

        if msg_my == 'q':
            break

    conn.close()
    time.sleep(3)
    break

sk.close()

# 改成一直聊天的逻辑，并且带标志的退出 试试群聊