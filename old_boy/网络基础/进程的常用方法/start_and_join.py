from multiprocessing import Process
import time


def func():
    for i in range(5):
        time.sleep(0.05)
        print("hello")


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    p.join()  # 是让主进程等待子进程执行完， （当主进程执行到这句话的时候， 主进程阻塞，等待子进程执行完，主进程继续执行
    for i in range(5):
        time.sleep(0.01)
        print("hi")


# 开启一个正常的子进程，父进程会等待子进程结束后，父进程也就是程序才结束
# p.join()# 是让主进程等待子进程执行完。  现象：主进程执行到这句话，主进程阻塞住，等待子进程执行
# 如何把父进程和子进程之间的关系变为同步或者异步？
# 父进程执行join，就会变成同步，不执行join，父进程和子进程就是异步的关系
# join必须放在start()后边
