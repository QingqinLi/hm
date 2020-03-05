from multiprocessing import Event, Process
import time


def tra(e):
    print(e.is_set())
    while 1:
        if e.is_set():  # True
            time.sleep(0.5)
            e.clear()
            print("\033[31m 红灯 \033[0m")
        else:
            time.sleep(2)
            e.set()
            print("\033[32m 绿灯 \033[0m")


def car(e, i):
    if e.wait():
        print("%s 通过了" % i)


if __name__ == '__main__':
    e = Event()
    traffic_light = Process(target=tra, args=(e, ))
    traffic_light.start()
    for i in range(100):
        time.sleep(0.1)
        p = Process(target=car, args=(e, i))
        p.start()


