# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:43:08 2019

@author: marhc
"""

def square_odds(values):
    return ",".join([str(int(x) ** 2) for x in values if x != "," and int(x) % 2 == 1])

print(square_odds('1,2,3,4,5,6,7,8,9'))