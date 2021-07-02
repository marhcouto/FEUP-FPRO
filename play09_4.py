# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:20:56 2019

@author: marhc
"""
import functools 

def evaluate(a, x):
    return functools.reduce(lambda a, b: a + b, map(lambda b: x ** a.index(b) * b, a))