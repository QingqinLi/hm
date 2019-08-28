# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class Solution:
    """中值"""
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        len_list = len(nums1)
        if len_list % 2 == 0:
            print(len_list)
            return (nums1[len_list//2] + nums1[len_list//2 - 1]) / 2
        else:
            return nums1[(len_list-1)//2]
        # print(nums1)


    """
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
    which together with x-axis forms a container, such that the container contains the most water. 
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
    （1）以最大桶底开始，设置首尾两个指针left、right。
    （2）当height[left] < height[right]，left从左向右移动一个位置。
    （3）当height[left] >= height[right]，right从右向左移动一个位置。
    （4）每移动一次，就更新一下，容器的最大的容量，直到结束。
    （5）为什么这样做，就可以选择出最大的容器？可以简单的理解，即，桶底，保持最大，我只要选取最长的两个直线，那么我一定可以选择到最大的容器，不太严谨哈，其实可以用反证法证明的。

    """

    def maxArea(self, height) -> int:
        area_list = []
        left = 0
        right = len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * abs(right - left)
            area_list.append(area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max(area_list)

    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique 
    triplets in the array which gives the sum of zero.
    3和问题：
        2和问题演化而来，常见的解法：利用哈希表和两用双指针（性能会好一点， 和max_container解决方式一致，使用前后两个指针
    """

    def threeSum(self, nums):
        # result_list = []
        # len_nums = len(nums)
        # for i in range(len_nums):
        #     for j in range(i+1, len_nums):
        #         for z in range(j+1, len_nums):
        #             if nums[i] + nums[j] + nums[z] == 0:
        #                 result_list.append([nums[i], nums[j], nums[z]])
        # # 去重
        # b = []
        # c = []
        # for i in result_list:
        #     if set(i) not in b:
        #         b.append(set(i))
        #         c.append(i)
        #
        # return c
        result_list = []
        nums.sort()

        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            z = len(nums) - 1

            while j < z:
                sum_3 = nums[i] + nums[j] + nums[z]
                if sum_3 == 0:
                    result_list.append([nums[i], nums[j], nums[z]])
                    z -= 1
                    j += 1
                    # 去重(!!!) 避免重复操作，挪动到最后一个进行操作，避免对全部结果进行去重操作
                    while j < z and nums[j] == nums[j-1]:
                        j += 1
                    while j < z and nums[z] == nums[z+1]:
                        z -= 1

                elif sum_3 > 0:
                    z -= 1
                else:
                    j += 1

        return result_list

    """
    Given an array nums of n integers and an integer target, find three integers in nums such that the sum is 
    closest to target. Return the sum of the three integers. You may assume that each input would have exactly one 
    solution.
    """

    def threeSumClosest(self, nums, target):
        nums.sort()
        len_num = len(nums)
        result_dict = {}
        for i in range(len_num-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            z = len_num - 1
            while j < z:
                while j < z and j != i+1 and nums[j] == nums[j-1]:
                    j += 1
                while j < z and z != len_num - 1 and nums[z] == nums[z + 1]:
                    z -= 1
                if j == z:
                    break
                result_dict[abs(nums[i] + nums[j] + nums[z] - target)] = (nums[i] + nums[j] + nums[z])
                if nums[i]+nums[j]+nums[z] > target:
                    z -= 1
                else:
                    j += 1
        key = min(result_dict.keys())
        return result_dict[key]

    """Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target."""


s = Solution()
print(s.threeSumClosest([-10,0,-2,3,-8,1,-10,8,-8,6,-7,0,-7,2,2,-5,-8,1,-4,6], 18))