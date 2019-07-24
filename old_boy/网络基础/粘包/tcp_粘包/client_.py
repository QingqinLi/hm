import socket

sk = socket.socket()

sk.connect_ex(('127.0.0.1', 9090))

msg = sk.recv(1024)
print('a', msg)

msg2 = sk.recv(1024)
print('b', msg2)

sk.close()