# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:47:17 2019

@author: marhc
"""

def budgetting(budget, products, wishlist):
    for product in wishlist:
        wishlist[products] *= products[product]
    expense = sum(wishlist.keys())
    if budget >= expense:
        return wishlist
    for i in wishlist:
        if i == min(wishlist.keys()) 