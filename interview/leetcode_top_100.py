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
            if another in nums[i+1:]:
                index = nums.index(another, i+1)
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
        num = len(s) // (2*k)
        result = []
        for i in range(num):
            l = list(s[i*2*k:(i+1)*2*k])
            low = 0
            high = k-1
            while low < high:
                l[low], l[high] = l[high], l[low]
                low += 1
                high -= 1
            result.extend(l)
        print("result", result)
        if len(s) - 2*k*num > 0:

            l = list(s[-(len(s)-2*k*num):])
            print("1", l)
            low = 0
            if len(l) >= k:
                high = k-1
            else:
                high = len(l) - 1
            while low < high:
                l[low], l[high] = l[high], l[low]
                low += 1
                high -= 1
            result.extend(l)
        elif len(s) - 2*k*num < 0:
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
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
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
    根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
    例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
    提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
    
    递减栈，存储index和值， 一个按照index存贮结果的list， 栈顶是最大的元素，pop取消之前入栈的比较小的数字， 用index索引来计算结果
    优点：只需要对数据进行一次遍历，每个元素最多被压入或弹出堆栈一次，算法复杂度是o(n)
    """

    def dailyTemperatures(self, T):
        temperature_list = [[0, T[0]]]
        result_list = [0]*len(T)
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
    给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
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
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
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
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
    解法：双指针
    """

    def threeSum(self, nums):
        result = []
        result_set = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
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
        length = len(s)//(numRows-2+numRows) + 1
        conv_list = [[0 for i in range(length)] for i in range((numRows-2+numRows))]
        for i in range(len(s)):
            index_x = i % (numRows-2+numRows)
            index_y = i // (numRows-2+numRows)
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
                    if not conv_list[(numRows-2+numRows)-i][j] == 0:
                        result_list.append(str(conv_list[(numRows-2+numRows)-i][j]))
        return ''.join(result_list)

    """
     寻找两个有序数组的中位数
     给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。
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
     给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，
    你想知道你拥有的石头中有多少是宝石。
    J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
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
        return m-s

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


class Codec:
    """
    TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
    它将返回一个简化的URL http://tinyurl.com/4e9iAk.
    要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，
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
    print(s.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))