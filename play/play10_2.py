# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:29:43 2019

@author: marhc
"""

def to_fahrenheit(t):
    return [round((x * 1.8) + 32, 2) for x in t]