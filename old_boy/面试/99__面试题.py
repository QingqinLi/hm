"""
# 一个类
# 对象的属性 : 姓名 性别 年龄 部门
# 员工管理系统
# 内部转岗 python开发 - go开发
# 姓名 性别 年龄 新的部门
# alex None 83 python
# alex None 85 luffy

# 1000个员工
# 如果几个员工对象的姓名和性别相同,这是一个人
# 请对这1000个员工做去重

先把自己可以写的部分完成
因为要去重， 所以想到用set， set的实现原理是hash，保证hash的部分是要比较的部分 因为hash之后如果存贮的值不同还要去比较值，如果值不一样就会
重新hash，保证不同的值存到不同的内存空间中，所以需要重写__eq__ 保证用==比较的是需要比较的部分 重写__str__ 打印查看对象的具体内容
"""


# class Employee:
#     def __init__(self, name, sex, age, development):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.development = development
#
#     def __hash__(self):
#         return object.__hash__(self.name + self.sex)
#
#     def __eq__(self, other):
#         if self.name == other.name and self.sex == other.sex:
#             return True
#         return False
#
#     def __str__(self):
#         return "%s  %s  %s  %s" % (self.name, self.sex, self.age, self.development)
#
#
# employee_list = []
# for i in range(200):
#     employee_list.append(Employee("alex", "man", i, "python"))
# for i in range(300):
#     employee_list.append(Employee("wusir", "women", i, "python"))
# for i in range(500):
#     employee_list.append(Employee("taibai", "women", i, "python"))
#
# result = set(employee_list)
# for i in result:
#     print(i)

#  生成随机四位验证码
import random


# def get_code(n):
#     code = ''
#     for i in range(n):
#         code_ran = random.randint(0, 9)
#         code += str(code_ran)
#     return code
# print(get_code(4))
#
#
# # 生成6位随机数（数字+字母）
# def get_code_mix(n, flag=True):
#     code = ''
#     for i in range(n):
#         code_ran = random.randint(0, 9)
#         if flag:
#             random_alpha = chr(random.randint(97, 122))
#             random_alpha_cap = chr(random.randint(65, 90))
#             code_ran = random.choice([code_ran, random_alpha, random_alpha_cap])
#         code += str(code_ran)
#
#     return code
# print(get_code_mix(6))

# """
# 路由器与交换机的区别
#     交换机的主要功能是组织局域网，经过交换机内部处理解析信息之后，将信息以点对点，点对多的形式发送给固定端
#     路由器的主要功能：进行跨网段的数据传输， 路由选择最佳路径
#     eg. 需要将多台电脑连接到一根网线，用交换机即可， 如果只有一个外网ip，但是你有好多台电脑需要上网，用路由器即可
# arp协议： 通过目标ip地址获取目标mac地址的一个协议
# """

"""
交换两个变量的值 a = 1, b = 2
"""

# b = 1
# a = 2
# print(a, b)

# b, a = a, b
# print(a, b)

# c = a
# a = b
# b = c
# print(a, b)
#
# a = a+b
# b = a-b
# a = a-b
# print(a, b)


# 缓存队列

"""
进程和线程的比较：
    thread 线程 import thread 操作线程的模块
    import threading 新的
    
    cpu中切换进程比切换线程 慢的多，在python中IO操作过多的话，使用多线程最好
    在同一个进程中，所有的线程共享这个进程的pid，即：所有的线程共享进程的所有资源和内存地址
    同一个进程中，所有的线程共享进程中的全局变量
    因为有GIL,Cpython中没有真正的线程并行，但是有真正的多进程并行，在计算密集的情况下使用多进程最好
        CPython中 计算密集使用多进程，IO密集使用多线程
    守护进程：要么自己结束，要么根据父进程的代码执行借助而结束
    守护线程：要么自己结束，要么根据父进程的执行结束而结束
    
什么时候用线程，什么时候用进程

任务场景分析使用线程还是进程
解释GIL
进程 线程 协程：
    计算密集用多进程，可以充分发挥多核cpu的性能
    IO密集使用多线程（协程是单线程的）
    
多线程和协程生物区别：
    线程是操作系统调度，控制
    协程是程序员自己调度，控制

IO多路复用 select（win，linux）, poll（linux）, epoll（linux）的区别：
    select和poll有一个共同的机制：采用轮训的方式去询问内核，有没有数据准备好
    select 有一个最大监听事件的显示，32位限制1024， 64位限制2048
    poll没有，理论上监听时间可以开到无限大，1g大概10w个监听
    
    epoll是最好的， 采用的是回调机制，解决了select和poll的共同问题，理论上也可以开启无限多个监听


"""

