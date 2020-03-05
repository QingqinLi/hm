from greenlet import greenlet
import time

"""
greenlet 知识可以实现一个简单的切换功能，不能做到遇到IO就切换
g = greenlet(func) 实例化一个对象
g.switch() 调用func函数
使用swithch调用func的时候，停止func：return／在func内部遇到switch
"""


def eat(name):
    print("%s eat chicken" % name)
    # time.sleep(1)
    g1.switch("wusir")
    print("%s eat ice" % name)
    g1.switch("wusir")


def drink(name):
    print("%s drink beer" % name)
    # time.sleep(1)
    g.switch("alex")
    print("over")


g = greenlet(eat)
g1 = greenlet(drink)
g.switch("alex")