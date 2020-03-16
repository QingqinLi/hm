from multiprocessing import Process
import time
import os


# 开启子进程的一种方式，os.getpid() 获取当前进程的pid， os.getppid()获取当前进程的父进程id
# def func(i):
#     time.sleep(1)
#     print("this is son, the pid is %s his parents's pip is %s" % (os.getpid(), os.getppid()))
#
#
# if __name__ == '__main__':
#     p = Process(target=func, args=(1, ))
#     p.start()
#     p.join()
#     print('this is father process the pid is %s and his father is %s' % (os.getpid(), os.getppid()))


# # 开启子进程的另外一种方式：继承
# class MyProcess(Process):
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         print('this is son')
#
#
# p1 = MyProcess()
# p1.start()  # 解释器告诉操作系统，去开启一个进程（并不一定会去开启，需要看系统的状态） 处在就绪状态
# p1.run()   # 告诉操作系统，马上执行这个子进程  执行状态


# 开启多个不同的子进程

def func(i):
    time.sleep(1)
    print(i)
    print("this is son, the pid is %s his parents's pip is %s" % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    for i in range(3):
        p = Process(target=func, args=(i,))
        p.start()
        p.join()
    print('this is father process the pid is %s and his father is %s' % (os.getpid(), os.getppid()))