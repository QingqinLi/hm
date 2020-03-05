from multiprocessing import Pool
import os


def func(num):
    num += 1
    print(num)
    return num


if __name__ == '__main__':
    p = Pool(os.cpu_count() + 1)
    print(os.cpu_count())
    res = p.map(func, [i for i in range(20)])
    p.close()
    p.join()
    print(type(res))
