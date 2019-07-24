"""
udp协议 可以实现多个客户端和一个服务端同时通信
"""
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)  # udp协议

sk.bind(("127.0.0.1", 9090))

# 按照名字 显示不同的颜色
color_dic = {'alex': '\033[32m',
             'boss': '\033[35m',
             'xiaoxue': '\033[38m',
             }

while 1:
    msg_r, addr = sk.recvfrom(1024)  # 接收来自哪里的消息
    name = msg_r.decode('utf-8').split(':')[0].strip()
    print(color_dic.get(name, 'None'), msg_r.decode('utf-8'))
    msg_s = input(">>>")
    sk.sendto(msg_s.encode('utf-8'), addr)  # 指定是发给谁的消息

sk.close()