"""
闭包：内层函数，对外层函数（非全局）变量的引用,使用函数名.__closure__返回cell就是闭包，返回None就不是
作用：
1、使变量常驻内存

迭代器：
dir(obj) 打印这个对象中的方法和函数
if __iter__ in dir(obj): 遵守了可迭代协议 可迭代对象
if __next__ in dir(obj): 使用__next__来获取到一个迭代器的元素(超过长度会报stopIteration错）迭代器
优点：
1、节省内存
2、惰性机制
3、不能反复，只能向下执行


"""


# def func1():
#     name = 'alex'
#
#     def func2():
#         print(name)
#     func2()
#     print(func2.__closure__)
# func1()

l = [1, 3, 4, 6, 7, 22, 55, 653]
c = l.__iter__()
while True:
    try:
        print(c.__next__())
    except StopIteration:
        break