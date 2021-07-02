# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:27:26 2019

@author: marhc
"""

def to_celsius(t):
    return [round((x - 32) / 1.8, 1) for x in t]