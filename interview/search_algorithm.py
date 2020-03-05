# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
"""
二分查找
"""


def binary_search(nums, target, start, end):
    # print(nums[start:end], start, end)
    if end < start:
        return -1
    # print(nums)
    mid = start + (end - start) // 2
    # print("mid", start, mid, target)
    # print("value", nums[mid])
    if target > nums[mid]:
        return binary_search(nums, target, mid + 1, end)
    elif target < nums[mid]:
        return binary_search(nums, target, start, mid - 1)
    else:
        # print("bingo")
        # print(mid)
        return "eeee"


l = [1, 90, 3, 68, 4, 56, 33, 44, 1, -9, 7]
n = sorted(l)
print(n)
print(binary_search(n, 900, 0, len(l)-1))