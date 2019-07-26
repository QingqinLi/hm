from multiprocessing import Pipe, Process


def func(con):
    con1, con2 = con
    con1.close()
    while 1:
        try:
            print(con2.recv())
        except EOFError:
            break   # 获取到错误，就是指子进程已经把管道中所有数据都接收完了，所以用这种方式去关闭管道
    con2.close()


if __name__ == '__main__':
    con1, con2 = Pipe()
    p = Process(target=func, args=((con1, con2),))
    p.start()
    con2.close()  # 在父进程中，使用con1去和子进程通信，所以不需要con2，就提前关闭

    for i in range(10):
        con1.send("hell0"+str(i))
    con1.close()  # 生产完数据，关闭父进程这一端的管道