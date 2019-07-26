from multiprocessing import Process
from threading import Thread, Lock, RLock
import time, os


def man(l_to, l_pa):
    l_to.acquire()
    print("man get toilet")
    time.sleep(1)
    l_pa.acquire()
    print("man get paper")
    time.sleep(0.5)
    print("man over")
    l_pa.release()
    l_to.release()


def woman(l_to, l_pa):
    l_pa.acquire()
    print("woman get paper")
    time.sleep(1)
    l_to.acquire()
    print("woman get toilet")
    time.sleep(0.5)
    print("woman over")
    l_to.release()
    l_pa.release()


if __name__ == '__main__':
    # l_to = Lock()
    # l_pa = Lock()
    l_to = l_pa = RLock()  # 递归锁
    t_man = Thread(target=man, args=(l_to, l_pa))
    t_woman = Thread(target=woman, args=(l_to, l_pa))
    t_man.start()
    t_woman.start()