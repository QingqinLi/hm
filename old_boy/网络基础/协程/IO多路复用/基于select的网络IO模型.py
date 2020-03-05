import select
import socket
sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen()

del_l = []
rlist = [sk]  # 是用来让select来帮忙监听所有接口
# select：windows/linux是监听事件有没有数据到来
# poll:  linux   也可以做select的工作
# epoll: linux   也可以做类似的工作

while 1:
    r, w, x = select.select(rlist, [], [])  # 传参给select，rlist列表中哪个接口有反应，就返回r这个列表
    if r:
        for i in r:  # 循环遍历，看看有反应的接口到底是sk还是conn
            if i == sk:
                """
                如果是sk，就代表有客户端的连接请求
                """
                conn, addr = i.accept()
                rlist.append(conn)  # 把新的客户端的连接。添加到rlist中，继续让select帮忙监听
            else:
                """
                不是sk，就是conn，代表有客户端给我发消息了
                """
                try:
                    msg_r = i.recv(1024).decode('utf-8')
                    if not msg_r:
                        del_l.append(i)
                        i.close()
                    else:
                        print(msg_r)
                        i.send(msg_r.upper().encode('utf-8'))
                except ConnectionResetError:
                    pass
        if del_l:
            for d in del_l:
                rlist.remove(d)
            del_l.clear()



