from multiprocessing import Queue

q = Queue(3)

q.put(1)
q.put(2)
q.put(3)
print(123)
print(q.get())
q.put(4)
try:
    q.put_nowait(5)
    q.get_nowait()
except:
    print("full")