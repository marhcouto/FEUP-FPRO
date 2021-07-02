# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:13:11 2019

@author: marhc
"""

def treasure(clues):
    start = (0,0)
    while start in clues:
        coordinate = clues[start]
        clues.pop(start, None)
        start = coordinate
    return coordinate

print(treasure({(0, 0): (1, 0), (2, 1): (3, 5), (1, 0): (2, 1)}))