"""
生成器：
本质是迭代器
获取生成器的方式
1、通过生成器函数
2、通过各种推导式来实现生成器
3、通过数据的转换可以获取生成器

send方法 也可以让生成器执行到下一个yield
send()和__next__()区别：
1、都是让生成器向下走一次
2、send可以给上个yield的位置传递值，不呢给最后一个yield发送值，第一次和最后一次执行生成器代码的时候不能使用send（）

生成器可以用for循环获取
for i in gen
len(生成器）

列表推导式
有列表推导式， 字典推导式， 集合推导式，没有元祖推导式
(i for i in list)

列表推导式和生成器表达式的区别：
列表推导式比较耗内存，一次性记载，生成器表达式几乎不占用内存，使用的时候才会分配和使用内存
列表推导式得到的是一个列表，生成器表达式获取到的是一个生成器

"""


# def func():
#     print(111)
#     yield 222
#     print(33)
#     yield 44
#
#
# # func() #这是一个生成器函数，通过函数的执行获得一个生成器, 使用__next__()来执行
# gener = func()
# print(gener.__next__())
# print(gener.__next__())
# yield 来分段执行函数

# def cloth():
#     for i in range(0, 10000):
#         yield "cloth" + str(i)
#
#
# cl = cloth()
# print(cl.__next__())
# print(cl.__next__())


def eat():
    print("我吃 么啊")
    a = yield "馒头"
    print("a=",a)
    b = yield " 饼"
    print("b=",b)
    c = yield " 菜盒 "
    print("c=",c)
    yield "GAME OVER"

gen = eat()
print(gen.__next__())
print(gen.send("122"))
print(gen.__next__())


# 列表推导式
# lst = [i for i in range(10) if i % 2 == 0]
# print(lst)
#
# # 生成器表达式
# gen = (i for i in range(1, 100) if i % 3 == 0)
# print(gen)
# for i in gen:
#     print(i)


# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#           ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
#
# gen = (name for i in range(len(names)) for name in names[i] if name.count("e") == 2)
# for i in gen:
#     print(i)

# # 字典推导式
# lst1 = ['jay', 'jj', 'sylar']
# lst2 = ['周杰伦', ' 俊杰', '邱彦涛']
# dic = {lst1[i]: lst2[i] for i in range(len(lst1))}
# print(dic)

# 集合推导式 直接生成一个集合 集合的特点是无序 不重复，所以集合推导式自动去重
# lst = [1, -1, 8, -8, 12] # 绝对值去重
# s = {abs(i) for i in lst}
# print(s)

# 面试题目 惰性机制, 不到最后不会拿值,所以最后n是10
# def add(a, b):
#     return a + b
#
#
# def test():
#     for r_i in range(4):
#         yield r_i
#
#
# g = test()
#
# for n in [2, 10]:
#     g = (add(n, i) for i in g)
# #     g = (add(n, i) for i in ((add(n, i) for i [0, 1, 2, 3]))
# print(list(g))
