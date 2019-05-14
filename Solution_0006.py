#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 17:43
# @Author  : AnNing
# @Site    : 
# @File    : Solution_0006.py
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows >= len(s) or numRows == 1 :
            return s
        res = []
        k = (numRows-1) << 1
        for i in range(numRows):
            for j in range(0, len(s)/k+2):
                a = i+j*k
                b = a + (k - 2*i)
                if a < len(s):
                    res.append(s[a])
                if i != 0 and i != (numRows-1) and b < len(s):
                    res.append(s[b])
        return "".join(res)

s = Solution()
s.convert("PAYPALISHIRING",4)
