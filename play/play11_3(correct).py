# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:17:00 2019

@author: marhc
"""

def count_zeros(f, count = 0):
    alist = f()
    upper = len(alist)
    lower = 0
    while True:
        mid = (upper + lower) // 2
        if alist[mid] == 0 and alist[mid - 1] == 1:
            return (len(alist) - mid)
        if alist[mid] == 0:
            upper = mid
        elif alist[mid] == 1:
            lower = mid
        
print(count_zeros(lambda: [1, 1, 1, 0, 0]))
print(count_zeros(lambda: [1]*80000000 + [0]*70000000))