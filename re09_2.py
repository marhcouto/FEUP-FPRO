# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:31:13 2019

@author: marhc
"""
import functools

def map_reduce(n1, n2):
    alist = [x**2 for x in range (n1, n2) if x % 2 != 0]
    result1 = functools.reduce(lambda a, b: a * b if (a * b) < 50 else a + b, alist)
    return result1
print(map_reduce(0, 10))