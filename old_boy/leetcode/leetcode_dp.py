# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class Solution:
    """
    Alice and Bob take turns playing a game, with Alice starting first.
    Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:
    Choosing any x with 0 < x < N and N % x == 0.
    Replacing the number N on the chalkboard with N - x.
    Also, if a player cannot make a move, they lose the game.
    Return True if and only if Alice wins the game, assuming both players play optimally.
    1 <= N <= 1000
    实质：数学问题，偶数的时候，Alice会赢
    dp:
        把所有的小于等于N的解都找出来，根据前面找后面的结果
        如果在0～N中找到可以整除的数字（Alice的答案） 在看剩下的这个数字是不是会输的情况，（这个应该是给Bob的），这种情况下就赢了
        因为是从小到大，所以不会遗漏中间的步骤(根据前面的更新后面的）
    """
    def divisorGame(self, n) -> bool:
        target = [0 for i in range(n + 1)]
        target[1] = 0
        if n <= 1:
            return False
        else:
            target[2] = 1
            for i in range(3, n+1):
                # 找约数
                for j in range(1, i//2):
                    if i % j == 0 and target[i-j] == 0:
                        target[i] = 1
                        break
        return target[n]


if __name__ == "__main__":
    s = Solution()
    print(s.divisorGame(1000))