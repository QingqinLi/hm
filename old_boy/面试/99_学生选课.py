import sys


class Manager:

    operate_dic = [
        ("创建学生信息", "create_stu"),
        ("创建课程信息", "create_course"),
        ("获取学生信息", "get_student")
    ]

    def __init__(self, name):
        self.name = name

    @staticmethod
    def create_stu():
        print("create_stu")

    @staticmethod
    def create_course():
        print("create_course")

    @staticmethod
    def get_student():
        print("get_student")


class Student:
    operate_dic = [
        ("查课程", "check_course"),
        ("aaa", "aaa"),
        ("bbb", "bbb")
    ]

    def __init__(self, name):
        self.name = name

    @staticmethod
    def check_course():
        print("check_course")

    @staticmethod
    def aaa():
        print("aaa")

    @staticmethod
    def bbb():
        print("bbb")


def login():
    username = input("input your name: ")
    password = input("inout your pwd: ")

    with open("userinfo", "r") as file:
        for line in file:
            user, pwd, identity = line.strip().split("|")
            if username == user and password == pwd:
                print("login success")
                return user, identity


def main():
    user, id = login()
    # 反射获取对象
    file = sys.modules["__main__"]
    obj = getattr(file, id)(user)

    while True:
        for num, item in enumerate(obj.operate_dic, 1):
            print(num, item[0])

        operate_num = input("input num: ")
        if operate_num.upper() == 'Q':
            break
        getattr(obj, obj.operate_dic[int(operate_num) - 1][1])()


main()