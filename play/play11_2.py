# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:01:32 2019

@author: marhc
"""

def bitonic_point(f):
    alist = f()
    while True:
        if len(alist) == 1:
            return alist[0]
        if len(alist) == 2:
            return max(alist)
        mid = len(alist) // 2
        if alist[mid + 1] < alist[mid]:
            alist = alist[:mid + 1]
        else:
            alist = alist[mid:]
        print(alist)

print(bitonic_point(lambda: [2, 6, 10, 25, 60, 30, 25, 10, 0]))