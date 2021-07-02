# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:21:21 2019

@author: marhc
"""

def comprehensions(i, j):
    alist = [x for x in range (i, j + 1) if x % 10 == 8 or x % 10 == 3]
    tup = tuple(round(x ** (1/2), 2) for x in range(i, j + 1))
    dic = {x:chr(x) for x in range(i, j + 1)}
    return(alist, tup, dic)

print(comprehensions(100, 102))