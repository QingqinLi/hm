
# isinstance(),判断对象所属类型
#  issubclass(A， B) 判断类与类之间的继承关系(A是否为B的子类）
# type()子类的对象 判断是不是父类的类型 结果为false（只管一层） isintsane()可以判断子类父类的关系
# is:身份运行 内存地址相等 ==值相等

#
class A: pass


class B(A): pass


b = B()
print(isinstance(b, A))
print(type(b) is A)

print(issubclass(B, A), issubclass(A, B))


"""
__名字__
类中的特殊方法／内置方法
双下方法／魔术方法
类中的双下方法都有它自己的特殊意义

__call__ 相当于对象（）
__len__ len(obj)
__new__ 特别重要的 开辟内存空间的 类的构造方法
__str__ str(obj), %s, print(s) 都调用了__str__
所有的双下方法中，没有需要在外部直接调用的，而是总有一些其他的内置函数 特殊的语法来自动触发这些双下方法
内置函数和类的内置方法通常是有关联的

"""


# # __call__源码中经常看到
# class A:
#     def __call__(self, *args, **kwargs):
#         print("call")
#
#
# class B:
#     def __init__(self, cls):
#         print("before init")
#         self.a = cls()
#         self.a()
#         print("after init")
#
#
# A()()  # 类名()()相当于调用__call__方法
# a = A()
# a()  # 对象名()()相当于调用__call__方法
# B(A)  # 在源码中经常看到，简化代码


# __len__
# class Mydict:
#     def __init__(self, s):
#         self.s = s
#
#     def __len__(self):
#         return len(self.s)
#
#
# l = Mydict("hhhhh")
# print(len(l))
# len(obj)相当于调用了这个obj的__len__方法，如果一个obj对象没有__len__方法，那么len函数就会报错

# iter和next的例子
# __iter__  iter(obj)
# __next__  next
# def iter(obj):
#     return obj.__iter__()
# l = [1,2,3]
# iter(l) # l.__iter__()


"""
__new__（）构造方法，在实例化之后。__init__之前先执行object的new方法
__init__()初始化方法
对象：
1、开辟一个内存空间 属于对象的 new
2、被对象的空间传给self, 执行init
3、把对象的空间返回给调用者
"""


# 重要 单例类
class Single:
    __ISINSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls.__ISINSTANCE:
            cls.__ISINSTANCE = object.__new__(cls)
        return cls.__ISINSTANCE

    def __init__(self):
        print("in init", self)


s1 = Single()
s2 = Single()
# # 此时s1, s2是同一个对象


# __str__
# print一个对象相当于调用一个对象的__str__方法
# str(obj),相当于执行obj.__str__方法
# '%s'%obj,相当于执行obj.__str__方法
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return "%s %s" % (self.name, self.age)
#
#
# s = Student("xiaoming", 18)
# print(s)
# print("%s" % s)
# print(str(s))


"""
eval() 执行字符串类型的代码，并返回最终结果
exec() 执行字符串类型的数据
compile（） 将字符床类型的代码编译，代码对象能够通过exec语句执行或者eval()进行求值
参数说明:
1. resource 要执 的代码, 动态代码 段
2.  件名, 代码存放的 件名, 当传  第 个参数的时候, 这个参数给空就可以  3. 模式, 取值有3个,
1. exec:  般放 些流程语 的时候
2. eval: resource只存放 个求值表达式.
3. single: resource存放的代码有交互的时候. mode应为single

有返回值的字符 形式的代码 eval(). 没有返回值的字符 形式的代码 exec(). 一般很用到compile()
hash()获取到对象的哈希值
__import__()用于动态加载类和函数
bin() 将给的参数转换成二进制 
otc() 将给的参数转换成八进制 
hex() 将给的参数转换成十六进制
abs()返回绝对值 
divmode() 返回商和余数
round() 四舍五入
pow(a,b)求a的b次幂, 如果有三个参数. 则求完次幂后对第三个数取余
list() 将 个可迭代对象转换成列表
tuple() 将 个可迭代对象转换成元组
reversed() 将一个序列翻转, 返回翻转序列的迭代器 slice() 列表的切片
字符 相关:
str() 将数据转化成字符 
format() 与具体数据相关,  于计算各种 数, 精算等
divmode() round()
pow(a, b)
sum() 求和 
min() 求最小值 
max() 求最大值
memoryview() 查看bytes在内存中的情况
ord() 输入字符找带字符编码的位置
chr() 输入位置数字找出对应的字符
ascii() 是ascii码中的返回该值 不是就返回
repr() 返回 个对象的string形式
# %r 原封 动的写出来 
name = 'taibai' print('我叫%r' % name)
enumerate() 获取集合的枚举对象
all() 
any()
可迭代对象中全部是True, 结果才是True 可迭代对象中有 个是True, 结果就是True
zip()把元素打包成一个个元祖

"""
 # 字符
print(format('test', '<20'))
print(format('test', '>20'))
print(format('test', '^20'))
# 数值
# print(format(3, 'b'))
# print(format(97, 'c'))
# print(format(11, 'd'))
# print(format(11, 'o'))
# print(format(11, 'x'))  # 16进制小写字母
# print(format(11, 'X'))  # 16进制大写字母
# print(format(11, 'n'))
# print(format(11)) # 和d 样
# # 浮点数
# print(format(123456789, 'e'))  # 科学计数法 默认保留6位小数
# print(format(123456789, '0.2e'))
# print(format(123456789, '0.2E'))
# print(format(1.23456789, 'f'))
# print(format(1.23456789, '0.2f'))
# print(format(1.23456789, '0.10f')) #  数点计数法. 保 10位 数 print(format(1.23456789e+10000, 'F')) #  数点计数法
#
# # bytes() 把字符 转化成bytes类型
# s = '中国'
# bs = bytes(s, encoding="utf-8")
# print(bs)

# name = 'taibai'
# print('我叫%r' % name)
#
l1 = [1,2,3,]
l2 = ['a','b','c',5]
l3 = ('*','**',(1,2,3))
print(zip(l1, l2, l3))
for i in zip(l1, l2, l3):
    print(i)

"""
lamda(): 匿名函数。不需要def来声明
函数名 = lamda 参数：返回值
参数可以有多个，参数之间用逗号隔开

sorted（）排序函数 不是对原对象直接排序
sorted(iterable, key = None. reverse = False))
key:排序规则，根据函数的运算结果进行排序,

filter(function.iterable) 获得的是生成器
function:筛选函数 只能返回true，false
iterable: 可迭代对象

map（function, itrerable）函数 对每一个可迭代对象中的每一个元素进行映射，分别去执行function

"""
lst = ["麻花藤", "冈本次郎", "中央情报局", "狐仙"]
lst2 = sorted(lst, key=lambda s: len(s))
print(lst2)

lst = [1,2,3,4,5,6,7]
ll = filter(lambda x: x % 2 == 0, lst)
print(list(ll))

# lst1 = [1, 2, 3, 4, 5]
# lst2 = [2, 4, 6, 8, 10]
# print(list(map(lambda x, y:x+y, lst1, lst2)))


"""
__str__:str(obj) 要求必须实现了__str__方法 要求这个方法的返回值必须是字符串类型 print %s str

__repr__: 是__str__的备胎 如果有__str__方法 则print %s str都会先去执行__str__方法，并且使用__str__的返回值，如果没有__str__ 那么print
%s str 会执行repr __repr__ 使用：repr(), %r

查找顺序：
在子类中使用__str__，先找子类的__str__，没有的话需要向上找，只要父类不是object，就执行父类的__str__,如果除了object之外的父类都没有__str__方法
先从子类找__repr__，找不到的话再从父类中找，一直找不到的话，执行object类中的__str__方法

"""

# a = '123'
# print(a)
# print(repr(a)) # 原样输出

#
# class A:
#     def __init__(self, name):
#         self.name = name
#
#     # def __str__(self):
#     #     return self.name + "A.__str__"
#
#     # def __repr__(self):
#     #     return self.name + "A.__repr__"
#
#
# class B(A):
#
#     def __init__(self, name):
#         self.name = name
#
#     # def __str__(self):
#     #     return self.name + "B.__str__"
#
#     # def __repr__(self):
#     #     return self.name + 'B.__repr__'
#
#
# b = B("alex")
# # print("%r" % b)
# print(b)

"""
析构方法
__del__ del obj会自动触发__del__

在清楚一个对象在内存中使用的时候会触发这个对象所在的类的析构方法

python解释器在内部就可以搞定的事情
申请一块内存空间（操作系统分配）
在这块内存空间的事情 由python解释器来管理

f = open(file_path) python -- 操作系统 -- 磁盘中的文件 --- 文件操作符

"""

#
# class A:
#     def __del__(self):
#         print("del")
#
#
# a = A()
# del a

#
# # 处理文件
# class File:
#     def __init__(self, file_path):
#         self.f = open(file_path)
#         self.name = 'alex'
#
#     def read(self):
#         return self.f.read(1024)
#
#     def __del__(self):
#         # 去归还 释放一些在创建对象的时候借用的一些资源 python解释器的垃圾回收机制，回收这个对象所占得的内存的时候，python自动触发的
#         self.f.close()
#         print("close")
#
#
# f = File("text.txt")
# print(f.read())
# # 不管是主动还是被动，这个对象f占用的内存空间总会被清理（调用__del__),在__del__中触发归还操作系统资源的close（）不是python可以自己解决的


"""
item系列 和对象使用[]访问值有关系
在内置的模块中，有一些特殊的方法，要求对象必须实现__getitem__/__setitem__才能使用


"""

# obj = {'k': 'v'}
# print(obj)
# print(obj['k'])


# class B:
#     def __getitem__(self, item):
#         print("__getitem__")
#         return getattr(self, item)
#
#     def __setitem__(self, key, value):
#         self.key = value
#         print("__setattr__")
#         setattr(self, self.key, value)
#
#
# b = B()
# b['a'] = "s"
# print(b['a'])

# class B:
#     def __getitem__(self, item):
#         # print("item", item)
#         return getattr(self, item)
#
#     def __setitem__(self, key, value):
#         # print("setitem", key, value)
#         setattr(self, key, value)
#
#     def __delitem__(self, key):
#         delattr(self, key)
#
#
# b = B()
# # b.k2 = 'v2'
# # print(b.k2)
# b['k1'] = '&1'  # __setitem__
# print(b['k1'])
# # print(b['k1'])  # __getitem__
# # del b['k1']     # __delitem__
# # print(b['k1'])

# class B:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __getitem__(self, item):
#         return self.lst[item]
#
#     def __setitem__(self, key, value):
#         self.lst[key] = value
#
#     def __delitem__(self, key):
#         self.lst.pop(key)
#
#
# b = B([1, 3, 5, 6, 7])
# print(b[0])
# b[0] = 'sss'
# print(b[0])
# del b[0]
# print(b.lst)


"""
hash()方法：能够把一个要存在内存中的值经过一系列的计算得到一个唯一的地址（当地址对象的内存中有值时，会去判断要存储的值和当前存储的值是否相等
不相等的话会再次计算hash，存到另外的地方，相同的话覆盖存储）--set去重原理

对同一个值在多次执行python代码的时候hash值是不一样的，但是对于同一个值，在同一次执行python代码的时候hash值永远不变
字典的寻址：hash算法 空间换时间 占用内存大，查找和插入很快 不会随着key的增加而缓慢 与list相反 key必须是不可变对象（可hash）
set去重： hash算法
hash(obj) obj内部必须实现了__hash__方法

"""


"""
__eq__方法 == 使用调用的
"""


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 重新定义__eq__
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        return False


a = A("alex", 23)
b = A("alex", 3)
print(a == b)  # 因为对象的内存地址不同，所以用==判断的时候，一定是False


























