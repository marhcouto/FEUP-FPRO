# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:12:48 2019

@author: marhc
"""

def fib(n):
    alist = [0, 1]
    for i in range(2, n + 1):
        alist.append(alist[i - 1] + alist[i - 2])
    return alist