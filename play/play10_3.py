# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:30:02 2019

@author: marhc
"""
def is_prime(n):
    return all([True if n % x != 0 else False for x in range(2, n)])
        
def get_composites(n):
    for x in range(4, n + 1):
        if not is_prime(x):
            yield x