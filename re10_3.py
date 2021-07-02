# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:33:09 2019

@author: marhc
"""

def brute_force(f, l):
    return [x1 + x2 + x3 for x1 in l for x2 in l for x3 in l if f(x1 + x2 + x3)]

print(brute_force(lambda x: x in ('abc', 'bac', 'cab', 'cba'), ['a', 'b', 'c', 'd', 'e']))