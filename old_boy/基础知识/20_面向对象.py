"""
面向对象：
什么时候用面向对象：
    代码量大，功能多
    处理比较复杂的角色之间的关系
优点:
    代码的清晰度高 无论是开发者还是调用者，都能明确的分辨出每个角色拥有的方法和属性
    增强了代码的可拓展性，可读性
    增加复用性
    更加规范


python中一切皆对象 基础数据类型都是对象
类型和自定义类的关系  是同一个东西
type(obj) obj是一个对象，那么它的type就是它的类型
创建一个对象 类名() 实例化 __new__()创建了对象的空间，一些简单的初始化
创建一个类 class 类名 语法级别的 类也是被创建出来的
type是所有类的元类，object是所有类的父类
class A(metaclass=ABCMeta) ABCMeta创建了这个A类,那么ABCMeta就是A的元类 不指定metaclass=ABCMeta 就是type创建的
一个类的type是type，那么type是这个类的元类
type(类)的结果就是创建这个类的元类,大多数情况下就是type,除非你指定metaclass
元类：用来创建类的

对象：
    类创造对象的过程就是实例化的过程：构造new,初始化init
    可以通过指针找到类的空间中的内容
    对象本省内部也存储类一些只属于对象的属性

组合 对象与对象 什么有什么的关系 eg人有武器：
    一个类的对象作为另一个类对象的属性

继承 什么是什么的关系 节省代码；
    单继承 多继承
        单继承：
            调用顺序：子类，父类，object 报错
            子类有但是想用父类的：super（不用自己传self）.方法名（除了self之外的参数），父类名.方法名（self,...)
        在任何类中调用的方法，都要自己分辨一些self到底是谁的对象
        多继承：
            新式类：默认继承object， 广度优先， py3默认继承object。py2需要主动继承，默认都是经典类，（广度优先）
                mro（）查看继承顺序
                py3: super().func() 遵循mro算法，在类的内部不需要传子类名和self
                py2: super(子类名，self).func() 必须传子类名和self
            经典类：（深度优先）
                没有mro

    子类 父类：

    经典类 新式类
    接口类和抽象类
        不能被实例化
        规范子类当中必须实现某个方法
        python中有原生的实现抽象类的方法，但是没有原生实现接口类的方法

        java:只支持类的单继承 接口（也是一个规范）支持多继承，（接口类和抽象类的区别明显）
        抽象类
            抽象类中的方法是可以实现的，只能单继承
        接口类
            可以多继承 但是这个类中的所有方法都不应该实现

封装 私有的（不能在类的外部访问，也不能被继承）：
    广义的封装：把方法和属性都封装在一个类里，定义一个规范来描述一类事物
    狭义的封装；私有化 只能在类的内部访问
    __静态变量。私有方法，私有的对象属性，私有的类方法，私有的静态方法
    内存中存储的是_类名__名字

多态
    多态 一种类型的多重形态（eg.多个子类去继承父类，那么每一个子类都是这个父类的一种形态）
    处处是多态 弱类型语言
    鸭子类型 eg,index（）【list, str, dict] 规范全凭自觉

property(装饰器函数，内置函数，帮助你将类中的方法伪装为属性）这个属性会随着类／对象的一些基础变量的变化而变化
    调用方法的时候不需要加（）
    让程序的逻辑性更合理
    @方法名.setter 修改被property装饰的属性的时候会调用这个装饰器的方法， 除了self之外，还有一个修改后的值，可以在修改值的时候加一些约束条件
    @方法名.deleter 删除被property装饰的属性的时候会调用这个装饰器的方法 不常用

classmethod 类方法的装饰器 内置函数
    使用类名调用。默认传类名作为第一个参数
    不用对象命名空间中的内容，而是用到类类命名空间中的变量（静态属性）或者类方法或者静态方法

staticmethod 静态方法的装饰漆 内置函数
    如果在一个类里面的方法 不需要self和cls的资源
    由于某种原因（1、用面向对象编程 所有的函数需要写到类中， 2、某个功能不依赖类和对象的资源） 需要把这个方法放到这个类中 需要变成静态方法


列表操作技巧：
    不要pop(参数）insert（）因为每一个值都需要移动 很耗时

反射：
    从某个指定的命名空间， 用字符串数据类型的变量名来获取变量的值 getattr setattr delattr getattr 命名空间 字符串变量名 【新的值】
    类 静态属性 类方法 静态方法
    对象 对象属性 方法
    模块 模块中的方法
    自己模块
    只能拿到字符串的情况下：1、从文件中拿， 2、交互中，input／网络传输（bytes--str)

内置方法 都不是被直接调用的
    内置方法／魔术方法／双下方法
    __名字__
    内置函数／面向对象中的特殊语法/python提供的语法糖（简化操作）
    __call__ 对象（） 用类写装饰漆的时候
    __new__ 实例化的过程中 最先执行的方法 执行init之前，用来创造一个对象 构造方法
    __init__ 在实例化的过程中 在new之后 自动触发的一个初始化方法
    __len__
    __str__ print %s str

"""


# class A:
#     pass
#
#
# print(type(A))
# print(type(object))

# from abc import ABCMeta
#
# class A(metaclass=ABCMeta):pass
# print(type(A))

"""
类是什么时候加载的
"""


# class Person:
#     ROLE = "中国"
#     print(ROLE)  # 加载变量 不需要完全加载完 类是什么时候加载的
#     # print(Person.ROLE) # 报错 变量都加载完，才能创建一个引用指向类名 类名是什么时候生效的
#
#     def func(self):
#         pass
#
#
# a = Person()
# print(Person.func)  # 真实的func地址的值
# print(a.func)  # 不是同一个。对象的内存空间存的是记录类中属性 的变量 的地址

# class Foo:
#     def __init__(self):
#         self.func()
#
#     def func(self):
#         print("FOO.Func")
#
#
# class Son(Foo):
#     def Func(self):print("SON.Func")
#
#
# s = Son()  # 调用的是子类的func

# class A:
#
#     def func(self):
#         print("A")
#
#
# class B(A):
#
#     def func(self):
#         super().func()
#         print("B")
#
#
# class C(A):
#
#     def func(self):
#         super().func()
#         print("C")
#
#
# class D(B, C):
#
#     def func(self):
#         super().func()
#         print("D")
#
# d = D()
# d.func()
# print(D.mro())
# # 遵循mro的顺序 多继承的继承顺序

# 装饰器
# class Goods:
#
#     __diccount = 0.8
#
#     def __init__(self, price):
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price * Goods.__diccount
#
#     @classmethod
#     def change_discount(cls, new_count):
#         cls.__diccount = new_count
#
#
# a = Goods(9)
# b = Goods(5)
# print(a.price, b.price)
# Goods.change_discount(1)
# print(a.price, b.price)


class Person:
    pass

class Student(Person):pass

class Manager(Person):pass

class Course:pass

class Classes:pass


