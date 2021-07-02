# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:31:05 2019

@author: marhc
"""

def bubble_sort(alist):
    DO = True
    while DO:
        DO = False
        for i in range(len(alist) - 1):
            if alist[i] > alist[i + 1]:
                dude = alist[i]
                dude1 = alist[i + 1]
                alist[i + 1] = dude
                alist[i] = dude1
                DO = True
    return alist
print(bubble_sort([5, 1, 2, 8, 2.5]))