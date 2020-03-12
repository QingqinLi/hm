"""
模块的分类：
    内置模块：安装python解释器的时候就装上的那些方法
    第三方模块／拓展模块：没在安装python的时候就安装的那些功能 在site_packages中存贮
    自定义模块：写的功能如果是一个通用的功能，为了节省代码 可以当成一个模块

模块的功能：
    自己不能完成的功能
        和操作系统交互
        时间
        随机数
        和网络通信
    别人写好的功能
        分类 管理
        节省内存
        提供更多的功能
通常是 文件夹／py文件／c语言编译好的一些编译文件

import 这个语句相当于执行了导入的文件
不会被重复导入

命名：满足变量命名的规范 一般情况下 都是小写字母开头得到

(1、找到这个模块
2、创建一个属于这个模块的内存空间
3、执行模块
4、将这个模块所在内训空间建立一个和my_moudle之间的引用关系（不会和本文件的变量／函数混淆）--- 需要执行完才能创建引用关系
)

规则
    模块的重命名 import my_moudle as moudle
    导入多个模块 可以写在一行 但是PEP8 不推荐，需要多行导入
    所有的模块导入都应该尽量放在这个文件的开头
    导入顺序：先导入内置模块 在导入第三方模块 最后导入自定义的模块

模块的搜索路径全部存储在sys.path列表中；导入模块的顺序，是从前到后找到一个符合条件的模块就立即停止不再向后寻找
    如果要导入的模块和当前执行的文件同级：直接导入即可
    如果要导入的模块和当前执行的文件不同级：需要把导入模块的绝对路径添加到sys.path列表中
"""

# 要导入一个py文件的名字 但是不加.py后缀
# import my_module
#
# my_module.login()

"""
模块 
from ... import 仍然相当于执行了整个py文件
    导入了什么就能使用什么，不导入的变量不能使用
    （1、找到这个模块
    2、开辟一块属于这个模块的命名空间
    3、执行这个模块
    4、在本文件中创建一个变量指向模块命名空间中导入的具体的内容（不导入并不代表不存，而是没有建立当前文件到模块中其他名字的引用）
    ）
    当当前文件中同名的eg.函数的时候，相当于变量的重新赋值，所以使用的是本命名空间的内容
    
    当模块中导入的方法或者变量 和本文件中有重名的时候 那么这个名字只代表最后一次对它赋值的那个方法或者变量
    在本文件中对全局变量的修改完全不会影响到模块中的变量引用的
    
    重命名 from ... import a as b 其实重新命名的是把a重命名成b
    导入多个 from ... import a,b
    导入多个重命名 from ... import a as a1,b as b1
    导入所有 from ... import *
        * 和 __all__的相关性：__all__可以控制*导入的包 ：在被导入模块中__all__ = [函数，变量]

模块相关的其他知识
    把模块当成脚本运行 反射本模块中的变量
        运行py的两种方式：1、以模块的方式运行 import xxx  2、直接运行（pycharm, cmd)---以脚本的形式运行
                        __name__内置变量 本文件__main__(当前正在执行的文件）,其他文件名 
                        if __name__ == "__main__" 在编写py文件的时候所有不在函数和类中封装的内容都应该写在if __name__ == "__main__"中（不需要调用就能执行的内容）
                        写了if __name__ == "__main__"被当作模块导入的时候不执行
                        sys,modules 存储类所有导入的文件的名字和这个文件饿内存地址{文件名：文件地址}
    重新加载模块
    pyc模块和重新加载模块
        当一个文件被当作模块导入的时候，就会在这个文件所在目录的__pycache__下生成一个编译好的文件，为了之后导入这个文件的时候直接读编译好的pyc文件就可以节省一些导入时候的时间
        import importlib  importlib.reload(aaa)---不用与正式开发（reloads可以强制重新加载）实际上import之后对导入模块的修改在不会影响本模块（在程序运行的过程中）
        
模块的循环引用：（互相导入）
    在模块的导入中不要产生循环引用问题 如果发生循环导入了 就会报错（写在本类中的方法提示不存在）
    
import module 使用：module.名字 
from mudle import name 直接使用

sys.path:查看系统路径 自定义模块能否被导入，就看sys.path列表中有没有这份模块所在的绝对路径 MoudleNotFoundError
sys.path.append()
文件的导入都是相对于当前执行的文件的，相当于把要导入的模块的代码都在当前执行的文件中执行


__file__ 当前文件的绝对目录
包：至少有__init__.py,集合类一组py文件，提供了一组复杂的功能
    为什么会有包：当提供的功能比较复杂，一个py文件无法完成的时候
    导入模块
        import a.b.xxx 点的左边都是包 用a.b.xxx（模块）.变量使用
        import a.b.c as d 用d使用相关的内容
        from package import moudle 直接使用
    导入包（相当于执行了包下面的__init__.py文件，并不会帮你把这个包下面的其他包以及py文件自动的导入到内存中 需要自己处理__init__文件【才能保证导入包的时候可以使用模块,保证导入的包都在sys.path下]）
        
        自己处理__init__文件    
            绝对路径 from xxx import xxxx
            相对路径 from . import xxxx
                使用了相对导入的模块只能被当作模块执行
    

简单的导入 平时

复杂的模块 读框架源码的时候

"""
# from my_module import login as b
#
#
# def login():
#     print("in my login")
#
# login()
# b()

# from my_module import login
# # 此时login这个变量重新赋值成了导入模块中的login
#
# login()
#
# print(__name__)
# print(__file__)


"""
重新加载模块：
    已经导入的模块即便被修改在程序执行过程中也不会生效# 
    当一个文件作为一个脚本被导入的时候
    # 就会在这个文件所在的目录的__pycache__下生成一个编译好的文件
    # 为了之后导入这个文件的时候直接读这个编译好的pyc文件就可以
    # 可以节省一些导入时候的时间
importlib.reload(modules) 表示重新加载 因为在import之后 再修改这个被导入的模块程序感知不到；reload这种方式可以强制程序重新导入这个模块一次（不推荐使用）

    
"""

"""
反射自己模块：
import sys
getattr(sys.modules[__name__], 变量名）
"""

"""
random模块
小数: random.random()0-1/random.uniform(n,m)n-m
整数：random.randomint(m, n) m-n 包括n/random.randomrange(m,n) 不包括n/random.randrange(m ,n ,t) 设置步长
随机抽取：random.choice(可迭代) 单个／random.sample(iter,n) 抽取n个-返回一个列表
打乱顺序: random.shuffle()
    
"""
# import random
# # print(random.random(), random.uniform(7, 9), random.randint(1, 2), random.randrange(1, 2), random.randrange(1, 10, 2))
# l = [1, 3, 4, 'sss']
# print(random.choice(l), random.sample(l, 2))
# random.shuffle(l)
# print(l)


"""
time  时间模块
    时间戳时间：格林威治时间，float时间 给机器用的 1970.1.1 0:0:0
    结构化时间 时间对象 是上下两种格式的中间状态 可以通过.属性名来获取对象中的值
    格式化时间 字符串时间 str数据类型 给人看的
    时间戳time.time <-mktime-结构化time.localtime <-strptime-格式化时间time.strftime
    
"""
import time
# # 时间戳
# print(time.time())

# 格式化时间
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# print(time.strftime("%Y-%m-%d %A %H:%M:%S"))
# print(time.strftime("%c"))

# 时间 对象结构的
time_obj = time.localtime()
print(time_obj.tm_year)
print(time.localtime(1500000000))

# time_obj = time.localtime(2500000000)
# print(time.strftime("%Y-%m-%d %H:%M:%S", time_obj))
#
# # 字符串格式时间转换为时间戳时间
# struct_time = time.strptime('2019-03-22 12:26:40', '%Y-%m-%d %H:%M:%S')
# print(time.mktime(struct_time))

# 计算本月一号的时间戳
# 结构化时间
print("*"*10)
struct_time = time.localtime()
struct_time = time.strptime("%s-%s-1" % (struct_time.tm_year, struct_time.tm_mon), "%Y-%m-%d")
timestamp = time.mktime(struct_time)
print(timestamp)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp)))
#
# # 格式化时间
# ret = time.strftime("%Y-%m-01")
# struct_time = time.strptime(ret, "%Y-%m-%d")
# print(time.mktime(struct_time))


"""
sys模块 和python解释器打交道的
"""
# import sys
# # print(sys.path)
# # print(sys.modules)
# # print(sys.platform)
#
# # 主动退出程序
# exit()
# # sys.argv 系统参数 返回的是一个列表， 第一个参数是执行这个文件的时候 写在python后面的第一个值 之后的元素 在执行python的时候可以写多个值
# # 都会依次被添加到列表中
# print(sys.argv[0])

"""
os 模块
    # mkdir/rmdir/makedirs/removedirs/listdir
    # remove/rename
    # system popen
    # path : join  split basename dirname abspath isdir isfile getsize
    

"""
import os

# print(os.getcwd())  # 在哪执行这个文件，getcwd的结果就是这个路径（不是文件的存储路径，而是执行文件的路径）
# print(__file__)
# os.chdir("/Users/qing.li/Desktop")  # 切换路径
# print(os.getcwd())  # 获取当前路径
#
# print(os.curdir, os.pardir)  # 永远都是。 .. 一般不会用到

# 创建文件夹／删除文件夹
# os.mkdir('dir/dir1')  #创建文件夹 不能创建上层目录不存在的多层目录
# os.rmdir('dir/dir2')  # 删除一个文件夹 但是不能删除一个非空的文件夹
# os.removedirs('dir/dir2/dir3/dir4')  # 递归向上删除文件夹,只要删除当前目录之后，发现上一级的目录为空，就把上一级的目录也删除掉，如果发现上一级的目录中有其他文件，就停止删除

# print(os.listdir(os.getcwd()))  # 查看给定目录下的文件，返回的是一个list
# print(os.stat("dir"))  # 查看给定目录的文件信息
# print(os.sep)  # 查看当前操作系统的目录分割符
# print([os.linesep])  # 查看当前操作系统的行终止符 （放在列表中可以让输出内容"原形毕露"）
# print(os.pathsep)  # 查看当前操作系统分割文件路径的字符串
# print(os.name)  # 查看当前使用的平台 win->'nt'; Linux->'posix'

# os.system("ls")  # 执行系统命令
# ret = os.popen("pwd")  # 查看当前路径 查看某些信息
# print(ret.read())

# print(os.environ)  # 相当于环境变量的部分

# print(os.path.abspath("dir"))  # 查看文件的绝对路径
# print(os.path.split("/Users/qing.li/PycharmProjects/hm/old_boy"))  # 返回一个元祖上层目录，文件/文件夹目录
# print(os.path.dirname("/Users/qing.li/PycharmProjects/hm/old_boy"))  # 返回当前地址的上层目录
# print(os.path.basename("/Users/qing.li/PycharmProjects/hm/old_boy/dir"))  # 返回当前文件的最后一层目录／文件
# print(os.path.exists("/Users/qing.li/PycharmProjects/hm/old_boy/dir1"))  # 判断路径是否存在
# print(os.path.isfile("/Users/qing.li/PycharmProjects/hm/old_boy/dir"))  # 判断目录是否为文件
# print(os.path.isdir("/Users/qing.li/PycharmProjects/hm/old_boy/dir"))  # 判断当前目录是否为文件夹

# ret = os.path.join('/Users/qing.li/PycharmProjects/hm/old_boy/dir', 'aaa', 'vvv')
# print(os.path.abspath(ret))
#
# print(os.path.getsize("/Users/qing.li/PycharmProjects/hm"))  # 查看大小
# #


'''
hashlib模块：
    摘要算法的模块， 能够把一个字符串数据类型的变量，转换成一个定长的密文的字符串，这个字符串中的每一个字符都是一个十六进制的数字
    对于同一个字符串，不管这个字符串有多长，只要是相同的，无论在任何环境下，多少次的执行，在什么语言中，只要使用相同的算法／手段 得到的结果永远是相同的，只要不是相同的字符串，得到的结果一定是不同的
    密文是不可逆的
md5算法：
    生成一个32位的字符串，每一个字符都是16进制，效率快，算法相对简单
    关于md5解密：撞库（实际不是真的破解，是把常用的对应关系记录在数据库中，查询）
    加盐: 不仅是对要加密的字符串加密，还加入一个其他的字符串
sha1算法：
    生成一个40位的字符串，每个字符都是十六进制的算法相对复杂。计算速度慢，安全系数相对较高
'''
import hashlib

# md5的加密过程
s = 'alex1321'
# md5_obj = hashlib.md5()
# md5_obj.update(s.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res)

# 防撞库
# 加盐
# md5_obj = hashlib.md5('我加的盐'.encode('utf-8'))
# md5_obj.update(s.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res)

# 动态加盐（用户名+密码）
# username = input("username:")
# password = input("password:")
# md5_obj = hashlib.md5(username.encode('utf-8'))
# md5_obj.update(password.encode('utf-8'))
# md5 = md5_obj.hexdigest()
# print(md5)

# sha1算法
# sha_obj = hashlib.sha1()
# sha_obj.update("test".encode('utf-8'))
# print(sha_obj.hexdigest())

# 文件的一致性校验
# md5_one = hashlib.md5()
# with open('json_dump', 'rb') as f:
#     md5_one.update(f.read())
#     ret1 = md5_one.hexdigest()
#
# md5_two = hashlib.md5()
# with open('pickle_demo', 'rb') as f:
#     md5_two.update(f.read())
#     ret2 = md5_two.hexdigest()
#
# print(ret1, ret2)

# 如果要对比的文件特别大，内存装不下的情况（文本，视屏， 音乐， 图片 bytes）按行读／按字节读
# md5_obj = hashlib.md5()
# md5_obj.update('hello,'.encode('utf-8'))
# md5_obj.update('alex,'.encode('utf-8'))
# md5_obj.update('sb'.encode('utf-8'))
# print(md5_obj.hexdigest())
#
# md51 = hashlib.md5()
# md51.update("hello,alex,sb".encode('utf-8'))
# print(md51.hexdigest())

# 大文件的一致性校验
md5_obj = hashlib.md5()
with open('29_正则表达式.py', 'rb') as f:
    while True:
        c = f.read(10240)
        if len(c) > 0:
            md5_obj.update(c)
        else:
            break

    print(md5_obj.hexdigest())
#
# md51 = hashlib.md5()
# with open('29_正则表达式.py', 'rb') as f:
#     md51.update(f.read())
#     print(md51.hexdigest())


"""
configparser模块
    一个固定格式的配置文件，有一个对应的模块去帮你做这个文件的字符串处理
    default 模块中的内容可以在任意其他模块中找到
    读文件的时候需要先read()再操作
"""
import configparser

# config = configparser.ConfigParser()
# # config["DEFAULT"] = {'ServerAliveInterval': '45',
# #                      'Compression': 'yes',
# #                      'CompressionLevel': '9',
# #                      'ForwardX11': 'yes',
# #                      }
# # config["bitbucket.org"] = {'user': 'alex'}
# #
# # config['topsecret.server.com'] = {'Host Port': '50022', 'ForwardX11': 'no'}
# #
# # with open('example.ini', 'w') as f:
# #     config.write(f)

# config = configparser.ConfigParser()
# print(config.read('example.ini'))
# print(config.sections())
# print('bitbucket.org' in config)
# print(config['bitbucket.org']['user'])
# print(config['bitbucket.org']['compression'])
# print(config['bitbucket.org'])
# for key in config['bitbucket.org']:
#     print(key)
# print(config.options('bitbucket.org'))  # 同for循环，找到所有的键，输出为list
# print(config.items('bitbucket.org'))  # 找到所有的键值对
# print(config.get('bitbucket.org','compression'))  # 获取键对应的值

"""
logging模块
    功能：日志格式的规范，操作的简化，日志的分级管理
    需要自己定义日志的级别，内容
    使用： 
        普通配置型： 简单的，可定制化差
        对象配置型： 复杂的，可定制化强
        
    basicConfig:不能讲一个log信息既输出到屏幕，又输出到文件
    logger对象的形式：
        创建一个logger对象
        创建一个文件管理操作符
        创建一个屏幕管理操作符
        创建一个日志输出的格式
        
        文件管理操作符 绑定一个格式
        屏幕管理操作符 绑定一个格式
        
        logger对象 绑定 文件管理操作符
        logger对象 绑定 屏幕管理操作符
        
        
"""
import logging

# logging.basicConfig(level=logging.DEBUG)  # 设置日志打印的级别，从DEBUG级别开始打印
# logging.debug('debug message')  # 调试模式
# logging.info("info message")  # 基础信息
# logging.warning("warning message")  # 警告
# logging.error("error message")  # 错误
# logging.critical("critical meaage")  # 严重错误

#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log')  # 设置日志打印的级别，从DEBUG级别开始打印
# # logging.basicConfig(level=logging.DEBUG,
# #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
# #                     datefmt='%a, %d %b %Y %H:%M:%S',
# #                     filename='test.log')
# logging.debug('debug message')  # 调试模式
# logging.info("info message")  # 基础信息
# logging.warning("warning message")  # 警告
# logging.error("error message")  # 错误
# logging.critical("critical meaage")  # 严重错误

# 创建一个文件对象
# logger = logging.getLogger()
#
# # 创建一个文件管理符
# fh = logging.FileHandler('logger.log', encoding='utf-8')
#
# # 创建一个屏幕管理操作符
# sh = logging.StreamHandler()
#
# # 创建一个日志输出的格式
# format1 = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s - %(message)s")
#
# # 文件管理操作符 绑定一个格式
# fh.setFormatter(format1)
# # 屏幕管理操作符 绑定一个格式
# sh.setFormatter(format1)
#
# logger.setLevel(logging.DEBUG)
#
# logger.addHandler(fh)
# logger.addHandler(sh)
#
# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warn message")
# logger.error("error message")
# logger.critical("critical message")

"""
collections模块
    数据类型的拓展模块
    队列 queue：先进先出
    双端队列 deque：
        append 往队列右边添加值
        appendleft 往队列左边添加值
        pop 从队列右侧弹出值
    总结：在insert，remove的时候 deque的平均效率高于列表； 列表根据索引查看某个值的效率高与deque；append和pop对于列表的效率是没有影响的
"""
# import queue
# q = queue.Queue()
# print(q.qsize())
# q.put(1)
# q.put("aaa")
# q.put([1,2,3])
# print(q.qsize())
# print(q.get())

from collections import deque
dq = deque()
dq.append(1)
dq.append("aaa")
dq.appendleft("vvvv")
dq.append("hhh")
# print(dq)
# print(dq.pop())
# print(dq.popleft())
print(dq)
print(dq.remove('aaa'))
print(dq)
print(dq.insert(0, 'abc'))
print(dq)