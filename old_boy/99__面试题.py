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


def get_code(n):
    code = ''
    for i in range(n):
        code_ran = random.randint(0, 9)
        code += str(code_ran)
    return code
print(get_code(4))


# 生成6位随机数（数字+字母）
def get_code_mix(n, flag=True):
    code = ''
    for i in range(n):
        code_ran = random.randint(0, 9)
        if flag:
            random_alpha = chr(random.randint(97, 122))
            random_alpha_cap = chr(random.randint(65, 90))
            code_ran = random.choice([code_ran, random_alpha, random_alpha_cap])
        code += str(code_ran)

    return code
print(get_code_mix(6))
