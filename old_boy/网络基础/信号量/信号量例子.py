from multiprocessing import Process,Semaphore
import time
import random


def func(i, sem):
    sem.acquire()
    print(i)
    time.sleep(0.2)
    print(i)
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(2)
    for i in range(20):
        p = Process(target=func, args=(i, sem))
        p.start()