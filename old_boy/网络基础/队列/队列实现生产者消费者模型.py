from multiprocessing import Queue, Process
import time


def producer(q, name):
    for i in range(20):
        q.put(name)
        print("生产第%s个%s" % (i, name))
    # q.put(None)


def consumer(q, name, color):
    while 1:
        info = q.get()
        if info:
            print("%s %s拿走来%s\033[0m" % (color, name, info))
        else:
            break


if __name__ == '__main__':
    q = Queue(10)
    p = Process(target=producer, args=(q, 'number one'))
    p1 = Process(target=producer, args=(q, 'number two'))
    p2 = Process(target=producer, args=(q, 'number three'))
    c1 = Process(target=consumer, args=(q, 'alex', '\033[31m'))
    c2 = Process(target=consumer, args=(q, 'wusir', '\033[32m'))
    p_l = [p, p1, p2, c2, c1]
    [i.start() for i in p_l]
    p.join()
    p1.join()
    p2.join()
    q.put(None)
    q.put(None)  # 设置标志 表示没有数据了，生产者不再生产数据
