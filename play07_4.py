# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:53:44 2019

@author: marhc
"""
def hexadecimal(num):
    NUMBER = []
    for n in num[1:]:
        if n == "F":
            NUMBER.append(15)
        elif n == "E":
            NUMBER.append(14)
        elif n == "D":
            NUMBER.append(13)
        elif n == "C":
            NUMBER.append(12)
        elif n == "B":
            NUMBER.append(11)
        elif n == "A":
            NUMBER.append(10)
        else:
            NUMBER.append(int(n))
    for i in range(len(NUMBER)):
        NUMBER[i] = NUMBER[i] * (16 ** (len(NUMBER) - i - 1))
    return sum(NUMBER)

def sort_by_value(dic):
    alist = [(a, b) for a, b in dic.items()]
    alist.sort(key = lambda x: hexadecimal(x[1]))
    return alist

print(sort_by_value({'Magenta': '#FF00FF', 'Red': '#FF0000', 'White': '#FFFFFF'}))