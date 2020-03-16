from multiprocessing import Pool
import os
import time


def func(num):
    time.sleep(1)
    num += 1
    print(num)
    return num


if __name__ == '__main__':
    p = Pool(os.cpu_count() + 1)
    print(os.cpu_count())
    res = p.map(func, [i for i in range(20)])
    p.close()
    p.join()
    print(res, type(res))
