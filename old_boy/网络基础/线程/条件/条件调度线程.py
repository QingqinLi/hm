from threading import Thread, Condition
import timeit

# Condition涉及4个方法
# acquire()
# release()
# wait()    是指让线程阻塞住
# notify(int)  是指给wait发一个信号，让wait变成不阻塞
#     int是指，你要给多少给wait发信号


def func(con, i):
    con.acquire()
    con.wait()
    con.release()
    print(i)


if __name__ == '__main__':
    con = Condition()
    for i in range(10):
        t = Thread(target=func, args=(con, i))
        t.start()
    while 1:
        num = int(input(">>>"))
        con.acquire()
        con.notify(num)
        con.release()