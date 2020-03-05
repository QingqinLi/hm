# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""

"""
选择排序每， 时间复杂度高O(n*n)
"""


def find_min(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    result_list = []
    for i in range(len(arr)):
        result = find_min(arr)
        result_list.append(arr.pop(result))
    return result_list


l = [4, 5, 6, 1, 3, 7, 2, 2, 44]
print(selection_sort(l))
