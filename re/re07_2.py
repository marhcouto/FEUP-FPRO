# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:20:11 2019

@author: marhc
"""
def hash_(a_int):
    result = 0
    string = str(a_int)
    for i in string:
        result += int(i)
    return result % 8

def collisions(alist):
    dict_1 = {}
    for i in alist:
        if hash_(i) in dict_1.keys():
            dict_1[hash_(i)] += 1
        else:
            dict_1[hash_(i)] = 1
    return dict_1

print(collisions([1, 789, 100, 9807, 1208, 92, 101]))