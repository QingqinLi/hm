from multiprocessing import Process
from threading import Thread
import time


def func():
    pass


if __name__ == '__main__':
    start = time.time()
    for i in range(100):
        p = Process(target=func, args=())
        p.start()
    print("开100个进程的时间", time.time() - start)

    start = time.time()
    for i in range(100):
        t = Thread(target=func, args=())
        t.start()
    print("开100个线程的时间", time.time() - start)