#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 21:34
# @Author  : AnNing
# @Site    : 
# @File    : Solution_0005.py
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        matrix = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # dp(i,j) = true if dp(i+1,j-1) and s[i] == s[j]  else false
        begin,end,maxLength = 0,0,1
        for i in range(len(s)):
            matrix[i][i] = True
        for i in range(0,len(s) - 1):
            matrix[i][i+1] = True if s[i] == s[i+1] else False
            if matrix[i][i+1]:
                begin,end,maxLength = i,i+1,2
        for i in range(2,len(s)):
            for j in range(0,len(s)-i):
                matrix[j][j+i] = True if matrix[j+1][j+i-1] and s[j] == s[j+i] else False
                if matrix[j][j+i] and i+1 > maxLength:
                    begin, end, maxLength = j,j+i,max(maxLength,i)
        return s[begin:end+1]
s = Solution()

print s.longestPalindrome("dgggj")