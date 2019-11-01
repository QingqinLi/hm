# 列表推导式
lst1 = [i for i in range(1, 101) if i % 3 == 0]
lst2 = [i ** 2 for i in range(1, 101) if i % 3 == 0]
# print(lst1, "\n", lst2)
names = [["name", "luara", "mikeee", "Alice", "ee"], ['ad', 'dd', 'ff', 'gg']]
# 双层循环
name = [name for first in names for name in first if name.count("e") > 2]
print(name)

# 生成器表达式
# 与列表生成器基本相同。[]换成（）,数据：要一个给一个
g = (i for i in range(10))
print("g", g)
for i in g:
    print(i)

"""
生成器：(本质是迭代器）可以分段执行函数，节省内存，惰性机制 只能往前
1、通过生成器函数（函数中包含yeild的函数。生成器函数执行，获取到的是生成器，而不是函数的执行
2、生成器表达式：（结果 for 变量 in 可迭代对象 if 筛选）
取值：
1、__next__()
2、send() 给上一个yield的位置传一个值，第一个和最后一个不用传值
3、可以用for循环
4、list(g)
惰性机制

推导式：
1、列表推导式
2、字典推导式{key:value for 变量 in 可迭代对象 if 筛选}
3、集合推导式{} 字典去重
4、生成器推导式
5、
没有元祖推导式

"""


# 面试题 惰性机制 不使用不取值
def add(a, b):
    return a+b


def hell():
    for i in range(4):
        yield i


g = hell()

"""
 g = (add(n, i) for i in 【0， 1， 2， 3)
 g = (add(n, i) for i in (add(n, i) for i in [0, 1, 2, 3))
 取值的时候再计算， 此时n为10
"""
for n in [2, 10]:
    g = (add(n, i) for i in g)

print("test", list(g))

# s = input("input a+b：")
# print(eval(s))
#
# s = 'for i in range(10):print("test", i)'
# exec(s)


# reversed（）返回的是迭代器
lit = ["1", "2", "3"]
lis_2 = reversed(lit)
print(list(lis_2))

s = slice(1, 3)
print(lit[s])
