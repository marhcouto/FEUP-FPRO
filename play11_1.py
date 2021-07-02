# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:50:58 2019

@author: marhc
"""

def bubble_sort(alist):
    stop = False
    while not stop:
        stop = True
        for i in range(len(alist) - 1):
            one = alist[i]
            two = alist[i + 1]
            if alist[i] > alist [i + 1]:
                alist[i + 1] = one
                alist[i] = two
                stop = False
    return alist
print(bubble_sort([5, 1, 2, 8, 2.5]))