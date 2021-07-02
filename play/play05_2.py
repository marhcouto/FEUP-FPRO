# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:26:45 2019

@author: marhc
"""

def count_until(tup):
    count = 0
    for i in tup:
        if (str(type(i)))[8:11] == "tup":
            break
        count += 1
    if count == len(tup):
        count = -1
    return count

