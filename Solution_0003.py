#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 22:41
# @Author  : AnNing
# @Site    : 
# @File    : Solution_0003.py
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        begin,res = 0,0
        for i in range(len(s)):
            if s[i] not in dic or dic[s[i]] < begin:
                res = max(res,i-begin+1)
            else:
                res = max(res, i - dic[s[i]])
                begin = dic[s[i]] + 1
            dic[s[i]] = i
        return res