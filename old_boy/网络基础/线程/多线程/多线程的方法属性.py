from threading import Thread
from multiprocessing import Process
import time


def func_daemon():
    time.sleep(2)
    print("this is daemon thread")


def func():
    time.sleep(3)
    print("this is common thread")

"""
守护进程是随着父进程的代码结束而结束的
守护线程是随着父进程的执行结束而结束的
"""

if __name__ == '__main__':
    t = Thread(target=func_daemon,)
    t.daemon = True
    t.start()
    t1 = Thread(target=func)
    t1.start()
    print("this is main Thread")
    # time.sleep(4)

    # t = Process(target=func_daemon, )
    # t.daemon = True
    # t.start()
    # t1 = Process(target=func)
    # t1.start()
    # print("this is main Thread")