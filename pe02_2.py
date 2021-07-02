# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 16:01:16 2019

@author: marhc
"""

def greatest(num):
    final_num = ""
    list_num = [int(x) for x in str(num)]
    list_num_1 = list_num.copy()
    while len(final_num) < len(list_num):
        final_num += str(max(list_num_1))
        list_num_1.remove(max(list_num_1))
    return int(final_num)

print(greatest(310909))
