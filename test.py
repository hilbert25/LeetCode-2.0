#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 21:08
# @Author  : AnNing
# @Site    : 
# @File    : test.py
#-+ab*cde
def level(s1,s2):
    dic = {'+':0,'-':0,'*':1,'/':1,'(':2,')':2}
    return cmp(dic[s1],dic[s2])
str = 'a+b*(c-d)-e/f'
symbol_stack = []
number_stack = []
symbol_set = set('+-*/()')
for i in range(len(str)-1,-1,-1):
    s = str[i]
    if s not in symbol_set:
        number_stack.append(s) # 如果是数字直接入number栈
    else:
        if (not symbol_stack) or symbol_stack[-1] == ')' or s == ')': # 如果栈顶是右括号或者symbol栈空或者s是右括号直接入symbol栈
            symbol_stack.append(s)
        elif s == '(':
            while symbol_stack and symbol_stack[-1] != ')':#symbol出栈到number中直到遇到右括号
                number_stack.append(symbol_stack[-1])
                symbol_stack.pop()
            symbol_stack.pop()
        else:#需要比较优先级
            while symbol_stack and level(symbol_stack[-1],s) > 0:
                number_stack.append(symbol_stack[-1])
                symbol_stack.pop()
            symbol_stack.append(s)
while symbol_stack:
    number_stack.append(symbol_stack[-1])
    symbol_stack.pop()
number_stack.reverse()
print number_stack


