from threading import Thread, Event
import time, random


def conn_mysql(e, i):
    count = 1
    while count <= 3:
        print("%s正在重新尝试连接第%s次" % (i, count))
        if e.is_set():
            print("%s个人连接成功" % i)
        e.wait(0.5)
        count += 1


def check_mysql(e):
    print("\033[31m 数据库正在维护 \033[0m")
    time.sleep(random.randint(1, 2))
    e.set()  # 设置event的值为True，非阻塞
    print("hello")


if __name__ == '__main__':
    e = Event()
    t_c = Thread(target=check_mysql, args=(e, ))
    t_c.start()

    for i in range(10):
        t_conn = Thread(target=conn_mysql, args=(e, i))
        t_conn.start()