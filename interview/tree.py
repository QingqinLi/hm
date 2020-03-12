# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        # if (not t.left) and (not t.right):
        #     return
        # else:
        #     return t.val+"("+self.tree2str(t.left)+")"+"("+self.tree2str(t.right)+")"

        if not t:
            return ''
        left = '(' + self.tree2str(t.left) + ')' if (t.left or t.right) else ''
        right = '(' + self.tree2str(t.right) + ')' if t.right else ''
        return str(t.val) + left + right
