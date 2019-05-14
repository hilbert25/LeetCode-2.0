#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 18:46
# @Author  : AnNing
# @Site    : 
# @File    : Solution_0007.py
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
        max_number = 1<<32 - 1
        min_number = -1*(1<<32)
        res = 0
        negitive = 1 if x > 0 else -1
        x = x if x > 0 else -x
        while x > 0:
            res = res * 10 + x%10
            x /= 10
            if (negitive == 1 and res > max_number) or (negitive == -1 and res < min_number):
                return 0
        return res if negitive == 1 else -res