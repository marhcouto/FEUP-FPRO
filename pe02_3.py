# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:19:56 2019

@author: marhc
"""

def priority(tup):
    value = 0
    if tup[1] == 'grandparent':
        value = 1
    if tup[1] == 'cousin':
        value = 2
    if tup[1] == 'parent':
        value = 3
    if tup[1] == 'sibling':
        value = 4
    return (value, tup[0])


def genealogy(l):
    result_list = sorted(l, key = priority)
    return result_list
    
print(genealogy([('maria', 'parent'), ('matilde', 'grandparent'), ('geraldes', 'grandparent'), ('carlos', 'sibling'), ('paulo', 'sibling'), ('artur', 'grandparent'), ('pedro', 'parent'), ('alfredo', 'cousin'), ('carla', 'cousin')]))