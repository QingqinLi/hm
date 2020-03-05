from concurrent.futures import ThreadPoolExecutor
import time


def func(num):
    sum = 0
    for i in range(num):
        sum += i ** 2
    print(sum)


t = ThreadPoolExecutor(20)
start = time.time()
t.map(func, range(10))  # 相当于for + submit
t.shutdown()
print(time.time() - start)