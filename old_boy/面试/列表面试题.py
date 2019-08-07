"""
去重 保持原来的顺序
"""
l1 = [11, 2, 33, 7, 11, 8, 19, 1, 2]

ll = []
for i in l1:
    if i not in ll:
        ll.append(i)

print(ll)


l2 = list(set(l1))
print(l2)

# 记住索引来描述元素出现的顺序

# 通过sort key关键字 内置函数来排序
print(l1.index(11))

l2.sort(key=lambda x: l1.index(x))
print(l2)


name = [
    {"name": "sylar", "age": 88},
    {"name": "Gold", "age": 38},
    {"name": "Eva_J", "age": 18},
    {"name": "Alex", "age": 9000},
]

# 将l3的元素按照age由小到大排序
ret = sorted(name, key=lambda x: x['age'])
print(ret)

# 内置方法sort是对原来的列表操作，不是新生成一个列表
name.sort(key=lambda x: x['age'])
print(name)


# """
# 编写代码生成如下列表：
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12]]
# """

l = [i for i in range(5)]
print(l)
ll = []
for i in range(4):
    ll.append([m * i for m in l])
# print(ll)

# l1 = []
ll1 = []
for i in range(4):
    l1 = []
    for j in range(5):
        l1.append(j*i)
    # print(l1)
    ll1.append(l1)
    # l1 = []
# print(ll1)

print([[i * j for i in range(5)] for j in range(4)])

"""
# 今日面试题：
list可变对象 在一次的运行过程中不会改变？？？？？看视频
"""


def extend_list(v, li=[]):
    li.append(v)
    return li


list1 = extend_list(10)
print(list1)  # [10, ]
list2 = extend_list(123, [])
list3 = extend_list('a')
#
print(list1)  # [10, a]
print(list2)  # [123]
print(list3)  # [10, a]
#
print(list1 is list3)

# 第二题：问以下代码的输出结果是什么？
list1 = ["a", "b", "c", "d", "e"]
print("test", list1[10:])
print(list1[1:0])
print(list1[1::2])
# list1 = ["a", "b", "c", "d", "e"]
# print(list1[10:])  # []
# print(list1[1:])  # ["b", "c", "d", "e"]
# print(list1[1:0])  # []

# print(list1[1::2])  # "b", "c", "d", "e"



list2 = reversed(list1)
print(list2, list(list2))
print(list1)  # 不改变原列表
print(list1[::-1])  # 利用切片翻转列表，生成一个新列表不是操作的原来的列表
print(list1)

# 直接操作原来列表的方法
list1 = [11, 22, 33]
# append()
list1.append([44, 55])
print(list1)
# remove()
list1.remove(33)
print(list1)
# extend()
list1.extend([44, 55])
print(list1)
list1.insert(0, 0)
print(list1)

print("*"*20)
# 1求学要严谨
list1.insert(9, 99)
print(list1)

list1.pop(0)  # 返回被弹出的那个元素
print(list1)
# list1.pop(9)  # IndexError: pop index out of range
# print(list1)
#
list1.reverse()  # 反转原来的列表
print(list1)
#
list1.clear()  # 清空原列表
print(list1)

# 第三题：如何打乱一个有序的列表？

# listll = [11, 22, 33, 44]
# import random
# random.shuffle(listll)
# print(listll)

# 大写表示常量
# join的元素只能是str
l9 = [11, 12, 13, 14]
ret = '+'.join([str(x) for x in l9])
print(ret)

# python
a = 100
b = 200
c = a if a > b else b
print(c)


"""
问:执行完下面的代码后,  l,m的内容分别是什么?
"""
import copy


# def func(m):  不要再可迭代对象遍历过程中改变他的长度
#     for k, v in m.items():
#         m[k+2] = v+2
#
#
# m = {1: 2, 3: 4}
#
# l = m l和m指向了同一块内存地址  # copy.copy()浅拷贝, copy.deepcopy()  l = {1:2， 3:4}
#
# l[9] = 10  # l: {1:2, 3:4, 9:10}
#
# func(l)  # l: {1:2, 3:4, 5:6, 9:10, 11:12}
#
# m[7] = 8  # {1:2, 3:4, 7:8}

# l: {3:4, 5:6, 11:12}
# m: {}

# list1 = [11, 22, 33, 44]
# for i in list1:
#     list1.append("a")


# 引申补充
# 回去复习下：
# 1. 小数据池
# 2. 深浅拷贝的概念和用法


# list1 = [11, 22, 33, 44]
# list2 = list1[::]  # 类似于深copy
# list1[0] = 10
# print(list1)
# print(list2)

print(round(6.5))
