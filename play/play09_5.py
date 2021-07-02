# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:24:44 2019

@author: marhc
"""

def rearrange(l):
    return [x for x in l if x <= 0] + [x for x in l if x > 0]