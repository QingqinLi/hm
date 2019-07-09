# 类方法 通过类名调用的方法，第一个参数一般为cls， python自动将类空间传递给cls，
"""
使用场景:
1、类中的有些方法不需要对象参与
2、对类中的静态变量进行改变
3、在继承中，父类在类方法中获得子类的类空间，与对象调用方法相比，对象调用只能访问，类方法可以修改类的字端，但是类调用不能获得对象的属性
"""


class Person(object):

    name = 'alex'
    __age = 18

    @classmethod
    def get_name(cls):
        print(cls)
        return cls.name

    @classmethod
    def update_age(cls, new_age):
        cls.__age = new_age


p = Person()
print(Person.get_name())
Person.update_age(10)
print(Person.__dict__)
# 对象调用类方法 cls为类本省（一般不用对象调用类方法）
print(p.get_name())


class Animal(object):

    # 对象调用普通方法只能访问类属性，不能修改
    def func(self):
        print(self.age)

    # 类调用类方法，可以获得子类的类空间，修改子类的属性
    @classmethod
    def func1(cls):
        cls.age = 20


class Dog(Animal):
    age = 10
    pass


dog = Dog()
dog.func()
print(Dog.age)
Dog.func1()
print(Dog.age)


# 静态方法 不需要参数, 使用类名调用
"""
优点：
1、代码块，结构清晰
2、减少代码量，增加代码的复用性（在继承中）
"""


class Fruit(object):
    @staticmethod
    def get_all():
        return "abc"


f = Fruit()
print(f.get_all())
print(Fruit.get_all())
