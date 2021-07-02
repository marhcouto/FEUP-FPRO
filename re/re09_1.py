# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:23:45 2019

@author: marhc
"""

def sort_by_f(alist):
    return sorted(alist, key = lambda x: 5-x if x >= 5 else x)

print(sort_by_f([-10, -6, 2, 5, 90]))