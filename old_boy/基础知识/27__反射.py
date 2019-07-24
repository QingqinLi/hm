# 重要(大的项目中，用于简化）
# 反射：用字符串数据类型的变量名来访问这个变量的值
# eval 慎用 在网络和用户输入的情况下不能用
# 推荐用类调用：静态属性 类方法 静态方法
# 函数不加括号就是内存地址

"""
类
对象
模块
反射自己模块中的内容
"""


# # 类 静态属性 类方法 静态方法
# class Student:
#     def __init__(self):pass
#
#     def check_course(self):
#         print("check_course")
#
#     def choose_course(self):
#         print("choose_course")
#
#     def choosed_course(self):
#         print("查看已经选择的课程")
#
#
# stu = Student()
# num = input("please input")
# if num == "check_course":
#     stu.check_course()
# elif num == "choose_course":
#     stu.choose_course()
# elif num == "choosed_course":
#     stu.choosed_course()


# getattr() 第一个参数的命名空间中的变量名为第二个参数的变量的值, hasattr(),是否有这个,一般搭配使用，保证安全
# class Student:
#     ROLE = "STUDENT"
#
#     @classmethod
#     def check_course(cls):
#         print("check_course")
#
#     @staticmethod
#     def login():
#         print("login")
#
#
# # 反射查看属性
# print(getattr(Student, "ROLE"))
#
#
# # 反射调用方法
# print(getattr(Student, "check_course"))
# print(getattr(Student, "login"))
#
# if hasattr(Student, "ROLE"):
#     print(getattr(Student, "ROLE"))
# else:
#     print("no this param")


# 对象 方法 对象属性
# class A():
#     def __init__(self, name):
#         self.name = name
#
#     def func(self):
#         print("func")
#
#
# a = A("alex")
# print(getattr(a, "name"))
# print(getattr(a, "func"))

# # 模块
# import os
#
# print(getattr(os, "rename")("__init__1.py", "__init__.py"))
#
# # # 函数不加括号就是内存地址 rename, rename2都是rename函数的内存地址，使用（）使用
# rename = os.rename
# rename2 = getattr(os, "rename")

# enumerate


# 反射自己模块的内容
def wahaha():
    print("wahaha")

#
# def qqxing():
#     print("qqxing")


# 找到当前文件所在的内存空间， sys模块中的所有方法都是和python解释器相关的，sys.models:表示当前导入的
import sys
# # print(sys.modules)
#
# # 当前模块
# my_file = sys.modules["__main__"] __main__ 变成 __name__ (保证在自己文件和被导入的时候都可以正常的执行
my_file = sys.modules[__name__]
getattr(my_file, "wahaha")()


"""
setattr(命名空间，名字，要修改的值） 一般不用, 名字不存在就会创建一个
delattr（命名空间，名字） 同del 一般不用
"""


# class A:
#     def __init__(self, name):
#         self.name = name
#
#
# a = A("alex")
# print(a.name)
# setattr(a, "name", "new_alex")
# setattr(a, "age", 18)
# print(a.__dict__)
# print(a.name)
#
# delattr(a, "name")
# print(a.__dict__)
