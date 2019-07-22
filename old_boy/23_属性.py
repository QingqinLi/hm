# 装饰漆 property 保护属性不被轻易的修改

# 属性：把对象伪装为属性，在代码上没有提升，但是是更加合理
from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return pi * self.r * self.r

    @property
    def lenght(self):
        return 2 * pi * self.r


circle = Circle(3)
print(circle.area)
print(circle.lenght)


# 属性的修改
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 实际上在类中是_类名__方法名

    # 方法伪装为属性
    @property
    def age(self):
        return self.__age

    # 属性的修改
    @age.setter
    def age(self, new_age):
        if new_age < 30:
            self.__age = new_age
        else:
            print("age error")

    # 属性的删除
    @age.deleter
    def age(self):
        del self.__age


p = Person("ll", 17)
print(p.age)
p.age = 39
print(p.age)
del p.age
print(p.__dict__)





