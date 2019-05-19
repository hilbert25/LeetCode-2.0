#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 21:04
# @Author  : AnNing
# @Site    : 
# @File    : Solution_0008.py
# 画一个状态矩阵，注意正负号的处理
#0 只有空格
# 1 合法+数字
# 2 结束
#
# positive 记录正负
#    空格 正负号 其他符号  数字
# 0  0      1     2       1
# 1  2      2      2      1
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        positive = True
        matrix = [[0, 1, 2, 1], [2, 2, 2, 1]]
        num = 0
        status = 0
        for s in str:
            cur = 0
            if s == ' ':
                cur = 0
            elif s == '-':
                cur = 1
                if status == 0:
                    positive = False
            elif s == '+':
                cur = 1
            elif s.isdigit():
                cur = 3
                num = num*10 + int(s)
            else:
                cur = 2
            status = matrix[status][cur]
            if status == 2:
                break
        num = num if positive else -1*num
        return min(max(num, (-1*(1 << 31))), (1 << 31)-1 )