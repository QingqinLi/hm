# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from itertools import permutations, chain

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
        2和问题演化而来，常见的解法：利用哈希表和两用双指针（性能会好一点， 和max_container解决方式一致，使用前后两个指针,
        基础是列表必须要先排序
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
            # 去重精髓
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

    """Given an array nums of n integers and an integer target, are there elements a, b, c,
     and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target."""
    """
    Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + 
    b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
    4sum问题建立在3sum问题的基础上，在3sum问题的基础上再加一层循环，先给list排序。一层循环，加两个指针，对比和和target 的关系来移动指针的
    位置，关键是要排序！排序！排序！
    去重用上面的方法会导致0，0，0，0的情况被排除
    
    """
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        len_nums = len(nums)
        for i in range(len_nums-3):
            for j in range(i+1, len_nums):
                z = j + 1
                k = len_nums - 1
                while z < k:
                    sum = nums[i]+nums[j]+nums[z]+nums[k]
                    if sum > target:
                        k -= 1
                    elif sum < target:
                        z += 1
                    else:
                        if [nums[i], nums[j], nums[z], nums[k]] not in result:
                            result.append([nums[i], nums[j], nums[z], nums[k]])
                        # result.append([nums[i], nums[j], nums[z], nums[k]])
                        z += 1
                        k -= 1
        return result

    """
    Given a sorted array nums, remove the duplicates in-place such that each element appear only once 
    and return the new length.
    去重，在原list上修改 
        真正的删除， 需要知道不能在循环中删除的原理
    """

    def removeDuplicates(self, nums):

        # for i in range(len(nums)):
        #     while i != 0 and nums[i] == nums[i - 1] and nums[i] != 'flag':
        #         nums.pop(i)
        #         nums.append('flag')
        #
        #     # else:
        #     #     count += 1
        #     # result.append(nums[i])
        #     # result.insert(0, count)
        # try:
        #     index = nums.index('flag')
        #     nums = nums[:index]
        # except Exception as e:
        #     print(e)
        # return len(nums)
        i = 1
        while 1:
            if i < len(nums):
                if nums[i] == nums[i-1]:
                    nums.pop(i)
                else:
                    i += 1
            else:
                break
        return len(nums), nums

    """
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending 
    order).

    The replacement must be in-place and use only constant extra memory.

    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand 
    column.
    permutation的题目， 因为是要求比现有的数字大的最少的数字，所以是从后往前遍历去交换，交换之后对交换之后的数字去排序取最小值。
        这样来保证获得的是比当前数字大最少的数字，当全部循环完成也没有交换数字（break）的时候，使用else，来把list反转（需求相关）
    关注点：
        解题思路，临界条件，细节判断
    """

    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        range()倒序，需要加-1的步长
        """
        for i in range(len(nums)-2, -1, -1):
            flag = False
            j = len(nums) - 1
            while j > i:
                if nums[i] < nums[j]:
                    pre = nums[i]
                    after = nums[j]
                    nums[j] = pre
                    nums[i] = after
                    sub_list = nums[i+1:]
                    sub_list.reverse()
                    print(nums[:i+1], sub_list)
                    if sub_list:
                        for k in range(len(sub_list)):
                            nums[i+k+1] = sub_list[k]
                    flag = True
                    break
                else:
                    j -= 1
            if flag:
                break
        else:
            nums.reverse()
        print(nums)

    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
    You are given a target value to search. If found in the array return its index, otherwise return -1.
    You may assume no duplicate exists in the array.
    Your algorithm's runtime complexity must be in the order of O(log n)---二分查找. 
    二分查找的变种，高低指针，先找到有序的部分再来使用二分查找，注意边界条件
    """
    def search(self, nums, target):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            # 左半边是有序的
            if nums[mid] >= nums[low]:
                # 目标在当前范围内的时候
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # 右边有序的情况
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        else:
            return -1

    """
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
    Your algorithm's runtime complexity must be in the order of O(log n).
    If the target is not found in the array, return [-1, -1].
    二分法查找：
        找到目标之后，在目标的前后查找是否有相同的值，有的话就返回范围，没有就返回-1，-1
    """
    def searchRange(self, nums, target):
        low = 0
        high = len(nums)-1
        start = -1
        end = -1
        while low <= high:
            mid = (low + high) // 2
            print(mid, low, high)
            if(nums[mid]) == target:
                start = mid
                pre = mid-1  # 这里是-1的操作
                after = mid + 1
                end = mid
                while pre >= 0 and nums[pre] == target:
                    start = pre
                    pre -= 1
                while after < len(nums) and nums[after] == target:
                    end = after
                    after += 1
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return [start, end]

    """
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
    You may assume no duplicates in the array.
    经典例子：
        二分法，找不到目标值的情况下，low指针指向的是该值应该插入的位置，恰好停在比target大的index上
    """

    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            return low

    """
    Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
    find all unique combinations in candidates where the candidate numbers sums to target.The same repeated number may be chosen from candidates unlimited number of times.
    """
    def combinationSum(self, candidates, target):
        candidates.reverse()
        result = []
        for i in range(len(candidates)):
            if not candidates[i] > target:
                if candidates[i] == target:
                    result.append(candidates[i])
                else:
                    l = [candidates[i],]
                    while target - i:
                        if len(candidates) > i:
                            for j in range(i+1, len(candidates)):
                                if



        pass


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))