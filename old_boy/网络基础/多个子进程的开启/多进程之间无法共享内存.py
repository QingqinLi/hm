from multiprocessing import Process


def func(i, num):
    print(i)
    # n = n - 1  多进程之间无法共享内存，可以访问？
    print(n)
    print(num)
    num -= 1
    print(num)
    print(n)


if __name__ == '__main__':
    n = 9999
    for i in range(4):
        p = Process(target=func, args=(i, n))  # 通过传值的方式，其实是拷贝了一份， 修改的不是原来的那个变量
        p.start()
    print("result n", n)