import gevent
from gevent import monkey
import time
"""
gevent 可以实现 当函数遇到io操作时候，就自动切换到另一个函数
g1 = gevent.spawn(func, 参数)
gevent.join(g1) 让func执行完毕
gevent.joinall([...]) 
func停止的原因：
    func执行完了
    遇到IO操作
    
"""


# def func():
#     print("122")
#     gevent.sleep(1)
#     print("222")
#     gevent.sleep(2)
#     print("333")
#
#
# def func1():
#     print("444")
#     gevent.sleep(1)
#     print("555")
#     gevent.sleep(1)
#     print("666")
#
#
# g1 = gevent.spawn(func)
# g2 = gevent.spawn(func1)
# gevent.joinall([g1, g2])


# ********** 解决gevent不识别其他io操作的问题
monkey.patch_all()  # 可以让gevent识别大部分常见的IO操作
def func():
    print("122")
    # time.sleep(1)
    print("222")
    s = input()
    time.sleep(2)
    print("333")


def func1():
    print("444")
    time.sleep(1)
    print("555")
    time.sleep(1)
    print("666")


g1 = gevent.spawn(func)
g2 = gevent.spawn(func1)
gevent.joinall([g1, g2])