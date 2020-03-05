import socket

sk = socket.socket()

sk.connect_ex(('127.0.0.1', 8080))

while 1:
    msg = input("input your order:")
    sk.send(msg.encode('utf-8'))
    if msg == 'q':
        break
    result = sk.recv(1024).decode('utf-8')
    print(result)

sk.close()