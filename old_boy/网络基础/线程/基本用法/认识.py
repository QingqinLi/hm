from threading import Thread
import time

# def func():
#     print("test")
#
# if __name__ == '__main__':
#     t = Thread(target=func, args=())
#     t.start()


class MyThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("自线程")


t = MyThread()
t.start()