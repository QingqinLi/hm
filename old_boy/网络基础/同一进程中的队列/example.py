from multiprocessing import Queue  # 用于多进程的队列，专门用来做进程间通信（IPC）
import queue  # 是用于同一进程内的队列，不能做多进程间的通信

# q = queue.Queue()  # 先进先出
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

# q = queue.LifoQueue()  # 后进先出的队列
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())

q = queue.PriorityQueue()
# 优先级队列，put（）方法接收到的是一个元组，第一个位置是优先级，第二个位置是数据, 优先级数据的类型必须是相同的
# 优先级如果是数字，直接比较数字的大小
# 如果是字符串，是按照ASCII比较，当ASCII相同的时候，回按照先进先出的原则

# q.put((1, 'ac'))
# q.put((4, '123'))
# q.put((2, [2, 4]))
# print(q.get(), q.get())

q.put(('h', 'abc'))
q.put(('a', '123'))
print(q.get())