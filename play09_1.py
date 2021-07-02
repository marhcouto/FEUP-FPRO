# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:06:43 2019

@author: marhc
"""

def to_celsius(t):
    return list(map(lambda a: round((a - 32) / (1.8), 1), t))

print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]))