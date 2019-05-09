#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 23:48
# @Author  : AnNing
# @Site    : 
# @File    : Solutio_0002.py
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_0002(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1,node2,head = l1,l2,ListNode(0)
        add = 0
        root = head
        while node1 or node2:
            temp = ListNode(add)
            if node1:
                temp.val += node1.val
                node1 = node1.next
            if node2:
                temp.val += node2.val
                node2 = node2.next
            add = temp.val / 10
            temp.val %= 10
            root.next = temp
            root = root.next
        if add == 1:
            root.next = ListNode(1)
        return head.next

#注意头结点的使用，以及最后一次如果发生进位怎么做


