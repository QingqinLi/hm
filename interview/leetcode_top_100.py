# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""

import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    两数的和
    """

    def twoSum(self, nums, target):
        for i in range(len(nums)):
            another = target - nums[i]
            if another in nums[i + 1:]:
                index = nums.index(another, i + 1)
                return i, index

    """
    两数相加（链表）
    :循环链表取两个数，反转后求和，在反转，构造为链表，返回头节点
    """

    def addTwoNumbers(self, l1, l2):
        l1_list, l2_list = [], []
        while l1.next:
            l1_list.append(l1.val)
            l1 = l1.next
        l1_list.append(l1.val)
        l1_list.reverse()

        while l2.next:
            l2_list.append(l2.val)
            l2 = l2.next
        l2_list.append(l2.val)
        l2_list.reverse()

        num1 = int(''.join([str(i) for i in l1_list]))
        num2 = int(''.join([str(i) for i in l2_list]))
        num_result = num1 + num2
        result = str(num_result)[::-1]
        result_node = ListNode(result[0])
        first = result_node
        for i in range(1, len(result)):
            result_node.next = ListNode(result[i])
            result_node = result_node.next
        return first

    """
    反转字符串
    编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
    不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
    你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
    """

    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s) - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

    """
    反转字符串II
    给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。
    如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
    """

    def reverseStr(self, s: str, k: int) -> str:
        num = len(s) // (2 * k)
        result = []
        for i in range(num):
            l = list(s[i * 2 * k:(i + 1) * 2 * k])
            low = 0
            high = k - 1
            while low < high:
                l[low], l[high] = l[high], l[low]
                low += 1
                high -= 1
            result.extend(l)
        print("result", result)
        if len(s) - 2 * k * num > 0:

            l = list(s[-(len(s) - 2 * k * num):])
            print("1", l)
            low = 0
            if len(l) >= k:
                high = k - 1
            else:
                high = len(l) - 1
            while low < high:
                l[low], l[high] = l[high], l[low]
                low += 1
                high -= 1
            result.extend(l)
        elif len(s) - 2 * k * num < 0:
            print(2)
            l = list(s)
            low = 0
            if len(s) > k:
                high = k - 1
            else:
                high = len(s) - 1
            while low < high:
                l[low], l[high] = l[high], l[low]
                low += 1
                high -= 1
            result.extend(l)
        return ''.join(result)

    """
    判断是不是异位词
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    """

    def isAnagram(self, s: str, t: str) -> bool:
        # l = [0] * 26
        # for i in s:
        #     l[ord(i)-97] += 1
        # for i in t:
        #     l[ord(i)-97] -= 1
        # for i in l:
        #     if not i == 0:
        #         return False
        # return True
        d = {}
        for i in s:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        print(d)
        for i in t:
            if i in d.keys():
                d[i] -= 1
            else:
                return False
        print(d)
        for i in d.values():
            if not i == 0:
                return False
        return True

    """
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。
    """

    def isValid(self, s: str) -> bool:
        l = []
        d = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for i in s:
            if i in ['(', '[', '{']:
                l.append(i)
            else:
                if l:
                    if l[-1] == d[i]:
                        l.pop()
                    else:
                        return False
                else:
                    return False
        if not l:
            return True
        else:
            return False

    """
    温度升高的问题：
    根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
    例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
    提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

    递减栈，存储index和值， 一个按照index存贮结果的list， 栈顶是最大的元素，pop取消之前入栈的比较小的数字， 用index索引来计算结果
    优点：只需要对数据进行一次遍历，每个元素最多被压入或弹出堆栈一次，算法复杂度是o(n)
    """

    def dailyTemperatures(self, T):
        temperature_list = [[0, T[0]]]
        result_list = [0] * len(T)
        for i in range(1, len(T)):
            if temperature_list:
                if T[i] < temperature_list[-1][1]:
                    temperature_list.append([i, T[i]])
                else:
                    while temperature_list and T[i] > temperature_list[-1][1]:
                        result_list[temperature_list[-1][0]] = i - temperature_list[-1][0]
                        temperature_list.pop()
                    temperature_list.append([i, T[i]])
        return result_list

    """
    给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回滑动窗口中的最大值。
    """

    def maxSlidingWindow(self, nums, k):
        result_list = []
        max_num = max(nums[:k])
        for i in nums[k:]:
            if i > max_num:
                pass
        result_list.append(max_num)
        print(max_num)

    """
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
    注意你不能在买入股票前卖出股票。

    时间超限：尽量减少循环次数
    """

    def maxProfit(self, prices):
        # sub = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j]-prices[i] > 0 and prices[j]-prices[i] > sub:
        #             sub = prices[j]-prices[i]
        # return sub

        sub = 0
        if prices:
            min_num = prices[0]
            sub = 0
            for i in prices:
                if i < min_num:
                    min_num = i
                if i - min_num > sub:
                    sub = i - min_num

        return sub

    """
    请判断一个链表是否为回文链表。
    ''.join()不能是int类型的列表
    """

    def isPalindrome(self, head: ListNode) -> bool:
        start_list = []
        if not head:
            return True
        while head.next:
            start_list.append(head.val)
            head = head.next
        start_list.append(head.val)

        print(start_list)
        s2 = start_list[::-1]
        print(start_list, s2)
        if start_list == s2:
            return True
        return False

    """
    回文数
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    """

    def isPalindromeNum(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            l = []
            num = x
            while num > 0:
                l.append(num % 10)
                num = num // 10
            if l == l[::-1]:
                return True
        return False

    """
    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
    dict排序，items（） x:x[1]来排序
    不写items就是key排序
    """

    def topKFrequent(self, nums, k):
        nums_d = {}
        for i in nums:
            if i in nums_d.keys():
                nums_d[i] += 1
            else:
                nums_d[i] = 1

        print(nums_d)
        # result = sorted(nums_d.items(), key=lambda x: x[1], reverse=True)
        result = sorted(nums_d.keys(), key=lambda x: nums_d[x], reverse=True)
        return result[:k]

    """
    最长公共前缀
        编写一个函数来查找字符串数组中的最长公共前缀。
        如果不存在公共前缀，返回空字符串 ""。
    """

    def longestCommonPrefix(self, strs) -> str:
        if len(strs) < 2:
            if strs:
                return strs[0]
            else:
                return ""
        else:
            sub = strs[0]
            for i in strs[1:]:
                now = []
                len_ = len(sub) if len(sub) < len(i) else len(i)
                for j in range(len_):
                    if sub[j] == i[j]:
                        now.append(i[j])
                    else:
                        break
                sub = ''.join(now)
        return sub

    """
    链表的插入排序
    """

    def insertionSortList(self, head: ListNode) -> ListNode:
        result = head
        while head.next:
            while result:
                if result.val < head.next.val < result.next.val:
                    result.next.next = result.next
                    result.next = head
            head = head.next
        return

    """
    三数之和
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
    解法：双指针
    """

    def threeSum(self, nums):
        result = []
        result_set = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result_set.add({nums[i], nums[j], nums[k]})
                        result.append([nums[i], nums[j], nums[k]])

        return result, result_set

    """
    Z 字形变换
    将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
    比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
    解:
        将z字形转换为二位数组，初始化为0，按照规则填充，再读取，返回
      要考虑异常的情况  
    """

    def convert(self, s: str, numRows: int) -> str:
        # 二维数组行的长度
        if not s:
            return ''
        if numRows == 1:
            return s
        length = len(s) // (numRows - 2 + numRows) + 1
        conv_list = [[0 for i in range(length)] for i in range((numRows - 2 + numRows))]
        for i in range(len(s)):
            index_x = i % (numRows - 2 + numRows)
            index_y = i // (numRows - 2 + numRows)
            print(index_x, index_y)
            conv_list[index_x][index_y] = s[i]
        result_list = []
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                for j in range(length):
                    if not conv_list[i][j] == 0:
                        result_list.append(str(conv_list[i][j]))
            else:
                for j in range(length):
                    print()
                    if not conv_list[i][j] == 0:
                        result_list.append(str(conv_list[i][j]))
                    if not conv_list[(numRows - 2 + numRows) - i][j] == 0:
                        result_list.append(str(conv_list[(numRows - 2 + numRows) - i][j]))
        return ''.join(result_list)

    """
     寻找两个有序数组的中位数
     给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。
    """

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        pass

    """
    猜数字
    小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？
    """

    def game(self, guess, answer) -> int:
        count = 0
        for i in range(3):
            if guess[i] == answer[i]:
                count += 1
        return count

    """
    宝石与石头
     给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，
    你想知道你拥有的石头中有多少是宝石。
    J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
    """

    def numJewelsInStones(self, J: str, S: str) -> int:
        # count = 0
        # for i in S:
        #     if i in J:
        #         count += 1
        # return count
        return sum([S.count(i) for i in J])

    """
    ip地址无效化
    给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
    所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
    """

    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

    """
    删除链表中的节点
    请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
    """

    def deleteNode(self, head, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while head.next:
            if head.next.val == node:
                if head.next.next:
                    head.next = head.next.next
                    break
                else:
                    head.next = None
                    break

    """
    整数的个位积和之差
    """

    def subtractProductAndSum(self, n: int) -> int:
        l = []
        for i in str(n):
            l.append(int(i))
        s = sum(l)
        m = 1
        for i in l:
            m *= i
        print(l, s, m)
        return m - s

    """
    编写一个函数判断它是否是2的幂次方
    """

    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            s = n % 2
            if not s == 0:
                return False
            n = n // 2
        else:
            return True

    """
    位1的个数（汉明重量）无符号整数
    """

    def hammingWeight(self, n: int) -> int:
        # 现转换为二进制的格式
        n = bin(n)
        count = 0
        for i in n:
            if i == '1':
                count += 1
        return count

    """
    供暖器
    思路：找到每个房屋到加热器的最短距离
    二分查找
    """

    def findRadius(self, houses, heaters) -> int:
        # 二分查找，找到每个房屋到加热器的最短距离
        heaters = sorted(heaters)
        dis = []

        for house in houses:
            start = 0
            end = len(heaters) - 1
            while start < end:
                mid = start + (end - start) // 2
                if heaters[mid] < house:
                    start = mid + 1
                else:
                    end = mid

        pass

    """
    保持城市天际线
    """

    def maxIncreaseKeepingSkyline(self, grid) -> int:
        col = []
        s = 0
        for i in range(len(grid)):
            c = []
            for j in range(len(grid[0])):
                c.append(grid[j][i])
            col.append(max(c))
        for i in range(len(grid)):
            m = max(grid[i][:])
            for j in range(len(grid[0])):
                s += min(m, col[j]) - grid[i][j]
        return s

    """
    三锥形体的表面积
    考虑：凹陷的情况
    """

    def surfaceArea(self, grid) -> int:
        # b = pow(len(grid[0]), 2)
        # row = []
        # col = []
        # for i in range(len(grid)):
        #     row.append(max(grid[i]))
        # for i in range(len(grid)):
        #     m = []
        #     for j in range(len(grid[0])):
        #         m.append(grid[j][i])
        #     col.append(max(m))
        # n = sum(row)
        # l = sum(col)
        # print(l, b, n)
        # return 2*b + 2*n + 2*l
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += grid[i][j]
        print(5 * count)

    """
    第三大的数， 要求算法复杂度必须是O(n)
    python中无限小的数 float("-inf")
    """

    def thirdMax(self, nums) -> int:

        if len(nums) < 3:
            return max(nums)
        first = float("-inf")
        second = float("-inf")
        third = float("-inf")
        for i in nums:
            if i > first:
                first, second, third = i, first, second
            elif second < i < first:
                second, third = i, second
            elif third < i < second:
                third = i
            else:
                pass
        if third > float("-inf"):
            return third
        else:
            return first

    """
    验证回文字符串II
    字符串反转的方式：https://www.cnblogs.com/taceywong/p/8045127.html
    比较是否为回文串一般：
    """

    def validPalindrome(self, s: str) -> bool:
        sl = s[::-1]
        if s == sl:
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            if not s[i] == s[j]:
                print(i, j, s[i], s[j])
                # 比较去掉两边之后是不是回文串
                if i == 0:
                    s_old = s[1:]
                    s_new = s_old[::-1]
                    if s_new == s_old:
                        return True
                    else:
                        s_old = s[0:len(s) - 1]
                        s_new = s_old[::-1]
                        if s_new == s_old:
                            return True
                        else:
                            return False
                else:
                    s_old = s[0:i] + s[i + 1:]
                    print(s[0:i], s[i + 1])
                    s_new = s_old[::-1]
                    print(s_old, s_new)
                    if s_new == s_old:
                        return True
                    else:
                        s_old = s[0:j] + s[j + 1:]
                        s_new = s_old[::-1]
                        if s_new == s_old:
                            return True
                        else:
                            return False
            i += 1
            j -= 1
        return True

    """
    四位数组组成的最大时间
    """

    def largestTimeFromDigits(self, A) -> str:
        l = []
        if 2 in A:
            A.remove(2)
            if 3 in A:
                A.remove(3)
            elif 2 in A:
                A.remove(2)
            elif 1 in A:
                A.remove(1)
            elif 0 in A:
                A.remove(0)
            else:
                pass

    """
    统计位数为偶数的数字
    """

    def findNumbers(self, nums) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1

        return count

    """
    访问所有点的最小时间
    解答：走折线最快，先看两个点之间的距离（转换成长方形），走完之后剩下的走直线
    """

    def minTimeToVisitAllPoints(self, points) -> int:
        count = 0
        for i in range(len(points) - 1):
            start = points[i]
            end = points[i + 1]
            x = abs(start[0] - end[0])
            y = abs(start[1] - end[1])
            common = min(x, y)
            if x == y:
                big = 0
            else:
                big = max(x, y) - common
            count = count + common + big
        return count

    """
     螺旋矩阵 II
     螺旋矩阵的解法：

    """

    def generateMatrix(self, n: int):
        l = [[0 for j in range(n)] for i in range(n)]
        count = 1

        top = 0
        right = n - 1
        bottom = n - 1
        left = 0

        for i in range(4):
            if i == 0:
                # 第一行
                pass
        print(l)

    """
    和为零的N个唯一整数
    """

    def sumZero(self, n: int):
        l = []
        if n % 2 == 0:
            for i in range(1, n // 2 + 1):
                l.append(i)
                l.append(-i)
        else:
            for i in range(1, n // 2 + 1):
                l.append(i)
                l.append(-i)
            l.append(0)
        return l

    """
    奇数值单元格的数目
    """

    def oddCells(self, n: int, m: int, indices) -> int:
        l = [[0 for i in range(m)] for j in range(n)]
        for indice in indices:
            row = indice[0]
            for i in range(m):
                l[row][i] += 1
            col = indice[1]
            for j in range(n):
                l[j][col] += 1
        count = 0
        for i in range(n):
            for j in range(m):
                if not l[i][j] % 2 == 0:
                    count += 1

        return count

    """
    将每个元素替换为右侧最大元素
    将中间部分省略
    """

    def replaceElements(self, arr):
        result = []
        max_num = arr[0]
        for i in range(len(arr) - 1):
            if arr[i] >= max_num:
                max_n = max(arr[i + 1:])
                result.append(max_n)
                max_num = max_n
            else:
                result.append(max_num)
        result.append(-1)
        return result

    """
    翻转图像
    """

    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            A[i].reverse()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A

    """
    删除排序数组中的重复项
    设置快慢双指针
    """

    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        else:
            i, j = 0, 0
            count = 1
            while j < len(nums):
                if nums[i] >= nums[j]:
                    j += 1
                else:
                    nums[i + 1] = nums[j]
                    i += 1
                    j += 1
                    count += 1
        return count

    """
    高度检查器
    先排序，再和之前没有排序的数组进行比较
    """

    def heightChecker(self, heights) -> int:
        origin = heights[:]
        heights.sort()
        count = 0
        for i in range(len(origin)):
            if not origin[i] == heights[i]:
                count += 1
        return count

    """
    有序数组的平方
    """

    def sortedSquares(self, A):
        result = []
        for i in A:
            result.append(i * i)

        # 冒泡排序
        # for i in range(len(result)):
        #     for j in range(i, len(result)):
        #         if result[i] > result[j]:
        #             result[i], result[j] = result[j], result[i]

        # 快排
        def quicksort(nums, left, right):
            if left >= right:
                return
            ref = nums[left]
            start = left
            end = right
            while left < right:
                while left < right and nums[right] >= ref:
                    right -= 1
                nums[left], nums[right] = nums[right], nums[left]
                while left < right and nums[left] < ref:
                    left += 1
                nums[left], nums[right] = nums[right], nums[left]
            quicksort(nums, start, left - 1)
            quicksort(nums, left + 1, end)

        quicksort(result, 0, len(result) - 1)

        return result

    """
    数组拆分 I
    给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
    """

    def arrayPairSum(self, nums) -> int:
        nums.sort()
        result = []
        for i in range(0, len(nums), 2):
            result.append([nums[i], nums[i + 1]])
        count = 0
        for i in result:
            count += min(i)
        return count

    """
    可被 5 整除的二进制前缀
    python二进制转10进制， int("100100", 2)
    """

    def prefixesDivBy5(self, A):
        # mid = [str(A[0])]
        result = [int(str(A[0]), 2) % 5 == 0]
        num = str(A[0])
        for i in range(1, len(A)):
            num = num + str(A[i])
            result.append(int(num, 2) % 5 == 0)

        return result

    """
    转置矩阵
    """

    def transpose(self, A):
        n = len(A)
        m = len(A[0])
        result = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = A[j][i]
        return result

    """
    玩筹码
    """

    def minCostToMoveChips(self, chips) -> int:
        odd = 0
        even = 0
        for i in chips:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)

    """
    查找公共字符
    字符串转换为列表，使用for循环查看元素是不是在每一个list中for else
    """

    def commonChars(self, A):
        l = [list(s) for s in A]
        result = []
        for i in l[0]:
            for j in range(1, len(l)):
                if i not in l[j]:
                    break
                else:
                    l[j].remove(i)
            else:
                result.append(i)
        return result

    """
    分割平衡字符串
    """

    def balancedStringSplit(self, s: str) -> int:
        # count = 0
        # l = []
        # for i in s:
        #     l.append(i)
        #     if l and (l.count('L') == l.count('R')):
        #         l = []
        #         count +=1
        # return count
        l = 0
        count = 0
        for i in s:
            if i == 'L':
                l += 1
            else:
                l -= 1
            if l == 0:
                count += 1
        return count

    """
    转换成小写字母
    """

    def toLowerCase(self, str: str) -> str:
        s = list(str)
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                s[i] = chr(ord(s[i]) + 32)
        return "".join(s)

    """
    解码字母到整数映射,倒序查看元素是否为三位连在一起需要解析的
    """

    def freqAlphabets(self, s: str) -> str:
        d = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            '10#': 'j',
            '11#': 'k',
            '12#': 'l',
            '13#': 'm',
            '14#': 'n',
            '15#': 'o',
            '16#': 'p',
            '17#': 'q',
            '18#': 'r',
            '19#': 's',
            '20#': 't',
            '21#': 'u',
            '22#': 'v',
            '23#': 'w',
            '24#': 'x',
            '25#': 'y',
            '26#': 'z',
        }
        l = []
        result = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '#':
                l.append(s[i - 2:i + 1])
            elif i < len(s) - 1 and s[i + 1] == '#':
                pass
            elif i < len(s) - 2 and (s[i + 1] == '#' or s[i + 2] == '#'):
                pass
            else:
                # print("test", s[i], s[i + 1], s[i + 2])
                l.append(s[i])
        for i in l:
            result.append(d[i])
        print(result, l)
        return "".join(reversed(result))

    """
    斐波那契数
    """

    def fib(self, N: int):
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)

    """
    车的可用捕获量
    """

    def numRookCaptures(self, board) -> int:
        row = 0
        col = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    row = i
                    col = j
                    break
        count = 0
        print("row, col", row, col)
        for i in range(col - 1, -1, -1):
            print(row, i)
            if board[row][i] == 'B':
                break
            elif board[row][i] == 'p':
                count += 1
                break

        for i in range(col + 1, len(board[0])):
            print(row, i)
            if board[row][i] == 'B':
                break
            elif board[row][i] == 'p':
                count += 1
                break

        for i in range(row - 1, -1, -1):
            print(i, col, list(range(row - 1, -1, -1)), board[i][col])
            if board[i][col] == 'B':
                break
            elif board[i][col] == 'p':
                count += 1
                break

        for i in range(row + 1, len(board)):
            print(i, col)
            if board[i][col] == 'B':
                break
            elif board[i][col] == 'p':
                count += 1
                break

        return count

    """
    唯一摩尔斯密码词
    """

    def uniqueMorseRepresentations(self, words) -> int:
        moss_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                     "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        result = []
        for word in words:
            word_list = list(word)
            l = []
            for i in word_list:
                code = moss_code[ord(i) - 97]
                l.append(code)
            result.append(''.join(l))
        return len(set(result))

    """
    杨辉三角
    """

    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            l = [1, ]
            for j in range(len(result[-1]) - 1):
                l.append(result[-1][j] + result[-1][j + 1])
            l.append(1)
            result.append(l)
        return result

    """
     数组的相对排序
    """

    def relativeSortArray(self, arr1, arr2):
        result = []
        for i in arr2:
            while i in arr1:
                result.append(i)
                arr1.remove(i)
        arr1.sort()
        result.extend(arr1)
        return result

    """
    机器人能否返回原点
    """

    def judgeCircle(self, moves: str) -> bool:
        result_u = 0
        result_l = 0
        for i in list(moves):
            if i == 'R':
                result_l += 1
            elif i == 'L':
                result_l -= 1
            elif i == 'U':
                result_u += 1
            elif i == 'D':
                result_u -= 1
        if result_l == 0 and result_u == 0:
            return True
        else:
            return False

    """反转字符串中的单词 III"""

    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        word_reversed_list = []
        for i in word_list:
            reverse_word = i[::-1]
            word_reversed_list.append(reverse_word)
        return ' '.join(word_reversed_list)

    """快乐数"""

    def isHappy(self, n: int) -> bool:
        nums = [n, ]

        while 1:
            sum = 0
            for i in list(str(nums[-1])):
                num = int(i)
                sum += pow(num, 2)
            print(sum)
            if sum == 1:
                return True
            if sum in nums:
                return False
            else:
                nums.append(sum)

    """最小绝对差"""

    def minimumAbsDifference(self, arr):
        arr.sort()
        result = {}
        for i in range(len(arr) - 1):
            key = arr[i + 1] - arr[i]
            if key not in result.keys():
                result[key] = [[arr[i], arr[i + 1]], ]
            else:
                result[key].append([arr[i], arr[i + 1]])
        r = sorted(result.items(), key=lambda x: x[0])
        print(r)
        return r[0][1]

    """拼写单词"""

    def countCharacters(self, words, chars: str) -> int:
        result = []
        char_list = list(chars)
        for i in words:
            c = char_list[:]
            l = list(i)
            for j in l:
                if j in c:
                    c.remove(j)
                else:
                    break
            else:
                result.append(i)
        count = 0
        for i in result:
            count += len(i)
        return count

    """特殊等价字符串组"""

    def numSpecialEquivGroups(self, A):
        result = []
        for a in A:
            l = []
            r = []
            ll = list(a)
            for i in range(len(ll)):
                if i % 2 == 0:
                    r.append(ll[i])
                else:
                    l.append(ll[i])
            l.sort()
            r.sort()
            result.append([a, r, l])
        # print(result)
        already = []
        result_l = []
        for i in range(len(result)):
            if result[i][0] in already:
                continue
            rl = []
            rl.append(result[i][0])
            r = result[i][1]
            l = result[i][2]
            for j in range(i + 1, len(result)):
                if r == result[j][1] and l == result[j][2]:
                    rl.append(result[j][0])
                    already.append(result[j][0])

            result_l.append(rl)
        print(result_l)
        return len(result_l)

    """
    最长特殊序列I
    """

    def findLUSlength(self, a: str, b: str) -> int:
        if not len(a) == len(b):
            return max(len(a), len(b))
        else:
            if a == b:
                return -1
            else:
                return len(a)

    """
    独特的电子邮件地址
    """

    def numUniqueEmails(self, emails) -> int:
        result = []
        for email in emails:
            e = email.split("@")
            local = e[0]
            n = e[1]
            if "." in local:
                local = local.replace(".", "")
            if "+" in local:
                local = local.split("+")[0]
            if local + "@" + n not in result:
                result.append(local + "@" + n)
        return len(result)

    """
     比较字符串最小字母出现频次
     """

    def numSmallerByFrequency(self, queries, words):
        result = []

        def f(s):
            # n = []
            # for i in list(s):
            #     n.append(ord(i))
            # m = min(n)
            # return n.count(m)
            s = list(s)
            s.sort()
            count = 0
            for i in s:
                if i == s[0]:
                    count += 1
                else:
                    break
            return count

        w = []
        for i in words:
            w.append(f(i))
        w.sort(reverse=True)

        q = []
        for i in queries:
            q.append(f(i))
        for i in q:
            count = 0
            for j in w:
                if i < j:
                    count += 1
                else:
                    break
            result.append(count)
        return result

    """将整数转换为两个无零整数的和"""

    def getNoZeroIntegers(self, n: int):

        result = []
        for i in range(1, n):
            if '0' not in str(n - i) and '0' not in str(i):
                result.append(i)
                result.append(n - i)
                break
        return result

    """旋转数字"""

    def rotatedDigits(self, N: int) -> int:
        result = []
        for i in range(1, N + 1):
            l = list(str(i))
            if '3' in l or '4' in l or '7' in l:
                continue
            if '2' in l or '5' in l or '6' in l or '9' in l:
                result.append(i)
        return len(result)

    """山羊拉丁文"""

    def toGoatLatin(self, S: str) -> str:
        l = S.split(" ")
        for w in range(len(l)):
            if l[w][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                l[w] = l[w] + 'ma' + (w + 1) * 'a'
            else:
                l[w] = l[w][1:] + l[w][0] + 'ma' + (w + 1) * 'a'
        return ' '.join(l)

    """重塑矩阵"""

    def matrixReshape(self, nums, r: int, c: int):
        m = len(nums)
        n = len(nums[0])
        if not m * n == r * c:
            return nums
        else:
            l = []
            result = [[0 for i in range(c)] for j in range(r)]
            for i in range(m):
                for j in range(n):
                    l.append(nums[i][j])
            for i in range(r):
                for j in range(c):
                    result[i][j] = l[0]
                    l.pop(0)
            return result

    """实现strStr"""

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

    """27. 移除元素"""

    def removeElement(self, nums, val) -> int:
        last = len(nums) - 1
        start = 0
        count = 0
        while last > start:
            if nums[last] == val:
                last -= 1
                count += 1
                continue
            if nums[start] == val and not nums[last] == val:
                nums[start], nums[last] = nums[last], nums[start]
                last -= 1
                count += 1
            start += 1
        print(nums, len(nums) - count)

    """53. 最大子序和"""

    def maxSubArray(self, nums) -> int:
        result = []
        s = 0
        for i in range(len(nums) - 1):
            if nums[i] > 0:
                result.append(nums[i])

    """统计有序矩阵中的负数"""

    def countNegatives(self, grid) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    count += 1
        return count

    """打印从1到最大的n位数"""

    def printNumbers(self, n: int):
        if n <= 0:
            return [0]
        m = pow(10, n)
        result = []
        for i in range(1, m):
            result.append(i)
        return result

    """合并排序的数组"""

    def merge(self, A, m: int, B, n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        A[m:] = B
        low = 0
        high = m
        while low < m:
            print(low, high)
            if A[low] <= A[high]:
                low += 1
            else:
                A[low], A[high] = A[high], A[low]
                # low += 1
                # high += 1
        print(A)

    """替换空格"""

    def replaceSpace(self, s: str) -> str:
        s1 = s.replace(" ", "%20")
        return s1

    """ 剪绳子"""

    def cuttingRope(self, n: int) -> int:
        s = 1
        for i in range(2, n):
            pass

    """有多少小于当前数字的数字"""

    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)

        return result

    """左旋转字符串"""

    def reverseLeftWords(self, s: str, n: int) -> str:
        s1 = s[0:n]
        s2 = s[n:]
        return s2 + s1

    """腐烂的橘子"""

    def orangesRotting(self, grid) -> int:
        bad_guys = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    bad_guys.append([i, j])
        if len(bad_guys) == 0:
            return -1

        direction_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minute = 0
        visit = [[False] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(bad_guys)):
            visit[bad_guys[i][0]][bad_guys[i][1]] = True
        while True:
            new_bad_guys = []
            while bad_guys:
                guy = bad_guys.pop()
                for d in direction_list:
                    x = guy[0] + d[0]
                    y = guy[1] + d[1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and not visit[x][y]:
                        grid[x][y] = 2
                        print(x, y)
                        new_bad_guys.append([x, y])
            if new_bad_guys:
                bad_guys = new_bad_guys
                minute += 1
            else:
                break
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        else:
            return minute

    """把数字变成0的步骤"""

    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            count += 1
        return count

    """只出现一次的数字"""

    def singleNumber(self, nums) -> int:
        double_list = []
        pre_list = []
        for i in nums:
            if i in pre_list:
                double_list.append(i)
            if i not in pre_list:
                pre_list.append(i)
        result = set(nums) - set(double_list)
        print(double_list, list(result)[0])
        return list(result)[0]

    """缺失数字"""

    def missingNumber(self, nums) -> int:
        nums.sort()
        for i in range(len(nums)):
            if not nums[i] == i:
                return i

    """分糖果 II"""

    def distributeCandies(self, candies: int, num_people: int):
        result = [0 for i in range(num_people)]
        candy = 1
        while True:
            if candies > 0:
                # 该发出几个糖果了candy， 计算出应该给哪个小朋友了
                children = candy % num_people
                if children == 0:
                    children = num_people
                # 看剩下的糖果够不够
                if candies - candy > 0:
                    should_candy = candy
                else:
                    should_candy = candies
                result[children - 1] += should_candy
                candies -= should_candy
                candy += 1
            else:
                break
        return result

    """ 解压缩编码列表"""

    def decompressRLElist(self, nums):
        l = int(len(nums) / 2)
        result = []
        for i in range(l):
            new_number = nums[i * 2 + 1]
            new_len = nums[i * 2]
            new_need = [new_number for j in range(new_len)]
            result.extend(new_need)
        return result

    """字符串压缩"""

    def compressString(self, S: str) -> str:
        t = []
        for i in S:
            if t and not i == t[-1][0]:
                t.append([i, 1])
            elif t:
                t[-1][1] += 1
            else:
                t = [[i, 1]]
        result = []
        for i in t:
            i[1] = str(i[1])
            result.append(''.join(i))
        print(result)
        print(t)
        r = ''.join(result)
        if len(r) >= len(S):
            return S
        else:
            return r



class Codec:
    """
    TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
    它将返回一个简化的URL http://tinyurl.com/4e9iAk.
    要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，
    你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL
    """

    _map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """


if __name__ == '__main__':
    s = Solution()
    # s1 = ListNode(-129)
    # s1.next = ListNode(-129)
    # s2 = ListNode(5)
    # s2.next = ListNode(6)
    # s2.next.next = ListNode(4)
    # print(s.addTwoNumbers(s1, s2))
    print(s.compressString("aabcccccaaa"))