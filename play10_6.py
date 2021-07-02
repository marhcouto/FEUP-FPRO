# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:42:24 2019

@author: marhc
"""
import statistics
def batch_norm(alist, batch_size):
    i = 0
    while i < len(alist):
        if i + batch_size >= len(alist):
            alist1 = alist[i:]
            yield [x - statistics.median(alist1) for x in alist1]
            i += batch_size
        else:
            alist1 = alist[i:i + batch_size]
            yield [x - statistics.median(alist1) for x in alist1]
            i += batch_size
print(list(batch_norm([-1, 0, 1, 1, 2, 4], 3)))