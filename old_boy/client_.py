import socket

sk = socket.socket()

sk.connect(('192.168.38.162', 9999))

sk.send(b'hello')
sk.send('中文'.encode('utf-8'))

sk.close()