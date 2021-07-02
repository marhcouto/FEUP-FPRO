# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:39:59 2019

@author: marhc
"""

def multiples_of7(n):
    for x in range(n):
        if x % 7 == 0:
            yield x
            
print([x for x in multiples_of7(21)])