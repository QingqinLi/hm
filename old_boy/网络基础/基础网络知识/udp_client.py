import socket

sk = socket.socket(type=socket.SOCK_DGRAM)  # udp协议

name = input("inout your name:")

while 1:
    msg_s = input(">>>")
    info = name + ":" + msg_s
    sk.sendto(info.encode('utf-8'), ("127.0.0.1", 9090))
    # msg_r, addr = sk.recvfrom(1024)
    # print(msg_r.encode('utf-8'))
sk.close()