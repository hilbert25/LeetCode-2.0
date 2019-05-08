#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 0:16
# @Author  : AnNing
# @Site    : 
# @File    : Solution_0001.py
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for k, v in enumerate(nums):
            if target - v in dic:
                return dic[target - v], k
            dic[v] = k
# 采用enumerate记录位置索引，边走边记录