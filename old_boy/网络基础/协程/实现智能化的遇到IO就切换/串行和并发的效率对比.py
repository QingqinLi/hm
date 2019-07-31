import gevent
from gevent import monkey
import time
monkey.patch_all()


def func1(num):
    time.sleep(1)
    print(num)


# def func2():
#     pass
start = time.time()
for i in range(10):
    func1(i)
print("串行", time.time() - start)


start = time.time()
l = []
for i in range(10):
    g = gevent.spawn(func1, i)
    l.append(g)
gevent.joinall(l)
print("gevent", time.time() - start)
