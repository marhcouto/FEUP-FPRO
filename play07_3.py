# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:52:02 2019

@author: marhc
"""
def most_frequent(alist):
    dic = {}
    prev = 0
    for i in alist:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for key, value in dic.items():
        if value > prev:
            prev = value
            prev_key = key
        if value == prev:
            prev_key = max((key, prev_key))
    return prev_key

print(most_frequent([-1, 2, 5, -1, 3, 3, 3, 4, 4, 2, 4, 5, -1, -1]))