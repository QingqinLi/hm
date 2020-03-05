import time

"""
在单线程中，如果存在多个函数，如果某个函数发生IO操作，想让程序马上切换到另一个函数去执行

实现一个yield的假的并发现象（效率没有串行执行的效率高）
    yield 是能实现单纯的切换函数和保存函数状态的函数
    不能实现当一个函数遇到io阻塞时，自动切换到另一个函数去执行
    目标：
        当一个函数中遇到IO阻塞时候，程序能自动的切换到另一个函数去执行，如果可以实现，那么每一个函数都是一个协程
    但是协程的本质还是主要依靠yield实现的
"""


def consumer():
    # yield 0
    while 1:
        a = yield
        print("a", a)


def producer():
    g = consumer()  # 获得一个生成器
    print(next(g))
    for i in range(1000):
        g.send(i)


if __name__ == '__main__':
    start = time.time()
    producer()
    print(time.time() - start)