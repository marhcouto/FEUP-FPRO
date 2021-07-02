# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:42:14 2019

@author: marhc
"""

def rearrange(l):
    return [x for x in l if x <= 0] + [x for x in l if x > 0]