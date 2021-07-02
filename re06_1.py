# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:52:02 2019

@author: marhc
"""

def jump(l):
    value = l[0]
    index = 0
    jump_0 = 0
    No_jumps = 0
    while value != -1:
        jump_0 = l[index]
        value = l[jump_0 % len(l)]
        index = l.index(value)
        No_jumps += 1
    return No_jumps
        
        
        

print(jump([8, 11, 6, 2, 7, 1, 4, -1, 10, -1, 3, 9]))