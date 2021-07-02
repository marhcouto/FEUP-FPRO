# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:15:00 2019

@author: marhc
"""

def change(money):
    coins = {2.0:0, 1.0:0, 0.5:0, 0.2:0, 0.1:0, 0.05:0, 0.02:0, 0.01:0}
    values = sorted([x for x, value in coins.items()], reverse = True)
    for i in values:
        while money >= i:
            coins[i] += int(money // i)
            money = round(money % i, 2)
        print(money)
    return coins
print(change(7.71))