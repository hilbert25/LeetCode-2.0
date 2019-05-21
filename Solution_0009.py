#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 21:00
# @Author  : AnNing
# @Site    : 
# @File    : Solution_0009.py
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            temp,y = 0, x
            while y > 0:
                temp = temp*10+y%10
                y/=10
        return x == temp