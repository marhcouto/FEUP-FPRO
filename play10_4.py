# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:39:27 2019

@author: marhc
"""

def evaluate(a, x):
    return sum([x ** (a.index(i)) * i for i in a])