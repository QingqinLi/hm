# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
class Solution:
    """
    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    """
    def isSymmetric(self, root):
        level = 0
        while root:
            l = root[2 ** (level-1) - 1, 2 ** level - 1]

