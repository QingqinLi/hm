from multiprocessing import Process
from threading import Thread, Lock
import time,os


def func():
    global num
    # num -= 1
    tmp = num
    time.sleep(0.001)
    num = tmp - 1


if __name__ == '__main__':
    num = 100
    t_l = []

    for i in range(100):
        t = Thread(target=func)
        t.start()
        t_l.append(t)
    [t.join() for t in t_l]
    print(num)