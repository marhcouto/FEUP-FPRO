# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:00:51 2019

@author: marhc
"""

def ugly(n):
    while n % 2 == 0:
        n /= 2
    while n % 3 == 0:
        n /= 3
    while n % 5 == 0:
        n /= 5
    return n == 1

print(ugly(14))