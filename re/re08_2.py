# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:25:12 2019

@author: marhc
"""

def calculator(expr):
    if type(expr) is not tuple:
        return expr
    if expr[1] == "+":
        return calculator(expr[0]) + calculator(expr[2])
    if expr[1] == "*":
        return calculator(expr[0]) * calculator(expr[2])
    if expr[1] == "-":
        return calculator(expr[0]) - calculator(expr[2])
        
print(calculator(((1, '+', 2), '*', 3)))