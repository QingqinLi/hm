# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class Node:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next


def reverse_link(head):
    if head is None:
        return None
    # L,M,R互相赋值迭代，并建立指向关系，从而实现单链表的反转
    L, M, R = None, None, head
    while R.next is not None:
        L = M
        M = R
        R = R.next
        M.next = L
    R.next = M
    return R


"""
反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        L, M, R = None, None, head
        while R.next:
            L = M
            M = R
            R = R.next
            M.next = L

        R.next = M
        return R

    # 递归实现链表反转
    def reverseList2(self, head: ListNode) -> ListNode:
        """
        先找到链表的头节点（遍历到原链表的最后一个节点返回最后节点）
        执行函数体后续代码，将原链表的尾节点指向原尾节点的前置节点
        前置节点的指针指向None（防止出现死循环）
        返回新链表的头部节点到上一层函数，重复以上操作
        :param head:
        :return:
        """
        if not head:
            return
        if head.next is None:
            return head
        else:
            newhead = self.reverseList2(head.next)
            head.next.next = head
            head.next = None

        return newhead


if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    l = reverse_link(l1)
    print(l.val, l.next.val)
