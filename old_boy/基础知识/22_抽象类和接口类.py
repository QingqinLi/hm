# 抽象类和接口类:制定一个规范
# 强制执行
from abc import ABCMeta, abstractmethod


# 抽象类／接口类（相当于是一个模版）
class Payment(metaclass=ABCMeta):
    # 制定了一个规范，所有继承这个类的类都必须又这个方法,没有这个方法会报错， abstractmethod--装饰器
    @abstractmethod
    def pay(self):
        pass


class Alipay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        return "使用支付宝支付%s" % self.money


class Jdpay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        return "使用支付宝支付%s" % self.money


a1 = Alipay(300)
j1 = Jdpay(100)


def pay(obj):
    return obj.pay()


print(pay(a1))
print(pay(j1))
# 归一化设计

"""
接口类,抽象类:python中就是一样的
        1,归一化设计.
        2,制定一个规范,凡是继承我类的类,必须有我规定的方法.

    多态: python处处是多态,没有多态的示例.
    鸭子类型: 看着像鸭子,其实就是鸭子.
    封装:
        1,广义的封装. 给对象封装属性,给类中封装静态字段.....
        2,狭义的封装: 私有制.私有成员.
            私有成员:静态私有字段,静态私有方法,静态私有对象属性.
                    只能在自己类中访问,不能再类的外部,或者派生类中访问.
"""