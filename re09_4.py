# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:12:49 2019

@author: marhc
"""

def override(l1, l2):
    forbidden = list(map(lambda a: a[0], l2))
    return sorted(l2 + list(filter(lambda a: a[0] not in forbidden, l1)))
    
print(override([('c', 'd'), ('c', 'e'), ('a', 'b'), ('a', 'd')], [('a', 'c'), ('b', 'd')]))