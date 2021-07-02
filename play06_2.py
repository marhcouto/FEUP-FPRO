# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:24:13 2019

@author: marhc
"""

def nth_lowest(lnum, n):
    lnum.sort()
    return lnum[n - 1]