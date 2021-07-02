# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:44:20 2019

@author: marhc
"""

def solver(a, b, c):
    sol_list = []
    radical1 = -b
    radical2 = ((b ** 2) - (4 * a * c))**(1/2)
    divisor = 2 * a
    sol1 = (radical1 + radical2) / divisor
    sol2 = (radical1 - radical2) / divisor
    if radical2 == 0:
        sol_list += list (radical1 / divisor)
    if radical2 < 0:
        sol_list = []
    if radical2 > 0:
        if sol1 < sol2:
            sol_list += [sol1, sol2]
        else:
            sol_list += [sol2, sol1]
    return sol_list

print(solver(-2, -5, -3))