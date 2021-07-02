# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:43:46 2019

@author: marhc
"""

def fibonacci(n):
    fbn = ((1 + (5)**(1/2))**n - (1 - (5)**(1/2))**n)//((2**n) * (5)**(1/2))
    return fbn

ABCD = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def caesar(message):
    message_2 = ""
    char_1 = ""
    for indx, value in enumerate(message):
        for n in ABCD:
            new_indx = (ABCD.index(n) - int(fibonacci(indx))) % 26
            if value == n:
                char_1 = ABCD[new_indx]
                break
            else:
                char_1 = value
        message_2 += char_1
        char_1 = ""
    return message_2

print(caesar('HELLO WORLD!'))