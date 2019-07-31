import time


def func():
    print(123)
    sum = 0
    print(333)
    sum += 1
    yield sum
    print(444)
    sum += 1
    yield sum
    print(555)
    sum += 1
    yield sum


def fff():
    g = func()  # 并不会开始执行函数
    print("this is in fff()")
    print(next(g))  # 开始执行到yeild 之后
    time.sleep(1)
    print("again")
    print(next(g))
    time.sleep(1)
    print("again and again")
    print(next(g))


fff()