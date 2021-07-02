# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:09:22 2019

@author: marhc
"""

def sparse_dot_product(dict1, dict2):
    result = 0
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if key1 == key2:
                result += (value1 * value2)
    return result
print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1}))