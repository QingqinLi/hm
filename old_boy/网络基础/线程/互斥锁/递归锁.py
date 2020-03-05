from threading import RLock, Thread, Lock
from threading import Semaphore
from multiprocessing import Process, Manager
import time

# s = RLock()
# s1 = RLock()
# s.acquire()
# s.acquire()
# s.acquire()
# s.acquire()
# print(124)

"""
在同一个线程内，递归锁可以无止尽的acquire，但是互斥锁不能
在不同的线程内，递归所只能保证一个线程拿到锁，然后无止尽的acquire， 其他的线程只能等待
python中没有真正的线程并发
"""


def func(l, i):
    l.acquire()
    # print("%s:%s" % (i, time.time()))
    global num
    print(i, num)
    # time.sleep(3)
    # print("%s开始执行, num:%s, 时间是：%s" % (i, num, time.time()))
    # l.acquire()
    # time.sleep(0.1)

    num -= 10
    # print("num:%s, 时间%s" % (num, time.time()))
    # l.acquire()
    # time.sleep(0.1)
    # print("%s执行结束, num:%s, 时间%s" % (i, num, time.time()))
    # l.release()
    # l.release()
    print("这个num:%s, 时间：%s, 第%s个" % (num, time.time(), i))
    # time.sleep(0.2)
    l.release()


# l = RLock()
l = Lock()
t_l = []
num = 100
for i in range(10):
    t = Thread(target=func, args=(l, i))
    # print("这个num:%s" % num)
    t.start()
    # print("这个main的num:%s" % num)
    t_l.append(t)
[t.join() for t in t_l]
print("main num", num)
