from multiprocessing import Process
from threading import Thread
import time
import os


def func(name):
    print("%s, pid: %s" % (name, os.getpid()))


if __name__ == '__main__':
    print("主进程， pid:%s" % os.getpid())
    for i in range(10):
        p = Process(target=func, args=('进程', ))
        p.start()
    for i in range(10):
        t = Thread(target=func, args=("线程",))
        t.start()

 #  线程的pid是主线程的pid