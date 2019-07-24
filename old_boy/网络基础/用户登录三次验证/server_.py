import socketserver
import json
import hashlib


class MySocket(socketserver.BaseRequestHandler):
    def handle(self):
        salt = 'liqing'
        while 1:
            str_dic = self.request.recv(1024).decode('utf-8')
            dic = json.loads(str_dic)
            result = {}
            if not dic['status']:
                with open('info', 'r', encoding='utf-8') as f:
                    for info in f:
                        username, password = info.strip().split("|")
                        print(username, password, dic["username"], username == dic["username"],type(username), type(dic["username"]))
                        if username == dic["username"]:
                            print("test shhsh")
                            md5_obj = hashlib.md5(salt.encode('utf-8'))
                            md5_obj.update(dic['password'].encode('utf-8'))
                            pawd = md5_obj.hexdigest()
                            print(pawd)
                            if password == pawd:
                                result['status'] = True
                            else:
                                result["status"] = False
                                result["reason"] = "密码错误"
                            print(result)
                            break
                    else:
                        result["reason"] = "用户不存在"
                        result['status'] = False
                str_result = json.dumps(result)
                self.request.send(str_result.encode('utf-8'))


server = socketserver.TCPServer(("127.0.0.1", 9090), MySocket)
server.serve_forever()