# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:00:07 2019

@author: marhc
"""

def find_me(f, limits):
    cycles = 0
    alist = [x for x in range(limits[0], limits[1])]
    while True:
        if f(alist[len(alist) // 2]) == 0:
            return cycles
        elif f(alist[len(alist) // 2]) == -1:
            alist = alist[:len(alist) // 2]
        elif f(alist[len(alist) // 2]) == 1:
            alist = alist[(len(alist) // 2):]
        cycles += 1
print(find_me(lambda n: 0 if n == 99 else 1, (0, 100)))