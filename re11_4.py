# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:03:17 2019

@author: marhc
"""

def bisect(f, n):
    lower = 0
    upper = 1
    for i in range(n):
        midpoint = (lower + upper) / 2
        if f(midpoint) == 0:
            return round(midpoint, 5)
        if f(lower) * f(midpoint) > 0:
            lower = midpoint
        else:
            upper = midpoint
    return round(midpoint, 5)
print(bisect(lambda x: (1-(x+0.2))*(x+0.2), 10))