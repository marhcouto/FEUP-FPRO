# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 23:19:52 2019

@author: marhc
"""

import math

def comb(n, m):
    return math.factorial(n)/(math.factorial(m) * math.factorial(n - m))

def pascal(n):
    triangle = ""
    for i in range (0, n):
        line = ""
        for k in range (0, i + 1):
            line += str(int(comb(i, k))) + " "
        triangle += line[:len(line) -1] + "\n"
    return triangle
        
pascal(3)