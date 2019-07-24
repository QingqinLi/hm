import socket
import hashlib
import json

sk = socket.socket()

sk.connect_ex(('127.0.0.1', 9090))

dic = {'status': False,
       'username': None,
       'password': None
       }
circle = 3
while circle:
    username = input("username>>>")
    password = input("password>>>")

    md5_obj = hashlib.md5(password.encode('utf-8'))
    md5_obj.update(username.encode('utf-8'))
    pass_md5 = md5_obj.hexdigest()

    dic['username'] = username
    dic['password'] = pass_md5
    str_dic = json.dumps(dic)
    sk.send(str_dic.encode('utf-8'))

    result_dic = sk.recv(1024).decode('utf-8')
    print(result_dic)
    result = json.loads(result_dic)

    if result['status']:
        print("success")
    else:
        print("fail because %s" % result['reason'])

    circle -= 1


# md5_obj = hashlib.md5("liqing".encode('utf-8'))
# md5_obj.update("d79164e768c7514c862e97ceb42f7779".encode("utf-8"))
# print(md5_obj.hexdigest())
#
# import hmac
#
# # hmac实现加密
# md5_obj = hmac.new("liqing".encode('utf-8'))
# result = md5_obj.hexdigest()
# print(result)
# md5_obj = hashlib.md5('liqing'.encode('utf-8'))
# md5_obj.update('cb00b0d12772c0dec783906adeae5d7f'.encode('utf-8'))
# pass_md5 = md5_obj.hexdigest()
# print(pass_md5)