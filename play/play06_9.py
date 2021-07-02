# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:44:31 2019

@author: marhc
"""

def pattern_hunting(l1, l2, p):
    alist = []
    for i in range(len(l1)):
        if p in l1[i] and p not in l2[i]:
            alist.append(l2[i])
        elif p not in l1[i] and p in l2[i]:
            alist.append(l1[i])
    return sorted(alist, reverse = True)
print(pattern_hunting(['a string', 'two strings', 'not here'], ['choose me', 'me too', 'but not me'], 'string'))