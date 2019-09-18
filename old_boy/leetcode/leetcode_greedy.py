# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class Solution:
    """
    Say you have an array for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    跌就买涨就卖，画图简单
    """
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                profit += prices[i+1] - prices[i]

        return profit

    """
    Given a string s and a string t, check if s is subsequence of t.
    You may assume that there is only lower case English letters in both s and t. t is potentially a very long 
    (length ~= 500,000) string, and s is a short string (<=100).
    A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) 
    of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence 
    of "abcde" while "aec" is not).
    暴力求解
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        begin = 0
        flag = True
        after = t
        for se in s:
            # 关键条件 从当前找到的点的下一个点开始查找
            after = after[begin:]
            for te in after:
                if se == te:
                    begin = after.index(te) + 1
                    break
            # 任意点找不到 程序异常，退出程序 返回结果
            else:
                flag = False
                break
        return flag

    """
    Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at 
    most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be 
    content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child 
    i will be content. Your goal is to maximize the number of your content children and output the maximum number.
    """

    def findContentChildren(self, g, s) -> int:
        count = 0
        g.sort()
        s.sort()
        for gi in g:
            for si in s:
                if si >= gi:
                    count += 1
                    s.remove(si)
                    break
        return count

    """
    A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

    -2: turn left 90 degrees
    -1: turn right 90 degrees
    1 <= x <= 9: move forward x units
    Some of the grid squares are obstacles. 
    The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
    If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)
    Return the square of the maximum Euclidean distance that the robot will be from the origin.
    能到的最远距离，一步一步走，看下一步是不是障碍物
    """

    def robotSim(self, commands, obstacles) -> int:
        # list不可hash，无法set，转换成tuple
        obstacles = (set(map(tuple, obstacles)))
        start_point = [0, 0]
        direction = {
            "north": {
                -1: "east",
                -2: "west",
            },
            "east": {
                -1: "south",
                -2: "north",
            },
            "west": {
                -1: "north",
                -2: "south",
            },
            "south": {
                -1: "west",
                -2: "east",
            }
        }
        direct = "north"
        result = []
        for i in commands:
            if i == -1 or i == -2:
                direct = direction[direct][i]
            elif 1 <= i <= 9:
                for j in range(i):
                    if direct == "north":
                        start_point[1] += 1
                        if tuple(start_point) in obstacles:
                            start_point[1] -= 1
                            break
                    elif direct == "south":
                        start_point[1] -= 1
                        if tuple(start_point) in obstacles:
                            start_point[1] += 1
                            break
                    elif direct == "east":
                        start_point[0] += 1
                        if tuple(start_point) in obstacles:
                            start_point[0] -= 1
                            break
                    elif direct == "west":
                        start_point[0] -= 1
                        if tuple(start_point) in obstacles:
                            start_point[0] += 1
                            break
            result.append(pow(start_point[0], 2) + pow(start_point[1], 2))
        return max(result)

    """
    There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
·   Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
    """

    def twoCitySchedCost(self, costs) -> int:
        count_a, count_b = len(costs) // 2, len(costs) // 2
        cost_value = []
        costs.sort(key=lambda x: x[0]+x[1], reverse=True)
        cost = []
        for i in costs:
            cost.extend(i)
        while cost:
            min_value = min(cost)
            min_index = cost.index(min_value)
            # print(min_index, min_value, cost, count_a, count_b)
            if count_a == 0:
                for m in range(len(cost)):
                    if m % 2 == 1:
                        cost_value.append(cost[m])
                break
            elif count_b == 0:
                for m in range(len(cost)):
                    if m % 2 == 0:
                        cost_value.append(cost[m])
                break
            else:
                if min_index % 2 == 0:
                    count_a -= 1
                    cost_value.append(min_value)
                    cost.pop(min_index)
                    cost.pop(min_index)
                else:
                    count_b -= 1
                    cost_value.append(min_value)
                    cost.pop(min_index - 1)
                    cost.pop(min_index - 1)
        return sum(cost_value)
        # print(cost, cost_value)


if __name__ == "__main__":
    s = Solution()
    print(s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))