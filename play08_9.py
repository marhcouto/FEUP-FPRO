# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:12:21 2019

@author: marhc
"""

import math
def size_n(n, size = 2):
    if abs(n // 10) < 10:
        return size
    else:
        return size_n(n // 10, size = size + 1)

def digits_average(n):
    if abs(n) < 10:
        return n
    else:
        size = size_n(n)
        if (size % 2) == 1:
            return math.ceil((digits_average(n // 10**(size // 2)) + digits_average(n % 10**((size // 2) + 1))) / 2)
        else:
            return math.ceil((digits_average(n // 10**(size // 2)) + digits_average(n % 10**(size // 2))) / 2)



print(digits_average(0))