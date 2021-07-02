# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:42:39 2019

@author: marhc
"""

def days_until_empty(c, l):
    capacity = c
    i = 0
    while capacity > 0:
        capacity += l
        if capacity > c:
            capacity = c
        capacity -= i
        i += 1
    return i - 1
print(days_until_empty(100, 5))