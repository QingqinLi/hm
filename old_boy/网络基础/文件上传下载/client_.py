import socket
import os
import json

sk = socket.socket()
sk.connect_ex(('127.0.0.1', 9090))

menu_dic = {'1': 'upload',
            '2': 'download',
            }
for k, v in menu_dic.items():
    print(k, v)

choice = input("choice: ")

if choice == '1':
    # 上传功能，dic = {要执行的操作， 文件名， 文件内容} /Users/qing.li/PycharmProjects/hm/old_boy/基础知识/00_基础知识.py
    dic = {'opt': menu_dic.get(choice),
           'filename': None,
           'content': None
           }
    file_path = input('文件的绝对路径>>>')
    file_name = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    dic['filename'] = file_name
    dic['content'] = content

    str_dic = json.dumps(dic)
    sk.send(str_dic.encode('utf-8'))

elif choice == '2':
    pass

else:
    print("选择错误")






sk.close()