# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:14:27 2019

@author: marhc
"""
    
def paint(n, boards):
    if n == 1:
        print(boards)
        return max(boards)
    alist = []
    for i in range(1, len(boards) - (n - 1) + 1):
        alist.append(paint(1, boards[:i]) + paint(n - 1, boards[i:]))
    return min(alist)

print(paint(2, [60, 70, 10, 20, 40, 50, 10, 40]))