import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8080))

sk.listen()
conn, addr = sk.accept()
while 1:
    msg = conn.recv(1024)
    conn.send(msg.decode('utf-8').upper().encode('utf-8'))

conn.close()
sk.close()