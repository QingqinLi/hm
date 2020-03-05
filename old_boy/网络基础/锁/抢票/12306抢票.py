from multiprocessing import Process,Lock
import time


def check(n, l):
    # l.acquire()
    with open('ticket') as f:
        num = f.read()
    print("%s查看时候票还有%s张" % (n, num))
    # l.release()


def buy(n, l):
    l.acquire()
    with open('ticket') as f:
        try:
            num = int(f.read())
        except Exception as e:
            print(e, 'test:', f.read())
    if num > 0:
        print("\033[32m %s买到票了\033[0m" % n)
        num -= 1
    else:
        print("\033[32m %s没买到票\033[0m" % n)
    time.sleep(0.1)
    with open('ticket', 'w') as f:
        f.write(str(num))
    l.release()


if __name__ == '__main__':
    l = Lock()
    for i in range(10):
        p = Process(target=check, args=(i, l))
        p.start()
    for i in range(10):
        p = Process(target=buy, args=(i, l))
        p.start()
