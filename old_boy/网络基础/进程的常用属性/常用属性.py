from multiprocessing import Process
import time
import os


def func():
    print('this is son', os.getpid())


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    p.name = 'alex'
    print(p.name, p.pid, p.daemon)