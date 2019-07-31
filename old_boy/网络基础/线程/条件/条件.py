from threading import Condition, Thread
import time

# 条件 涉及 4个方法：
#    con.acquire()
#    con.release()
#    con.wait()  # 假设有一个初始状态为False，阻塞。一旦接受到notify的信号后，变为True，不再阻塞
#    con.notify(int)  给wait发信号，发int个信号，会传递给int个wait，让int个线程正常执行


def func(con, i):
    con.acquire()
    con.wait()
    print("%s线程执行了" % i)
    con.release()


con = Condition()
for i in range(10):
    t = Thread(target=func, args=(con, i))
    t.start()

while 1:
    con.acquire()
    num = input(">>>")
    con.notify(int(num))
    con.release()
    # time.sleep(0.1)
