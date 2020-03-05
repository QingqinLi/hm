class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法%d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的公有方法")
        self.__test()


class B(A):
    def demo(self):
        # 访问父类的私有属性---在子类的对象方法中，不能访问父类的私有属性
        print("访问父类的私有属性%d" % self.num1)
        # 调用父类的私有方法---在子类的对象方法中，不能访问调用父类的私有方法
        # 访问父类的公有属性和方法
        self.test()


# 创建一个子类对象
b = B()
print(b)
b.demo()
