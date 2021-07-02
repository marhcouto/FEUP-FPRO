# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:45:49 2019

@author: marhc
"""
import itertools
            
def budgeting(budget, products, wishlist):
    expense = [products[i] * wishlist[i] for i in wishlist]
    if sum(expense) <= budget:
        return wishlist
    desired = []
    for i in wishlist:
        while wishlist[i] > 0:
            desired.append(i)
            wishlist[i] -= 1
    combinations_0 = []
    for i in range(len(desired) + 1):
        combinations_0 += itertools.combinations(desired, i)
    best_price = 0
    for i in combinations_0:
        actual_price = sum([products[x] for x in i])
        if actual_price <= budget and budget - actual_price < budget - best_price:
            best_price = actual_price
            best_comb = i
    best_dic = {}
    for i in best_comb:
        if i in best_dic:
            best_dic[i] += 1
        else:
            best_dic[i] = 1
    return best_dic

print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 
                       'jacket': 40, 'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))