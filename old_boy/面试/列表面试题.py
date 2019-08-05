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






















