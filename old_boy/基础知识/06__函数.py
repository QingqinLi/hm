"""
函数：对代码块和功能的封装和定义
关于返回值:
如果return 么都不写 或者  脆不写return .那么返回的就是None
如果return后只写一个值. 则调用者可以接收一个结果 如果return后面写了多个结果, 则调用者可以接收一个tuple, 调用者可以直接解构成
多个变量
实参分类：位置参数 关键字参数 混合参数（混合参数中 关键字参数必须在位置参数后面）
形参分类：位置参数 默认值参数 （必须先声明位置参数 才能声明默认值参数）
动态传参（形参）：
1、动态接收位置参数 *args（*表示接收任意参数） 动态参数必须在位置参数后面 顺序：位置参数 动态参数 默认值参数
2、动态接收关键字参数 **kwargs 接收到的是一个dict 顺序：位置参数 *args 默认值参数 **kwargs
三元表达式 a if a>b else b

调用函数的时候使用*是把传进来的参数打散,在形参的位置上。*表示的是把参数组合成一个元祖。如果是一个字典的话 也可以打散，不过是需要两个**
"""


# def fun(*agrs):
#     print(*agrs)
#
#
# lst = [1, 4, 7]
# fun(lst[0], lst[1], lst[2])
# fun(*lst)

"""
命名空间名 字和值的关系的空间起了个名字叫
在python解释器开始执 之后, 就会在内存中开辟 个空间, 每当遇到 个变 的时候, 就
把变 名和值之间的关系记录下来, 但是当遇到函数定义的时候, 解释器只是把函数名读入内存, 表示这个函数存在 ,  
至于函数内部的变量和逻辑, 解释器是不关心的. 也就是说一开始的时候函数只是加载进来, 仅此而已, 只有当函数被调用和访问的时候, 
解释器才会根据函数内部声明的变量来进行开辟变量的内部空间. 随着函数执行完毕, 这些函数内部变量占用的空间也会随着函数执行完毕而被清空.


命名空间分类:
1. 全局命名空间--> 我们直接在py 件中, 函数外声明的变 都属于全局命名空间
2. 局部命名空间--> 在函数中声明的变 会放在局部命名空间
3. 内置命名空间--> 存放python解释器为我们提供的名字, list, tuple, str, int这些都是内
置命名空间

加载顺序:
1. 内置命名空间
2. 全局命名空间
3. 局部命名空间(函数被执 的时候)


取值顺序:
1. 局部命名空间 
2. 全局命名空间 
3. 内置命名空间

作 域命名空间:
1. 全局作用域: 全局命名空间 + 内置命名空间 
2. 局部作用域 域: 局部命名空间

globals()函数来查看全局作 域中的内容, 也可以通过locals()来查看局部作  域中的变 和函数信息
global表 . 不再使用局部作用域中的内容 .  改用全局作用域中的变量 可以修改全局变量
nonlocal 表示在局部作用域中, 调用父级命名空间中的变量.

函数名：
可以直接赋值给其他bianl
可以当作容器类的元素
可以当作函数的参数
可以作为函数的返回值
"""


# def func():
#     print("func")
#
#
# def func1():
#     print("func1")
#
#
# def func2():
#     print("fun2c")
#
#
# def func3():
#     print("func3")
#
#
# list1 = [func, func2, func3]
# print(list1)


# def func():
#     print("吃么")
#
#
# def func2(fn):
#     print("我是func2")
#     fn()  # 执 传递过来的fn print("我是func2")
#
#
# func2(func)

def func_1():
    # print("这 是函数1")
    name = 1
    def func_2():
        nonlocal name
        print("这 是函数", name)
    # print("这 是函数1")
    return func_2
fn = func_1() # 执 函数1. 函数1返回的是函数2, 这时fn指向的就是上 函数2
fn()