"""
Given a string, find the length of the longest substring without repeating characters.
考虑异常情况
考虑结束条件
enumerate:下标和元素
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len == 1:
            return 1
        elif s_len == 0:
            return 0
        max_length = 0
        for i in range(s_len):
            for j in range(i, s_len):
                if s[j] in s[i:j]:
                    if len(s[i:j]) > max_length:
                        max_length = len(s[i:j])
                    break
            else:
                if len(s[i:s_len]) > max_length:
                    max_length = len(s[i:s_len])
                    if max_length == s_len:
                        break
        # for i, v in enumerate(s):
        #     print(i,v)

        return max_length

    def lengthOfLongestSubstring1(self, s: str) -> int:
        s_len = len(s)
        if s_len == 1:
            return 1
        elif s_len == 0:
            return 0
        for i in range(0, s_len):
            len_new = s_len - i
            for j in range(i+1):
                new_str = s[j: j+len_new]
                # print(new_str, i, j+len_new)
                print("one")
                if len(set(new_str)) == len(new_str):
                    return len(new_str)

    """
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
    回文串
        穷举：
            切子串，看是不是回文，把当前最长的字符串记录，最后返回最长的 时间复杂度较高
            注意边界值
            range顾头不顾尾，需要特别注意
        ！！！可以使用动态规划（DP）算法
            p
        
            
    """
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        result = ''
        if(len(s)) == 1:
            return s
        for i in range(len(s)+1):
            for j in range(len(s)-i):
                sub_str = s[i:i+j+1]
                # 切片反转／列表的reverse方法 关于字符串反转：https://www.cnblogs.com/taceywong/p/8045127.html
                sub_str_rev = sub_str[::-1]
                if sub_str == sub_str_rev:
                    if len(sub_str) > max_length:
                        max_length = len(sub_str)
                        result = sub_str
        return result

    def longestPalindromedp(self, s: str) -> str:
        len_s = len(s)
        max_length = 0
        start = 0
        num_list = [[False for i in range(len_s)] for j in range(len_s)]
        if(len(s)) == 1:
            return s
        for i in range(len_s):
            for j in range(i+1):
                if s[i] == s[j]:
                    if i - j < 2:
                        num_list[j][i] = True
                    else:
                        num_list[j][i] = num_list[j+1][i-1]
                else:
                    num_list[j][i] = False
                if i-j+1 > max_length and num_list[j][i]:
                    max_length = i-j+1
                    start = j
        result = s[start:start+max_length]
        return result

    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
    zigzag conversion
    """

    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        else:
            result_list = []
            rows = numRows*2-2
            cols = len(s) // rows + 1
            # 二维数组初始化 防止浅拷贝造成的问题
            num_list = [['' for i in range(cols)] for j in range(rows)]
            for i in range(len(s)):
                col = i // rows
                row = i % rows
                num_list[row][col] = s[i]
            for i in range(len(num_list)):
                for j in range(len(num_list[i])):
                    # if num_list[i][j] != "0":
                    if i == 0 or i == numRows - 1:
                        # if num_list[i][j] != "0":
                        result_list.append(num_list[i][j])
                    elif i < numRows:
                        # if num_list[i][j] != "0":
                        result_list.append(num_list[i][j])
                        # if num_list[rows-i][j] != "0":
                        result_list.append(num_list[rows-i][j])

            result = "".join(result_list)
            return result

    """
    Implement atoi which converts a string to an integer.
    The function first discards as many whitespace characters as necessary until the first non-whitespace character is 
    found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many 
    numerical digits as possible, and interprets them as a numerical value. 
    The string can contain additional characters after those that form the integral number, which are ignored and have 
    no effect on the behavior of this function.
    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence 
    exists because either str is empty or it contains only whitespace characters, no conversion is performed.
    If no valid conversion could be performed, a zero value is returned.
    """
    def myAtoi(self, s: str) -> int:
        num_pre = s.strip()
        result = 0
        if len(num_pre) > 0:
            first = num_pre[0]
            result_list = []
            if first == '-':
                for i in num_pre[1:]:
                    if i.isdigit():
                        result_list.append(str(i))
                    else:
                        break
                if result_list:
                    result =int(''.join(result_list))*(-1)
            elif first == '+':
                for i in num_pre[1:]:
                    if i.isdigit():
                        result_list.append(str(i))
                    else:
                        break
                if result_list:
                    result = int(''.join(result_list))
            elif first.isdigit():
                for i in num_pre:
                    if i.isdigit():
                        result_list.append(str(i))
                    else:
                        break
                if result_list:
                    result = int(''.join(result_list))
            else:
                result = 0
            if result > pow(2, 31)-1:
                result = pow(2, 31)-1
            elif result < pow(2, 31)*(-1):
                result = pow(2, 31)*(-1)
        else:
            result = 0
        return result
    """
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
    """

    """
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
    """

    def isMatch(self, s: str, p: str) -> bool:
        list_s = list(s)
        # list_s.reverse()
        list_p = list(p)
        list_pp = []
        if len(list_p) == 0 and len(list_s) == 0:
            return True
        elif len(list_p) == 0:
            return False
        elif len(list_s) == 0:
            if list_p == ['*',]:
                return True
        if list_s[0] in list_p:
            list_p = list_p[list_p.index(list_s[0]):]
        else:
            list_p = list_p[:]
        for i in list_p:
            list_pp.append(i)

        for i in range(len(list_p)):
            print(list_p[i], list_s)
            if list_s:
                if list_p[i:] == ['*', '.']:
                    if len(list_s) > 1:
                        return True
                if list_p[i] == '.':
                    list_s.pop(0)
                elif list_p[i] == '*':
                    if i == len(list_p)-1:
                        return True

                    while (not i == len(list_p)-1) and list_s and list_p[i + 1] != list_s[0]:
                        # if list_p[i+1] == '.':
                        #     pass
                        list_s.pop(0)

                        # print("while", list_p[i], list_s)
                    else:
                        if i == len(list_p)-1:
                            # print("heer")
                            return True
                    while len(list_s) >= 2 and list_s[0] == list_s[1]:
                        # print("test")
                        list_s.pop(0)
                        # print("end", list_s)

                else:
                    if list_s and list_p[i] == list_s[0]:
                        list_s.pop(0)
                    else:
                        return False
                # print(list_s)
                list_pp.pop(0)

            else:
                break

        print("list_s", list_p, list_pp, list_s)

        if not list_s and not list_pp:
            return True
        else:
            return False
        # print(list_s)

    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    """

    def intToRoman(self, num: int) -> str:
        s_v = {
            0: ['I', 'V', 'X'],  # 1, 5, 10
            1: ['X', 'L', 'C'],  # 10, 50, 100
            2: ['C', 'D', 'M'],  # 100, 500, 1000
            3: ['M'],
               }
        result_list = []
        num_list = [int(i) for i in str(num)]
        num_list.reverse()
        for i in range(len(num_list)):
            num = num_list[i]
            s = s_v[i]
            if 0 < num <= 3:
                result_list.insert(0, s[0] * num)
            elif num == 4:
                result_list.insert(0, s[0]+s[1])
            elif num == 5:
                result_list.insert(0, s[1])
            elif 5 < num <= 8:
                result_list.insert(0, s[1]+s[0]*(num-5))
            elif num == 9:
                result_list.insert(0, s[0] + s[2])

        return ''.join(result_list)

    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    解题思路： list模拟栈的用法，进栈出栈来匹配
    """

    def isValid(self, s: str) -> bool:
        if not s:
            return True
        else:
            len_s = len(s)
            list_s = list(s)
            if len_s % 2 == 0:
                temp_list = []
                for i in list_s:
                    if i == '(' or i == '[' or i == '{':
                        temp_list.append(i)
                    elif i == ')':
                        if temp_list and temp_list[len(temp_list) - 1] == '(':
                            temp_list.pop(len(temp_list) - 1)
                        else:
                            return False
                    elif i == '}':
                        if temp_list and temp_list[len(temp_list) - 1] == '{':
                            temp_list.pop(len(temp_list) - 1)
                        else:
                            return False
                    elif i == ']':
                        if temp_list and temp_list[len(temp_list) - 1] == '[':
                            temp_list.pop(len(temp_list) - 1)
                        else:
                            return False

            else:
                return False
        if not temp_list:
            return True
        else:
            return False

    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    解题思路：递归， 结束条件：左右括号都用完的情况下
    """

    def generateParenthesis(self, n):
        resList = []

        def generate(left, right, res, n):
            if right == n:
                resList.append(res)
            else:
                if left < n:
                    generate(left+1, right, res+'(', n)
                if right < n and right < left:
                    generate(left, right+1, res+")", n)
        generate(0, 0, '', n)

        return resList

    """
    You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of
    substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
    全排列算法   暴力解法
    先找到长度为n*单个字段长度的子字符串，子字符串按照每个字符的长度分割为列表，查看目标列表中的每个值是都都在这个子字符串中（比较一个，弹出一个）
        避免重复字符串，注意输入为空的情况
    
    """

    def findSubstring(self, s: str, words):
        result = []
        result_list = []
        if not words:
            return []

        def perm(l, s, e):
            if s >= e:
                result.append(''.join([i for i in l]))  # 使用列表生成式，实现第一层的深拷贝 https://www.cnblogs.com/Black-rainbow/p/9577029.html
                # print(result)
            else:
                i = s
                for num in range(s, e):
                    l[i], l[num] = l[num], l[i]
                    perm(l, s+1, e)
                    l[i], l[num] = l[num], l[i]

        perm(words, 0, len(words))
        result = list(set(result))
        print(result)
        for i in result:
            if i in s:
                print(s, i)
                count = s.count(i)
                print(count)
                if count == 1:
                    result_list.append(s.index(i))
                else:
                    s1 = s
                    count_now = count
                    index = 0
                    while count_now:
                        result_list.append(s1.index(i, index))
                        index = len(words) * (count - count_now + 1) + s1.index(i)
                        count_now -= 1

        return list(set(result_list))

    def findSubstring2(self, s: str, words):
        """
        找长度为n*length的子串，看是不是包含了全部的list中的值

        :param s:
        :param words:
        :return:
        """
        def split_n(s, n):
            l = []
            while s:
                l.append(s[0:n])
                s = s[n:]
            return l

        if s == '' or words == []:
            return []
        need_length = len(words) * len(words[0])
        print(need_length)
        ll = {}
        result = []
        for i in range(len(s) - need_length + 1):
            ll[i] = s[i:i+need_length]
        for i in ll:
            res_l = split_n(ll[i], len(words[0]))
            print(res_l)
            for j in words:
                if j not in res_l:
                    break
                else:
                    res_l.remove(j)
            else:
                result.append(i)
        print(ll, result)
        return result


    """
    Given a string containing just the characters '(' and ')', 
    find the length of the longest valid (well-formed) parentheses substring.
    使用列表模拟栈，匹配则出栈,未匹配到则重新开始计数， 列表嵌套标记字符是否匹配到数据
    """

    def longestValidParentheses(self, s: str) -> int:
        all_list = []
        left_list = []
        for i in range(len(s)):
            if s[i] == '(':
                left_list.append([i, 1])
            else:
                if left_list:
                    end = len(left_list) - 1
                    while left_list[end][1] == 0:
                        if end == 0:
                            all_list.append(left_list)
                            left_list = []
                            break
                        end -= 1
                    else:
                        left_list[end][1] = 0
        all_list.append(left_list)

        m = 0
        for left in all_list:
            count = 0
            for i in left:
                if i[1] == 0:
                    count += 1
                else:
                    if count > m:
                        m = count
                    count = 0
            if count > m:
                m = count
        return m*2

    """
    The count-and-say sequence is the sequence of integers with the first five terms as following:
    """
    def countAndSay(self, n: int) -> str:
        # result_dict ={1: "1"}
        result_list = ["1", "11"]
        for i in range(1, n-1):
            last_data = result_list[len(result_list)-1]
            s = ""
            count = 1
            for j in range(1, len(last_data)):
                # item = last_data[j-1]
                if last_data[j] == last_data[j-1]:
                    count += 1
                else:
                    s += str(count)
                    s += last_data[j-1]
                    count = 1
                if j == len(last_data) - 1:
                    s += str(count)
                    s += last_data[j]

            result_list.append(s)
        return result_list[n-1]

    """
    Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]".
    """

    def defangIPaddr(self, address: str) -> str:

        return address.replace(".", "[.]")

    """
    You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.
    You are also given an integer maxCost.
    Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.
    If there is no substring from s that can be changed to its corresponding substring from t, return 0.
    """

    def equalSubstring(self, s: str, t: str, cost) -> int:
        sum_list = []
        sub_list = []
        for i in range(0, len(s)):
            sub = abs(ord(t[i]) - ord(s[i]))
            sub_list.append(sub)
        flag = True
        for i in range(0, len(sub_list)):
            for j in range(i, len(sub_list)):
                if sum_list and max(sum_list) > len(sub_list)-i:
                    flag = False
                    break

                if sum(sub_list[i:j + 1]) > cost:
                    if j >= i:
                        sum_list.append(j - i)
                    break
            else:
                if sum(sub_list[i:]) <= cost:
                    sum_list.append(len(sub_list) - i)
            if not flag:
                break
        return max(sum_list) if sum_list else 0
    """
    Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.
    We repeatedly make k duplicate removals on s until we no longer can.
    Return the final string after all such duplicate removals have been made.
    It is guaranteed that the answer is unique.
    避免无用操作浪费时间 ：
        找到耗时最长的操作，尽量减少重复此操作，优化耗时操作，避免循环嵌套循环
    """

    def removeDuplicates(self, s: str, k: int) -> str:
        while 1:
            sub_k = []
            i = 0
            while 1:
                if i > len(s)-k:
                    break
                if s[i] == s[i+k-1]:
                    if len(set(list(s[i:i+k]))) == 1:
                        sub_k.append(s[i])
                        i += k
                    else:
                        i += 1
                else:
                     i += 1
            if sub_k:
                for i in sub_k:
                    new_s = s.replace(i*k, "")
                    s = new_s
            else:
                break
        return s

    """
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, als
    represented as a string.
    """

    def multiply(self, num1: str, num2: str) -> str:
        result_list = [0]*(len(num1)+len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                mid = int(num1[i]) * int(num2[j])
                print(mid, result_list)
                if mid > 9:
                    result_list[len(result_list) - 1 - i - j] += mid - 10
                    result_list[len(result_list) - 2 - i - j] += 1
                else:
                    result_list[len(result_list) - 1 - i - j] += mid
        result = []
        for i in result_list:
            if i == 0:
                continue
            else:
                result.append(str(i))

            # print(mid)
        s = ''.join(reversed(result))
        return s


if __name__ == '__main__':
    s = Solution()
    # for i in range(10):
    #     print(i)
    #     i = 5

    print(s.multiply('123', '456'))
