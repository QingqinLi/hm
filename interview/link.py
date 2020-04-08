# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""移除重复节点"""
def removeDuplicateNodes(self, head):
    result = []
    first = head
    while head:
        if head.val in result:
            head.next = head.next.next
        else:
            result.append(head.val)
        head = head.next
    return first
