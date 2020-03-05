from multiprocessing import Process
import time
import random


def func(i):
    print(i)


if __name__ == '__main__':
    l = []
    addr = ['a', 'b', 'c', 'd', 'e']
    for i in addr:
        p = Process(target=func, args=(i,))
        p.start()
        l.append(p)
    [p.join() for p in l]
    print(random.choice(addr))
