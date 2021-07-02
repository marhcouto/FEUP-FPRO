# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:45:13 2019

@author: marhc
"""

def odd_range(start, stop, step):
    alist = [x for x in range(start, stop) if x % 2 == 1]
    for x in range(0, len(alist), step):
        yield alist[x]
            
print(list(odd_range(0,20,2)))