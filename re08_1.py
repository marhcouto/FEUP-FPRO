# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:42:35 2019

@author: marhc
"""

def flatten(alist):
    if alist == []:
        return alist
    if type(alist[0]) is list:
        return flatten(alist[0]) + flatten(alist[1:])
    else:
        return alist[:1] + flatten(alist[1:])
    
print(flatten(['Hello', [2, [[], False]], [True]]))