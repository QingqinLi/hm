from multiprocessing import Lock

l = Lock()

l.acquire()  # 拿走钥匙

l.release()  # 释放锁
