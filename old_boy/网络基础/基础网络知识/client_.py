import socket

sk = socket.socket()

sk.connect(('192.168.38.162', 9999))

while 1:
    msg = input(">>>")

    sk.send(msg.encode('utf-8'))

    if msg == 'q':
        break

    msg_server = sk.recv(1024)
    print(msg_server.decode('utf-8'))
    if msg_server.decode('utf-8') == 'q':
        break

sk.close()