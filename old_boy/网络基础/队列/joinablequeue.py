from multiprocessing import JoinableQueue, Process


def producer(q, name):
    for i in range(20):
        q.put(name)
        print("生产第%s个%s" % (i, name))
    q.join()


def consumer(q, name):
    while 1:
        q.get()
        print("%s 拿走了一个" % name)
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue(10)
    p1 = Process(target=producer, args=(q, 'one'))
    c1 = Process(target=consumer, args=(q, 'alex'))
    c1.daemon = True
    p1.start()
    c1.start()
    p1.join()

    # 主进程等待生产者进程结束
    # 程序有3个进程，主进程和生产者进程和消费者进程。  当主进程执行到35行代码时，主进程会等待生产进程结束
    # 而生产进程中（第26行）会等待消费者进程把所有数据消费完，生产者进程才结束。
    # 现在的状态就是  主进程等待生产者进程结束，生产者进程等待消费者消费完所有数据
    # 所以，把消费者设置为守护进程。  当主进程执行完，就代表生产进程已经结束，也就代表消费者进程已经把队列中数据消费完
    # 此时，主进程一旦结束，守护进程也就是消费者进程也就跟着结束。    整个程序也就能正常结束了。