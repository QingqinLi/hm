from multiprocessing import Process, Pool
import time


def func(num):
    num += 1
    # print(num)


if __name__ == '__main__':
    p = Pool(5)
    start = time.time()
    p.map(func, [i for i in range(1000)])
    p.close()  # 指不能再向进程池中添加任务
    p.join()  # 等待进程池中的所有任务执行完毕
    print(time.time() - start)

    p_l = []
    start = time.time()
    for i in range(1000):
        p = Process(target=func, args=(i,))
        p.start()
        p_l.append(p)
    [i.join() for i in p_l]
    print(time.time() - start)