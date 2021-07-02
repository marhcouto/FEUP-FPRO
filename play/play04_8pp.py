# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:21:41 2019

@author: marhc
"""

def greatest(num):
    list_num = [int(x) for x in str(num)]
    digit = 0
    final_num = 0
    for i in list_num:
        for n in list_num:
            digit = i * 10 ** (len(list_num) - 1)
            if i < n:
                i = n
                digit = i * 10 ** (len(list_num) - 1)
        final_num += digit
        del list_num[list_num.index(i)]
    return final_num

print(greatest(310909))