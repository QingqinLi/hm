import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))

while 1:
    print("msg1", sk.recvfrom(5))
    print("msg2", sk.recvfrom(5))

sk.close()