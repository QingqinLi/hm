"""
得到一个字符串的结果，过程就叫做序列化
字典，列表，数字，对象----（序列化） -> 字符串
序列化：列表 元祖 字符串
字符串 ---（反序列化） --> 列表，元祖，字符串
为什么要序列化：1、把内容写入文件。2、网络传输数据
eval()不能随便用 容易有各种安全问题
"""

"""
json 模块
    loads, str ---> list, dict
    load, 从文件读
    dumps, list,dict--->str
    dump 写入文件
    能处理的数据类型：有限，限制比较多
    能使用的语言；所有语言
    限制：json格式的key必须是字符串数据类型的（如果是数字类型的，dump（s）之后会强行专程字符串数据类型，字符串只能是" 
       对于value是元祖的字典转换之后会把元组强制转换为list,不支持元组做key
       set不能被dump／dumps
"""
import json

# dic = {'aaa': 'bbb',
# #        1: 'ddd',
# #        }
# dic = {'aaa': 'bbb',
#        'bbb': (1, 3),
#        }
# str_dic = json.dumps(dic)
# print(dic)
# print(type(str_dic), str_dic)
# print(type(json.loads(str_dic)), json.loads(str_dic))
#
# with open('json_dump', 'w') as f:
#     json.dump(dic, f)
#
# with open('json_dump') as f:
#     print(json.load(f))

# lst = [1, 2, 'aaa', 'bbb', 34]
# print(json.dumps(lst))
# with open('json_dump_list', 'w') as f:
#        json.dump(lst, f)
#
# with open('json_dump_list') as f:
#        print(json.load(f))

# dump多个数据到文件中  可以dump进文件，但是不能load出来,要json多条数据，使用dumps转换再写进文件中
# dic = {'aaa': 'bbb',
#        'ccc': 'ddd',
#        }
# lst = [1, 3, 5, '45', 'ss']
#
# with open('json_dump_mix', 'w') as f:
#     # json.dump(dic, f)
#     # json.dump(lst, f)
#     str_dic = json.dumps(dic)
#     str_lst = json.dumps(lst)
#     f.write(str_dic + "\n")
#     f.write(str_lst + "\n")
#
# with open('json_dump_mix') as f:
#     # print(json.load(f))
#     for line in f:
#         print(json.loads(line))

# 中文格式的，ensure_ascii = false
# dic = {'abc':(1,2,3),'country':'中国'}
# ret = json.dumps(dic, ensure_ascii=False)
# print(ret)
# print(json.loads(ret))
#
# with open('jsn_demo', 'w', encoding='utf-8') as f:
#     json.dump(dic, f, ensure_ascii=False)


# json的其他参数 为了用户看着方便 但是浪费存储空间
# data = {'username':['李华','二愣子'],'sex':'male','age':16}
# json_dic2 = json.dumps(data, sort_keys=True,indent=4,separators=('.',':'),ensure_ascii=False)
# print(data)
"""
pickle
    dump的结果是bytes， dump用的f文件句柄需要以wb的形式打开，load所用的f是rb模式，支持所有对象的序列化 对于对象的序列化需要这个对象对应的类在内存中
    对于多次dump／load的操作都有良好的处理, pickle几乎支持所有对象
    dumps
    loads
    dump
    load
    
"""
import pickle
# dic = {1:(12,3,4),('a','b'):4}
# pic_dic = pickle.dumps(dic)
# new_dic = pickle.loads(pic_dic)
# print(pic_dic, new_dic)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# alex = Student("alex", 83)
# ret = pickle.dumps(alex)
# print(ret)
# print(pickle.loads(ret).name)

# with open('pickle_demo', 'wb') as f:
#     pickle.dump(alex, f)
# with open('pickle_demo', 'rb') as f:
#     print(pickle.load(f).name)
#

# with open('pickle_demo','wb') as f:
#     pickle.dump({'k1':'v1'}, f)
#     pickle.dump({'k11':'v1'}, f)
#     pickle.dump({'k11':'v1'}, f)
#     pickle.dump({'k12':[1,2,3]}, f)
#     pickle.dump(['k1','v1','l1'], f)
#
# with open('pickle_demo','rb') as f:
#     while True:
#         try:
#             print(pickle.load(f))
#         except EOFError:
#             break


"""
shelve
    如果你写定了一个文件 改动的比较少，读文件的操作比较多，而且你大部分的读取都需要基于某个key获取value，可以用shelve
"""
import shelve
f = shelve.open('shelve_demo')
f['key'] = {'ke': (1,2,3), "k2": 'v2'}
f.close()

f = shelve.open('shelve_demo')
content = f['key']
f.close()
print(content)