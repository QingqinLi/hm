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

    """
    链表的中间结点
    """

    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        mid = count // 2
        num = 0
        while num < mid:
            head = head.next
            num += 1
        return head

        # print(count, mid)

    """合并两个有序链表"""

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ll1 = []
        ll2 = []
        while l1:
            ll1.append(l1.val)
            l1 = l1.next
        while l2:
            ll2.append(l2.val)
            l2 = l2.next
        ll1.extend(ll2)
        ll1.sort()
        if not ll1:
            return None
        result = ListNode(ll1[0])
        m = result
        for i in range(1, len(ll1)):
            result.next = ListNode(ll1[i])
            result = result.next

        return m

    """相交链表"""

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        index_a = headA
        index_b = headB
        while index_a != index_b:
            index_a = index_a.next if index_a else headB
            index_b = index_b.next if index_b else headA
        return index_a

    """删除排序链表中的重复元素"""

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        l = []
        while head:
            l.append(head.val)
            head = head.next

        l = list(set(l))
        l.sort()
        result = ListNode(l[0])
        cur = result
        for i in range(1, len(l)):
            cur.next = ListNode(l[i])
            cur = cur.next
        return result

    """环形链表"""
    def hasCycle(self, head: ListNode) -> bool:
        pass

    """
     移除链表元素
     """

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pass


if __name__ == '__main__':
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(4)
    # l.next.next.next = ListNode(3)
    # l.next.next.next.next = ListNode(4)
    # l.next.next.next.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    # l2.next.next.next = ListNode(3)
    # l2.next.next.next.next = ListNode(4)
    # l2.next.next.next.next.next = ListNode(5)
    print(s.getIntersectionNode(l, l2))













