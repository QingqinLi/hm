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
    find all unique combinations in candidates where the candidate numbers sums to target.The same repeated number may 
    be chosen from candidates unlimited number of times.
    暴力解法：
        组合任意多数， 然后确认是否为目标数字，并返回所有可能的组合，必须要遍历所有的可能性才能求解
    """
    def combinationSum(self, candidates, target):

        # 递归算法 实现
        result = []

        def rerc(l, t, r):
            print("start", l, t, r)
            if t in l:
                r.append(t)
                result.append(r)
            elif l:
                need_t = t
                print("need_t", t)
                print("=="*10)
                for i in range(len(l)):
                    print("hello", i, l[i], t, need_t)
                    r.append(l[i])
                    t -= l[i]
                    if l and t >= 0:
                        return rerc(l, t, r)
                    else:
                        print("else", l, t, need_t)
                        t = need_t
                print("||" * 10)

        candidates.sort(reverse=True)
        print("c", candidates)
        # result = []
        for i in range(len(candidates)):
            if not candidates[i] > target:
                if candidates[i] == target:
                    result.append(candidates[i])
                else:
                    print("*" * 20)
                    l = candidates[i:]
                    rerc(l, target, [])

        print(result)

    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest 
    sum and return its sum.
    解决：
        最大子串一定是正数开头，修改原list
        子串累计小于0的时候，不需要继续增加元素
    """

    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        flag = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                flag = i
                break
        nums = nums[flag:]

        m = min(nums)
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum > m:
                    m = sum
                if sum <= 0:
                    break

        return m


    """
    Students are asked to stand in non-decreasing order of heights for an annual photo.
    Return the minimum number of students not standing in the right positions.  (This is the number of students that 
    must move in order for all students to be standing in non-decreasing order of height.)
    list复制：
        使用切片法： 会生成原来对象的一个copy
        new_list = list(old_list)
        new_list = copy.copy(old_list) 速度较慢 需要先确定要复制内容的数据类型
        new_list = copy.deepcopy(old_list) copy库中的深拷贝 
    """
    def heightChecker(self, heights):
        high = list(heights)
        high.sort()
        count = 0
        for i in range(0, len(heights)):
            if not heights[i] == high[i]:
                count += 1
        return count

    """
    Given an unsorted integer array, find the smallest missing positive integer.
    """

    def firstMissingPositive(self, nums):
        for i in range(1, len(nums) + 1):
            if i not in nums:
                return i
        else:
            return len(nums) + 1

    """
    You are given an n x n 2D matrix representing an image.
    Rotate the image by 90 degrees (clockwise).
    solution:
        1、对称交换
        2、反转每一行
    """

    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0, len(matrix)):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for line in matrix:
            line.reverse()

    """
    Given an array of integers arr, write a function that returns true if and only if the number of occurrences of 
    each value in the array is unique.
    """

    def uniqueOccurrences(self, arr) -> bool:
        set_arr = set(arr)
        count_list = []
        for i in set_arr:
            count = arr.count(i)
            if count in count_list:
                return False
            count_list.append(count)
        else:
            return True

    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it    is able to trap after raining.
    """
    def trap(self, height) -> int:
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                if height[j] < 1:
                    pass
    """
    Given an array of non-negative integers, you are initially positioned at the            first index of the array.
    Each element in the array represents your maximum jump length at that position.

    Determine if you are able to reach the last index.
    从最后的数字开始，看哪个可以到达卒后一个数字， 递归
    """

    def canJump(self, nums) -> bool:
        if len(nums) == 1:
            return True
        end_list = []
        len_num = len(nums)

        # def go(start, step):
        #     if start + step + 1 >= len_num:
        #         return True
        #
        #     else:
        #         for i in range(start + step, start, -1):
        #             if i in end_list:
        #                 continue
        #             if go(i, nums[i]):
        #                 return True
        #     end_list.append(start)
        #
        # if go(0, nums[0]):
        #     return True
        # else:
        #     return False
        def per(start):
            for i in range(start-1, -1, -1):
                if i in end_list:
                    continue
                if i + nums[i] >= start:
                    if i == 0:
                        return True
                    if per(i):
                        return True
                end_list.append(i)
        if per(len_num-1):
            return True
        else:
            return False
    """
    Merge two sorted linked lists and return it as a new list. The new list should be made by          splicing together the nodes of the first two lists.
    """

    """
    You are given an array A of strings.
    Two strings S and T are special-equivalent if after any number of moves, S == T.
    A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].
    Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any    string not in S is not special-equivalent with any string in S.
    Return the number of groups of special-equivalent strings from A.
    """

    def numSpecialEquivGroups(self, A) -> int:
        for i in range(len(A)):
            A[i]

        pass
    '''
    Given a collection of intervals, merge all overlapping intervals.
    '''

    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result_list = []
        process_list = []
        # flag = False
        exit_flag = True
        while exit_flag:
            if len(intervals) == 1:
                break
            flag = False
            for i in range(len(intervals)):
                if intervals[i] in process_list:
                    continue
                for j in range(i+1, len(intervals)):
                    if intervals[i][0] <= intervals[j][0] <= intervals[i][1] or intervals[i][0] <= intervals[j][1] <= intervals[i][1]:
                        # print("pass card")
                        process_list.append(intervals[i])
                        process_list.append(intervals[j])
                        result_list.append([
                            min(intervals[i][0], intervals[j][0]),
                            max(intervals[j][1], intervals[i][1]),
                        ]
                        )
                        # print("hhshhshsh")
                        flag = True
                        break
                # print("flag", flag)
                if flag:
                    break
            else:
                # print("helloaaaa")
                exit_flag = False
            for i in intervals:
                if i not in process_list:
                    result_list.append(i)
            # print(result_list)
            intervals = result_list[:]
            result_list = []
            print(intervals, result_list)

        return intervals

    """
    排序数组
    """
    def sortArray(self, nums):
        if len(nums) < 2:
            return nums
        else:
            # 需要重复的过程
            mid = nums[0]
            left = [i for i in nums[1:] if i <= mid]
            right = [i for i in nums[1:] if i > mid]
        return self.sortArray(left) + [mid] + self.sortArray(right)


    """
     按奇偶排序数组，给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
    你可以返回满足此条件的任何数组作为答案。
    """

    def sortArrayByParity(self, A):
        result = []
        for i in A:
            if i % 2 == 0:
                result.insert(0, i)
            else:
                result.append(i)
        return result

    """
    给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
    对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
    你可以返回任何满足上述条件的数组作为答案。
    """

    def sortArrayByParityII(self, A):
        jishu = []
        oushu = []
        result = []
        for i in A:
            if i % 2 == 0:
                oushu.append(i)
            else:
                jishu.append(i)
        for i in range(len(A)):
            if i % 2 == 0:
                result.append(oushu.pop())
            else:
                result.append(jishu.pop())

        return result

    """
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    """

    def removeDuplicates(self, nums):
        remove = []
        for i in range(len(nums)):
            print(nums[:i], nums[i], nums[:i].count(nums[i]))
            if nums[:i].count(nums[i]) >= 2:
                remove.append(i)

        print(remove)
        for i in remove:
            nums.pop(i)
        print(nums)
        return len(nums)




if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,1,2,2,3]))