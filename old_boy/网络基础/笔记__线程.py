"""
线程：被称为轻量级的进程 GIL:全局解释锁（只有cpython有）
    对于线程来说，因为有GIL,所以没有真正的并行

    计算机的执行单位是以线程为单位，最小可执行是线程
    进程是资源分配的基本单位，线程是可执行的基本单位，是可被调用的基本单位
    线程不可以独立拥有资源，线程的执行，必须依赖于所属进程的资源
    进程中必须至少有一个线程

    进程：代码段 数据段 PCB(进程控制块）
    线程：代码段 数据段 TCB(线程控制块）

线程的使用方法：
    锁机制：
        递归锁：RLock() 可以有无止尽的锁，但是有一把万能钥匙
        互斥锁：Lock() 一把钥匙一把锁，为了保护数据安全，  共享资源又叫临界资源，共享代码 又叫临界代码，对临界资源进行操作时，一定要加锁
        GIL: 全局解释器锁 所得是线程，CPython，意思是一个时间点只u 允许一个线程访问cpu

    信号量：也是用来保护数据安全
        from threading import Semaphore
    事件：
        from threading import Event
    条件：
        from threading import Condition
        可以让程序员自行去调度线程的一个机制
        acquire()
        release()
        wait() 让线程阻塞
        notify(int)  给多少个wait发一个信号，让wait不阻塞

    定时器：
        from threading import Timer
        Timer(time, func) time:睡眠的事件（s), func，多久之后需要执行的任务

同一个进程内的队列（多线程）：
    import queue
    queue.Queue() 先进先出
    queue.LifoQueue() 后进先出
    queue.PriorityQueue() 优先级队列
        q = queue.PriorityQueue()
            q.put() 接收的是一个元组，第一个表示当前数据的优先级，第二个是要存放到队列中的数据
        优先级的比较：（首先需要保证在整个队列中，所有表示优先级的数据类型必须一致）
            如果都是int， 比较数字的大小
            如果都是str，比较字符串的大小（从第一个字符的ASCII开始比较）

线程池：
    在一个池子中，放固定数量的线程，这些线程等待任务，一旦有任务来，就有线程自发的去执行任务
        concurrent.futures 这个模块是异步调用的机制
        concurrent.futures 提交任务都是用submit
        for + submit 提交多任务
        shutdown 等效于pool中的close + join，不允许再继续向池中增加任务，然后让父进程（线程）等待池中所有的任务执行完成

    提交多任务的方式：
        for + submit 多个任务的提交 result拿结果
        map（func, iterable) 结果是一个生成器,使用__next__拿结果

    回调函数：
        不管死活pool进程池的方式，还是ProcessPoolExecutor的方式开启进程池，回调函数都是由父进程调用
        ThreadPoolExecutor 的回调函数是

多线程运行的时候是共享内存的，线程不安全，多线程用在无关的方向（没有需要共同操作的数据）是好的（爬虫等）


"""