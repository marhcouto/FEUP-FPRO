# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:43:06 2019

@author: marhc
"""

def no_consecutives1(k, alist = [2, 3]):
    if len(alist) == k:
        return alist[0]
    else:
        alist.append(alist[-1] + alist[-2])
        return no_consecutives1(k)
print(no_consecutives1())
        
        
        
        
        
        
        
        
        
        
        
        