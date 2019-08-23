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


s = Solution()
print(s.myAtoi("42"))
# array = [[1,2,3],[4,5,6]]
# print(array[0][1])
