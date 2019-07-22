import socket
import time

sk = socket.socket()  # 默认为网络类型的的，TCP协议

sk.bind(('192.168.38.162', 9999))  # 端口的范围是0-65535， 但是0-1023不能用
sk.listen()  # 监听

conn, addr = sk.accept()  # 接收客户端的连接

msg = conn.recv(10)  # 接收10个字节的数据
print(msg.decode('utf-8'))

print(conn, addr)
time.sleep(3)

conn.close()
sk.close()

# 改成一直聊天的逻辑，并且带标志的退出 试试群聊