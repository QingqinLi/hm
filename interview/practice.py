# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import re
import math

s = 'this is a sentence&and this is a word too'

# s_re = re.split('[ |&]', s)
# print("re", s_re)
# ma = re.match("this", s).group()
# se = re.search("is", s).group()
# f = re.findall("is", s)
# print(f)


def bubble_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def quick_sort(nums, left, right):
    if left >= right:
        return
    start = left
    end = right
    ref = nums[left]
    while left < right:
        print('left', left, right)
        while left < right and nums[right] >= ref:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        while left < right and nums[left] <= ref:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]

    quick_sort(nums, start, left-1)
    quick_sort(nums, left+1, end)
    return nums


# l = [6, 4, 6, 2, 9, 3, 1, 0, 90]
# print(quick_sort(l, 0, len(l)-1))

"""
选择排序
"""


def selectSort(nums):
    """
    每次选择最大/小的元素
    :param nums:
    :return:
    """
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                nums[j], nums[min_index] = nums[min_index], nums[j]
    return nums


"""
素数联习
"""


def prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True


print(selectSort([1, 3, 2, 0, 45, 67, 34, 23]))
