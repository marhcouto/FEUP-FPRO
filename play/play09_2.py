# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:11:33 2019

@author: marhc
"""

def to_fahrenheit(t):
    return list(map(lambda a: round((a * 1.8) + 32, 2), t))