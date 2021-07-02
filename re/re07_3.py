# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:32:29 2019

@author: marhc
"""

def roman_to_integer(astring):
    result = 0
    list1 = list(astring)
    dict_roman = {"I":1, "V":5, "X":10, "C":100, "L":50, "D":500, "M":1000}
    while len(list1) > 0:
        i = list1[0]
        if len(list1) > 1:
            n = list1[1]
            if dict_roman[i] < dict_roman[n]:
                result += (dict_roman[n] - dict_roman[i])
                list1.remove(i)
                list1.remove(n)
            else:
                result += dict_roman[i]
                list1.remove(i)
        else:
            result += dict_roman[i]
            list1.remove(i)
    return result

print(roman_to_integer('LXXXIV'))