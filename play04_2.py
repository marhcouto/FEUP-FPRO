# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:40:38 2019

@author: marhc
"""

def dogs(h_age):
    d_age = 0
    if h_age <= 2:
        d_age += h_age * 10.5
    elif h_age > 2:
        d_age += (2 * 10.5) + (h_age * 4)
    return d_age


        