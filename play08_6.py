# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:31:55 2019

@author: marhc
"""
def last_man_standing(alist, step):
    if len(alist) == 1:
        return alist[0]
    else:
        alist = alist[step % len(alist):] + alist[:step % len(alist)]
        del alist[-1]
        return last_man_standing(alist, step)
print(last_man_standing([6, 3, 8, 2, 1, 8, 5, 2, 2], 10))