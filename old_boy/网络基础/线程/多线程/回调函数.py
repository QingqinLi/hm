from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import current_thread
# Pool ProcessPoolExecutor的回调函数都是父进程调用的
import os
import time

#
# def func(num):
#     sum = 0
#     for i in range(num):
#         sum += i ** 2
#     print("子", os.getpid())
#     return sum
#
#
# def call_back_fun(res):
#     print(res.result())
#     print("回调函数", os.getpid())
#
#
# if __name__ == '__main__':
#     print("main", os.getpid())
#     t = ProcessPoolExecutor(5)
#     for i in range(20):
#         t.submit(func, i).add_done_callback(call_back_fun)
#     t.shutdown()


def func(num):
    sum = 0
    for i in range(num):
        sum += i ** 2
    print("子", num, current_thread())
    return sum


def call_back_fun(res):
    # print(res.result())
    print("回调函数", current_thread())
    # print("\n")


if __name__ == '__main__':
    t = ThreadPoolExecutor(5)
    for i in range(10):
        t.submit(func, i).add_done_callback(call_back_fun)
    t.shutdown()
    print("main", current_thread())

# from threading import Thread
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor
# import time
# def func(i):
#     sum = 0
#     sum += i
#     # time.sleep(1)
#     print('这是在子线程中', current_thread())
#     return sum
#
# def call_back(sum):
#     # time.sleep(1)
#     print('这是在回调函数中', sum.result(), current_thread())
#
#
# if __name__ == '__main__':
#     t = ThreadPoolExecutor(5)
#     res_l = []
#     for i in range(10):
#         res = t.submit(func, i)
#         res_l.append(res_l)
#         # time.sleep(1)
#     t.shutdown()
#     print('这是在主线程中', current_thread())