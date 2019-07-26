from multiprocessing import Process
from threading import Thread, Lock
import time,os

l = Lock()
l.acquire()
print(123)
l.acquire()
print(456)