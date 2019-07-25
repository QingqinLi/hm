from multiprocessing import Semaphore, Lock
#
# l = Lock()
# l.acquire()
# print(123)
# l.release()
# l.acquire()
# print(456)

sem = Semaphore(2)
sem.acquire()
print(1)
sem.acquire(2)
print(2)
sem.release()
sem.acquire(3)
print(3)