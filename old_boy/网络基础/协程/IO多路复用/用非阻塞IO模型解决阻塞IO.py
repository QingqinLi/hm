import socket
sk = socket.socket()
sk.setblocking(False)
sk.bind(("127.0.0.1", 8080))
sk.listen()

conn_list = []
del_list = []
while 1:
    try:
        conn, addr = sk.accept()
        conn_list.append(conn)
    except BlockingIOError:
        continue
    finally:
        if conn_list:
            for con in conn_list:
                try:
                    msg = con.recv(1024)
                    if msg == '':
                        del_list.append(con)
                        con.close()
                    else:
                        print(msg.decode("utf-8"))
                        con.send(msg.decode("utf-8").upper().encode("utf-8"))
                except (BlockingIOError, ConnectionResetError):
                    continue
            if del_list:
                for l in del_list:
                    conn_list.remove(l)
                del_list = []

sk.close()