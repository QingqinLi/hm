import socket

sk = socket.socket()

sk.connect_ex(('127.0.0.1', 8080))

msg = input(">>>")
sk.send(msg.encode('utf-8'))

print(sk.recv(1024).decode('utf-8'))

sk.close()