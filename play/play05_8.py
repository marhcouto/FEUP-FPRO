# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:06:15 2019

@author: marhc
"""

def score(n):
    result = 0
    if type(n) is tuple:
        for word in n:
            result += score(word)
    elif type(n) is str:
        for i in n:
            result += ord(i)
    return result


def greatest_member(atuple):
    result = ""
    for tuple_1 in atuple:
        if score(tuple_1) > score(result):
            result = tuple_1
    return result
        
