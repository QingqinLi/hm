from multiprocessing import Pool
import time


def func(num):
    num += 1
    return num


if __name__ == '__main__':
    p = Pool(5)
    start = time.time()
    for i in range(10):
        res = p.apply(func, args=(i,))  # 同步：即使有n个进程，也是一个一个的去执行任务
        time.sleep(0.4)
        print(res)
    print(time.time() - start)
