import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(5)

while 1:
    conn, addr = sk.accept()
    data = conn.recv(10000).decode('utf-8')
    print(data)
    conn.send(b"HTTP:/1.1 200 OK liqing\r\n\r\n")
    with open('html/获取用户输入的标签.html', 'rb') as f:
        conn.send(f.read())
    conn.close()

sk.close()