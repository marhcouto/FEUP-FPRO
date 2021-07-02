# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:02:08 2019

@author: marhc
"""
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alpb = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "s", "y", "z"]

def count_chars(astring):
    a = 0
    b = 0
    c = 0
    for i in astring:
        if i in digits:
            b += 1
        elif i in alpb:
            a += 1
        else:
            c += 1
    atup = (a, b, c)
    return atup

