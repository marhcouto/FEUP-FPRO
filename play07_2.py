# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:45:02 2019

@author: marhc
"""

def lost_element(s1, s2):
    if len(s1) > len(s2):
        a = (s1 - s2)
    else:
        a = (s2 - s1)
    for i in a:
        return i

print(lost_element({1, 4, 5, 7, 9}, {9, 4, 5, 7}))