# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:01:05 2019

@author: marhc
"""

def greatest(num):
    final_num = 0
    list_num = [int(x) for x in str(num)]
    while len(list_num) > 0:
        for i in list_num:
            if i == max(list_num):
                final_num += i * 10 ** (len(list_num) - 1)
                del list_num[list_num.index(i)]
                break
    return final_num
        