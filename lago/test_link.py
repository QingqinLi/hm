# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class LinkNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    # 追加
    def append(self, data):
        item = self
        while item.next:
            item = item.next
        item.next = LinkNode(data)
        return self

    # 遍历链表
    def travel(self):
        item = self
        while item:
            print(item.data)
            item = item.next

    # 查找元素
    def search(self, data):
        item = self
        index = 0
        while item:
            if item.data == data:
                return index
            else:
                item = item.next
                index += 1
        else:
            return -1

    # 在特定的位置插入元素
    def insert(self, pos, data):
        item = self
        index = 0
        if pos == 0:
            node = LinkNode(data)
            item = node
            # node.next = item
        else:
            while item:
                if index == pos - 1:
                    node = LinkNode(data)
                    node.next = item.next.next
                    item.next = node
                    break
                else:
                    item = item.next
                    index += 1
        item.travel()


class TestLinkNode:

    def setup(self):
        self.link = LinkNode(0)
        self.link.append(1)
        self.link.append(2).append(3).append(4).append(5)
        # self.link.travel()

    def test_add(self):
        # 创建链表
        l = LinkNode(3)
        # 增加节点
        l.next = LinkNode(4)
        l.next.next = LinkNode(5)
        print(l.next.data)

    def test_append(self):
        l = LinkNode(0)
        l.next = LinkNode(1)
        l.next.next = LinkNode(2)
        l.append(6)
        print("data", l.next.next.next.data)

    def test_travel(self):
        l = LinkNode(0)
        l.append(1)
        l.append(2)
        l.append(6)
        l.append(90)
        l.travel()

    def test_search(self):
        self.setup()
        print(self.link.search(0))

    def test_insert(self):
        self.setup()
        self.link.insert(0, 999)


t = TestLinkNode()
t.test_insert()