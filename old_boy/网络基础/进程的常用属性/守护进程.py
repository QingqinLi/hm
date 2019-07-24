from multiprocessing import Process
import time

"""
守护进程： 跟随者父进程的代码执行结束，守护进程就结束
    守护进程不允许开启子进程
"""


# def func():
#     time.sleep(3)
#     print("this is son")
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True  # 设置进程为守护进程，必须在start之前设置
#     p.start()
#     # p.join()
#     time.sleep(1)
#     print('this is father')


# def func_two():
#     print("this is grandson")
#
#
# def func():
#     p = Process(target=func_two)
#     p.start()
#     time.sleep(2)
#     print('this is son')
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True
#     p.start()
#     time.sleep(1)
#     print('this is father')


def func():
    for i in range(10):
        time.sleep(1)
        print(time.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True
    p.start()
    time.sleep(5)
    print('this is father')