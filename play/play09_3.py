# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:15:22 2019

@author: marhc
"""
import functools

def map_filter_reduce(lst, f1, f2, f3):
    return functools.reduce(f3, map(f2, filter(f1, lst)))
    
    
print(map_filter_reduce([1, 2, 3, 4, 5, 6, 7, 8], lambda i: i % 2 == 0, lambda i: i**2, lambda a, b: a+b))