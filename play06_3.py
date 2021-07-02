# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:27:49 2019

@author: marhc
"""

def rotate_list(l):
    new_l = []
    for i in range(len(l)):
        index = i + 3
        if index >= len(l):
            index = index % len(l)
        new_l.append(l[index])
    return new_l

print(rotate_list([1, 2, 3, 4, 5, 6]))