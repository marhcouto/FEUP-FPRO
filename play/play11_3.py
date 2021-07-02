# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:38:46 2019

@author: marhc
"""

def count_zeros(f):
    count = 0
    alist = f()
    while 0 in alist:
        mid = len(alist) // 2
        if alist[mid] == 0:
            count += (len(alist) - mid)
            alist = alist[:mid]
        else:
            alist = alist[mid:]
    return count

print(count_zeros(lambda: [1]*80000000 + [0]*50000000))
