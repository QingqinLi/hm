# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
"""
1234能组层多少个不重复不相同的三位数
permutation 重在排列，返回迭代器，需要转换成list使用， leetcode有4道permutation相关的题目
chain()常用在想要对不同的集合中所有元素执行某些操作的时候
"""
from collections import deque
from functools import reduce, partial
from itertools import permutations, chain

ret = permutations('1234', 3)
# print(list(ret))

list1 = [11, 22, 33]
list2 = ['aa', 'bb', 'cc']
print(list(chain(list1, list2)))