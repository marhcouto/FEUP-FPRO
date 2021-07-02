# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:37:55 2019

@author: marhc
"""

def last_man_standing(alist, step):
    i = 0
    while len(alist) > 1:
        i = (i + step - 1)
        if i >= len(alist):
            i = i% len(alist)
        print(i)
        print(alist[i], "gone")
        del alist[i]
    return alist[0]

print(last_man_standing([0.5, -2, 10, 5, 8.9, 10, 20, 10], 3))