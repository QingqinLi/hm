# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


def twoSum(nums, target):
    for i in range(len(nums)):
        if target-nums[i] in nums[i+1:]:
            print(target-nums[i], nums)
            return [i, nums.index(target-nums[i], i+1)]

twoSum([3,2,4], 6)