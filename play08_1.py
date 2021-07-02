# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:18:55 2019

@author: marhc
"""

def gcd_rec(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd_rec(n2, n1 % n2)
print(gcd_rec(12, 14))