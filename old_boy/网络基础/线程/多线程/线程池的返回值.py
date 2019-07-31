from concurrent.futures import ThreadPoolExecutor
import time

def func(num):
    sum = 0
    for i in range(num):
        sum += i ** 2
    return sum

t = ThreadPoolExecutor(10)

# map的方式提交多个任务，对应的拿结果的方法是__next__(),返回的是一个生成器对象
# res = t.map(func, range(1, 101))
# t.shutdown()
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())


# for + submit的方法提交多任务，对应的取结果的方式是result
res_l = []
for i in range(100):
    re = t.submit(func, i)
    res_l.append(re)
t.shutdown()
[print(i.result()) for i in res_l]

# 在pool进程池中取结果的方法是get（）， 在ThreadPoolExecutor中拿结果的方法是result
