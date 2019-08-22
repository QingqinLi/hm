from multiprocessing import Process, Lock, Value
import time


def get_money(num, l):
    l.acquire()
    for i in range(100):
        num.value -= 1
        time.sleep(0.1)
        print('get' + str(num.value))
    l.release()


def put_money(num, l):
    l.acquire()
    for i in range(100):
        num.value += 1
        time.sleep(0.12)
        print(num.value)
    l.release()


if __name__ == '__main__':
    num = Value('i', 100)
    l = Lock()
    p = Process(target=get_money, args=(num, l))

    p1 = Process(target=put_money, args=(num, l))
    p.start()
    p1.start()
    p.join()
    print("*"*20)
    p1.join()
    print("end" + str(num.value))