"""
编译和解释的区别：
编译器：把源程序的每一条语句都编译成机器语言。并保存成二进制文件，运行时候可以直接以机器语言来运行此程序，速度更快。
       一般会有预编译的过程对代码进行优化，可以脱离语言环境独立运行，不同的操作系统移植会出现问题
解释器：只在执行程序时，才一条一条的解释成机器语言给计算机来执行，所以运行速度并不如编译后的程序运行的快，
       有良好的平台兼容性，每次运行都需要重新解释一遍，性能上不如编译型语言
python的优缺点：
先看优点
1. Python的定位是“优雅”、“明确”、“简单”，
2. 开发效率非常高，Python有非常强大的三方库，基本上你想通过计算机实现任何功能，Python官方库都有相应的模块进行支持，直接下载调用后，在基础库的基础上再开发，大大降低开发周期，避免重复造轮 。
3. 高级语言————当你用Python语 编写程序的时候，你无需考虑诸如如何管理你的程序使用的内存一类的底层细节
4. 可移植性————由于它的开源本质，Python已经被移植在许多平台上(经过改动使它能够工作在一同平台上)。如果你小心地避免使用依赖于系统的特性，那么你的所有Python程序无需修改就几乎可以在市场上所有的系统平台上运
5. 可扩展性————如果你需要你的一段关键代码运行得更快或者希望某些算法不公开，你可以把你的部分程序用C或C++编写，然后在你的Python程序中使用它们。
6. 可嵌 性————你可以把Python嵌入你的C/C++程序，从而向你的程序用户提供脚本功能。
再看缺点:
1. 速度慢，Python 的运行速度相比C语言确实慢很多，跟JAVA相 也要慢 些，因此 这也是很多所谓的   屑于使 Python的主要原因，但其实这 所指的运 速度 慢在 多数情况下 户是 法直接感知到的，必须借助测试 具才能体现出来， 如 你 C运 个程序花 0.01s, Python是0.1s,这样C语 直接 Python快 10倍, 算是 常夸张 ，但是你是 法直接通过 眼感知的，因为 个正常 所能感知的时 间最 单位是0.15-0.4s左右，哈哈。其实在 多数情况下Python已经完全可以满  你对程序速度的要求，除 你要写对速度要求极 的搜索引擎等，这种情况下，当 然还是建议你 C去实现的。
2. 代码 能加密，因为PYTHON是解释性语 ，它的源码都是以名 形式存放的，  过我 认为这算是 个缺点，如果你的项 要求源代码必须是加密的，那你 开始就  应该 Python来去实现。
3. 线程 能  多CPU问题，这是Python被 诟病最多的 个缺点，GIL即全局解释  锁(Global Interpreter Lock)，是计算机程序设计语 解释  于同步线程的  具，使得任何时刻仅有 个线程在执 ，Python的线程是操作系统的原 线程。 在Linux上为pthread，在Windows上为Win thread，完全由操作系统调度线程的 执 。 个python解释 进程内有 条主线程，以及多条 户程序的执 线程。即 使在多核CPU平台上，由于GIL的存在，所以禁 多线程的并 执 。关于这个问题 的折衷解决 法，我们在以后线程和进程章节 再进 详细探讨。

当然，Python还有 些其它的 缺点，在这就    举 ，我想说的是，任何  语  都 是完美的，都有擅 和 擅 做的事情，建议各位 要拿 个语 的劣势去跟另 个 语 的优势来去 较，语 只是 个 具，是实现程序设计师思想的 具，就像我们之前中 学学 何时，有的时候需要要圆规，有的时候需要 三 尺 样，拿相应的 具去做它最擅  的事才是正确的选择。之前很多 问我Shell和Python到底哪个好?我回答说Shell是个 脚本语 ，但Python 只是个脚本语 ，能做的事情 多，然后 有钻  尖的 说完全 没必要学Python, Python能做的事情Shell都可以做，只要你 够 B,然后 举  Shell 可以写俄罗斯 块这样的游戏，对此我能说表达只能是， 要跟SB 论，SB会把你拉到跟 他 样的 度，然后 充分的经验把你打倒。

python的解释器：

CPython；官方 使用最广
IPython: 基于cpython的一个交互式解释器，与cpython的区别仅在于交互方式上有所增强
PyPy：JIT技术，对python代码进行动态编译（不是解释），可以显著提高python代码的执行速度
JPython：运行在java平台上的python解释器，可以直接把python代码编译成java字节码
IronPython：与Jpython蕾丝，是运行在微软.net平台上的解释器，可以直接把python代码编译成.net的字节码

python2.x默认编码为ASSIC.在程序的开始要写# -*- encoding:utf-8 -*-
python3.x默认编码为utf-8

变量的命名规则：
由数字，字母，下划线组成，不能用数字开头， 更不能是纯数字，不能是python的关键字，不要用中文，要有意义，区分大小写，不能太长
推荐使用驼峰命名法或者下划线命名

python中不寻在绝对的常量，预定俗成，所有的字母大写就是常量

常见的数据类型：
int:整数，64位机器上int的范围：-2 ** 63 ～ 2 ** 63-1 bit_length() 求二进制长度，python3中所有的整数都是int类型，python2中如果数据量
比较大，会使用long类型，在python3中不存在long类型
str: 字符串 多行赋值一个字符串，用三引号 字符串是不可变的对象，所有任何操作都不会对原字符串有影响
                1. upper() 转换成大写
                2. strip() 去掉空格
                3. replace() 替换
                4. split() 切割
                5. format() 格式化输出
                6. startswith() 判断是否以xxx开头
                7. find() 查找. 找不到返回-1
                8. len() 内置函数. 直接使用. 不用点操作 求字符串的长度, __len__()
                9. capitalize() 首字母大写 swapcase() 大小写互相转换 casefold()转换成小写，和lower（）的区别是。lower（）对某些字符的支持不够好，东欧的一些字符 title（）每个被特殊字符隔开的字符串首字母大写
                10. center(num, "str") 填充成num长, 居中展示，其他的字符填充str
                11、s.find()找元素，没有的话则返回-1， s.index()找位置，找不到程序会报错
                12、s.isalnum() 是否由字母和数字组成，s.isalpha() 是否由字母组成 s.isdigit()／s.isdecimal()/s.isnumeric()（这个可以识别中文） 判断是否由数字组成

bool：布尔 带空的是False, 不带空的True
list: 列表
tuple: 元祖
dict: 字典
set: 集合

s = "_".join(s) 集合拼接成字符串

不能在循环中删除 list，dict等的元素（删除之后，长度改变，导致出现问题）一般使用另外一个列表来记录要删除的内容，然后循环删除
 li = [11, 22, 33, 44]
del_li = []
for e in li:
    del_li.append(e)
for e in del_li:
    li.remove(e)
print(li)

dict中的fromkey(),可以帮我们通过list来创建 个dict


input（）用户交互 python2.x中为raw input(),接收到的数据为字符串类型

if循环嵌套，在实际的开发中，不要超过三层

while condition:
    代码块
    break：立刻跳出循环
    continue：停止本次循环，继续执行下一次循环
else:
    没有break后执行的语句

类型转换:
元组 =>  表 list(tuple)  表 => 元组 tuple(list)
list=>str str.join(list) str=>list str.split()
转换成False的数据: 0,'',None,[],(),{},set() ==> False

"""


# print(dic)
# s = "title"
# s1 = s.capitalize()
# print(s1)
# # 使用while循环输出1 2 3 4 5 6 7 8 9 10
# num = 1
# while num < 11:
#     print(num, end=" ")
#     num += 1
# print()
#
# # 求1-100的所有数的和
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)
#
# # 输出1-100内的所有奇数
# odd_list = []
# even_list = []
# for i in range(1, 101):
#     if i%2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
#
# print(odd_list, even_list)
#
# # 求1-2+3-4+5 ... 99的所有数的和
# sum = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         sum -= i
#     else:
#         sum += i
# print(sum)
#
# # 用户登录（三次重试机会）
# num = 1
# while num < 4:
#     name = input("input your name: ")
#     password = input("input your password: ")
#
#     if name == "alex" and password == "123456":
#         print("登录成功")
#         break
#     else:
#         print("error, again")
#     num += 1
# else:
#     print("登录失败")


"""
格式化输出：
1、%s, %d, %f... %s是通用的。当字符串中有%（表示百分比）的时候，需要使用%%转义
2、{}.format(),默认按照顺序，可以制定顺序，可以用关键字

基本运算符：
／：除法
//:返回商的整数部分
逻辑运算符：
优先级 ()>not>and>or,同以优先级从左向右计算

GBK, 国标码占 2个字节
UTF-8: 每个字符最少占8位. 每个字符占 的字节数不定.根据 字内容进 具体编码. 比如. 英 . 就 个字节就够 . 汉 字占3个字节. 这时即满  中 . 也满  节约. 也是 前使 频率最 的 种编码
UTF-16: 每个字符最少占16位. 
GBK: 每个字符占2个字节, 16位.
1. 最早的计算机编码是ASCII. 美国人创建的. 包含了英文字母(大写字母, 小写字母). 数字, 标点等特殊字符!@#$%
            128个码位 2**7 在此基础上加了一位 2**8
            8位. 1个字节(byte)
            不支持  中文
            支持    英文  数字  符号
2. GBK 国标码 16位. 2个字节(双字节字符) 支持  中文,英文,数字,符号
3. unicode 万国码   32位, 4个字节 支持  中文,英文,数字,符号 长度可变的万国码 最少用8位
4. utf-8:  英文  8 bit 1个字节
           欧洲文字 16bit 2个字节
           中文 24bit  3个字节

        8bit => 1 byte
        1024 byte = > 1kb
        1024 kb => 1mb
        1024mb => 1gb
        1024gb = > 1tb
ASCII: 英文字母, 数字, 特殊字符, 8bit 1byte
GBK: 中文 国标码.16bit 2byte
unicode: 万国码. 32bit 4byte
utf-8: 英文: 8bit 1byte   欧洲文字:16bit 2byte 中文: 24bit 3byte
"""

# print("%s 学习了%%2的内容" % "xiaoming")

# print(3 > 4 or 4 < 3 and 1 == 1)
# print(1 < 2 and 3 < 4 or 1 > 2)
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)
# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

# x or y  if x is True, then x, else y
# print(8 or 4)

# x and y if x is True, then y, else x
# print(0 and 3)

# print(0 or 4 and 3 or 7 or 9 and 6)

"""
list操作：（list可变所有是直接在原来的对象上进行了操作）
1、增： list.append() insert（）extend()增加一个可迭代的对象（list）
2、删： list.remove()删除指定元素，参数为元素值 pop()默认删除最后一个，有参数则删除第几个元素，clear()清空list del list[start:end]切片删除
3、改：索引修改 有步长的时候需要注意元素的个数
4、查：for循环
5、常用方法 len(), count() sort()排序（默认升序）修改的是原list
6. tuple 元组
        不可变的列表. 只读列表. 有索引和切片.
        不可变的是它内部子元素. 如果子元素是列表. 列表中的元素是可以变的.
7. range()
        数数
        有一个参数:结束为止
        两个参数: 1. 起始位置, 2.结束位置
        三个参数: 1. 起始位置, 2. 结束位置. 3.步长
        
元祖：
俗称不可变的列表，或者只读列表，除了修改之外，其他的操作和list一样

dict：
key必须是不可变的（可哈希）value没有要求，可以保存任意类型的数据
1、增；dict.setdefault(key, [value]) 如果 dict中没有这个key-value 可以通过setdefault设置默认值，如果dict已经存在，setdefault不会起作用
2、删除 dict.pop(key) del dict[key] dic.popitem()随机删除 dict.clear() 清空
3、修改
dic = {"id": 123, "name": 'sylar', "age": 18}
dic1 = {"id": 456, "name": "麻花藤", "ok": "wtf"}
dic.update(dic1) # 把dic1中的内容 新到dic中. 如果key重名. 则修改替换. 如果 存 在key, 则新增.
4、查询 使用key来查询具体的数据
"""
# lst = [1, 2, 3, 4, 5, 6, 0]
# # lst[1:4:2] = ["str", "ss"]
# print(lst)
# lst.sort()
# print(lst)

"""
集合：不重复，无序，里面的函数必须是可以hash的
1、增：
s = {1, 2, 4}
s.add(5)
s.update({1, 7, 8}) 迭代更新 参数是可迭代对象
2、删
s.pop() 随机删除
s.remove() 删除元素 元素不存在会报错
s.clear() 清空set集合
3、修改
先remove，再add
4、查询
可迭代 for循环

5、交集：
print(s1 & s2) # {'   '} p
rint(s1.intersection(s2)) # {'   '}
并集：
 print(s1 | s2) # {'刘科 ', '冯乡 ', '赵四', '   ', '刘能'} 
 print(s1.union(s2)) # {'刘科 ', '冯乡 ', '赵四', '   ', '刘能'}
# 差集
print(s1 - s2) # {'赵四', '刘能'} 得到第 个中单独存在的 
print(s1.difference(s2)) # {'赵四', '刘能'}
# 反交集
print(s1 ^ s2) # 两个集合中单独存在的数据 {'冯乡 ', '刘能', '刘科 ', '赵四'} 
print(s1.symmetric_difference(s2)) # {'冯乡 ', '刘能', '刘科 ', '赵四'}
s1 = {"刘能", "赵四"}
s2 = {"刘能", "赵四", "   "}
#  集
print(s1 < s2) # set1是set2的 集吗? 
True print(s1.issubset(s2))
# 超集
print(s1 > s2) # set1是set2的超集吗? 
False print(s1.issuperset(s2))
"""
# set1 = {1, [1, 3]}
# print(set1)
# 报错 因为包含来不可hash的对象，kusr

# s = {1, 2, 4}
# s.add(5)
# s.update({1, 7, 8})
# print(s)
"""
解构：
a, b = 1, 3
"""

"""
is 和 ==
==比较的是两遍的值
is 比较的是内存地址 id()获取内存地址
小数据池
-5～256 在这个范围内的数 用is判断是同一个内存地址（Pycharm不适用）
str类型：如果有特殊字符，那么他们的内存地址就是不一样的
如果字符长度超过20，他们的内存地址也是不一样的


"""

"""
编码和解码
python3在程序运行阶段，使用的是unicode，显示所有的内容

bytes类型 传输和存储使用的是bytes
encode(编码方式） 编码 拿到明文编码后对应的字节
decode（编码方式） 解码 将编码后的字节解码成对应的明文

"""


"""
深浅拷贝
浅拷 . 只会拷贝第一i层. 第层的内容不会拷 . 所以被称为浅拷 
import copy
copy.deepcopy()深拷贝
深度拷贝 把元素内部的元素完全进行拷贝复制. 不会产省一个改变另以个跟着改变的问题
"""

# lst1 = ["何炅", "杜涛", "周"]
# lst2 = lst1.copy()
# lst1.append("嘉诚")
# print(lst1)
# print(lst2)
# print(id(lst1), id(lst2))
# 结果:
# 两个lst完全  样. 内存地址和内容也  样. 发现实现 内存的拷
# import copy
# lst1 = ["何炅", "杜涛", "周渝 ", ["麻花藤", "芸", "周笔畅"]]
# lst2 = lst1.copy()
# list3 = copy.deepcopy(lst1)
# lst1[3].append(" 敌是多磨寂寞")
#
# print(lst1)
# print(lst2)
# print(list3)
# print(id(lst1[3]))
# print(id(lst2[3]))
# 结果:
# ['何炅', '杜 涛', '周渝 ', ['麻花藤', ' 芸', '周笔畅', ' 敌是多磨寂寞'
#
# # 面试题目 a的内存地址赋给a[1] 此时a[1]就是a，多层循环的效果
# a = [1, 2]
# a[1] = a
# print(a[1])
