# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head):
        result = []
        while head:
            result.append(str(head.val))
            head = head.next

        b = ''.join(result)
        return int(b, 2)

    """删除链表中的节点
    不是最后一个节点，后一个值赋值给这个点，后一个指针指向下下一个
    """

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    """反转链表
    建立三个变量， L， M，R互相赋值迭代，并建立指向关系，从而实现单链表的反转
    """

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        pre = None
        while cur.next:
            # 保存node
            lat = cur.next
            # 反转
            cur.next = pre
            pre = cur
            cur = lat
            # lat = cur.next
        cur.next = pre
        return cur

    """倒数第k个节点"""

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 先算出link的长度
        count = 0
        l = head
        while l.next:
            l = l.next
            count += 1
        count += 1
        my = count - k + 1
        print(my)
        m = 0
        while head.next:
            if m == my:
                return head
            else:
                m += 1

    """ 反转链表"""

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while cur.next:
            lat = cur.next
            cur.next = pre
            cur = lat
            pre = cur
        cur.next = pre
        return cur

    """返回倒数第k个节点的值"""

    def kthToLast(self, head: ListNode, k: int) -> int:
        count = 0
        cur = head
        while cur.next:
            count += 1
            cur = cur.next
        count += 1
        need = count - k + 1
        m = 1
        while head:
            if m == need:
                return head.val
            else:
                head = head.next
                m += 1
        return None






if __name__ == '__main__':
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(0)
    l.next.next = ListNode(1)
    l.next.next.next = ListNode(2)
    l.next.next.next.next = ListNode(3)
    print(s.reverseList(l))













