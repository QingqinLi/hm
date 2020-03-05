class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return "%s吃东西" % self.name

    def drink(self):
        return "%s喝水" % self.name
#
#
class Bird(Animal):

    # super()
    def __init__(self, name, age, wind):
        super().__init__(name, age)
        self.wind = wind


bird = Bird("1", 1, "str")
print(bird.name)

"""
简单总结:
        继承的优点:
            1,节省代码.
            2,规范代码.
            3、提高代码的复用性
            4、提高代码的维护性
            5、关联类与类
        初始继承:
            只执行本类的方法
            只执行父类的方法.
            既执行本类又执行父类的方法
                父类名.方法名(参数)
                super().方法名(参数(self自动传值))
        单继承,多继承.
        类:新式类（继承object的类，python3都是新式类）,经典类（只在python2中有）.
        单继承;
            新式类经典类一样.
        多继承:
            新式类:广度优先  类名.mro()  新式类.走到其他的继承也能到达的路径之后开始另一条路径，也叫钻石继承（
            如果子类继承自两个单独的超类，而那两个超类又继承自同一个公共基类，就构成了钻石继承系统），每个节点走且只走一次
            经典类:深度优先.

        深度优先，广度优先：只能是继承两个类的情况

super()的作用：在子类中调用父类的方法

"""


# class A(object):
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#
#
# class C(B):
#     def __init__(self):
#         print("C")
#
#
# class D(B):
#     def __init__(self):
#         print("D")
#
#
# class E(C):
#     def __init__(self):
#         print("E")
#
#
# class F(D):
#     def __init__(self):
#         print("F")


# class G(F):
#     def __init__(self):
#         print("G")
#
#
# class H(G, E):
#     def __init__(self):
#         print("H")
#
#
# print(H.mro())


# class Animal:
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print("%s 在吃法" % self.name)
#
#
# class Person(Animal):
#
#     def __init__(self,name, sex, age, skin):
#         super().__init__(name, sex, age)
#         self.skin = skin
#
#     def eat(self):
#         super().eat()
#         return "人类正在吃饭"
#
#
# class Dog(Animal):
#
#     def __init__(self, name, sex, age, color):
#         super().__init__(name, sex, age)
#         self.color = color
#
#     def eat(self):
#         return "狗狗正在吃饭"
#
#
# p1 = Person("xx", "22", 22, "dd")
# print(p1.__dict__)
# print(p1.eat())


# # 变量是可变的数据类型,内存中存的是一个变量+地址，添加值的时候改的是地址对应的值，地址不变，所以不会报错
class A:
    name = []


p1 = A()
p2 = A()
p1.name.append(1)

print(p1.name, p2.name, A.name)

# 不可变的数据类型 内存存的是数据本身，相当于给对象新增了一个属性
class A:
    name = "name"


p1 = A()
p2 = A()
p1.name = "alex"

print(p1.name, p2.name, A.name)








