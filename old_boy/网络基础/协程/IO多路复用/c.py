import socket
sk = socket.socket()

sk.connect_ex(("127.0.0.1", 8080))

while 1:
    msg_s = input(">>>")
    if msg_s == '':
        msg_s = input(">>>")
    elif msg_s == 'q':
        sk.close()
        break
    sk.send(msg_s.encode('utf-8'))
    print(sk.recv(1024).decode('utf-8'))
