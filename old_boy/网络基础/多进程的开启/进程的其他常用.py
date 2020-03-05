from multiprocessing import Process
import time


def func():
    time.sleep(1)
    print(123)


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    print('son is alive?', p.is_alive())  # 判断p进程是否还活着
    p.terminate()  # 杀死p进程 解释器告诉操作系统，kill p
    time.sleep(1)
    print('son is alive?', p.is_alive())