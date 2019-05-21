#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 21:23
# @Author  : AnNing
# @Site    : 
# @File    : Solution_0010#.py.py
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s or not p:
            return False
        dp = [[0 for _ in range(len(s))] for _ in range(len(p))]
        if p[0] == '.' or (p[0] == s[0]):
            dp[0][0] = True
        for 