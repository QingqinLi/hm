import socketserver


class Mysocket(socketserver.BaseRequestHandler):
    def handle(self):  # 这个方法的名字是固定的，必须是这个名字
        # 收发的逻辑代码(自定义）
        # self.request相当于conn
        msg = self.request.recv(1024).decode('utf-8')
        print(msg)
        self.request.send(msg.upper().encode('utf-8'))


server = socketserver.TCPServer(('127.0.0.1', 8080), Mysocket)  # 固定写法
server.serve_forever()  # 开启一个永久的服务
