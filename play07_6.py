# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:10:14 2019

@author: marhc
"""

def fight(heroes, villain):
    for i in heroes:
        if i["category"] != villain["category"]:
            continue
        if i["health"] >= villain["health"]:
            return (i["name"] + " defeated the villain and now has a score of " + str(i["score"] + 1))
        if i["health"] < villain["health"]:
            villain["health"] -= (i["health"] / 2)
    return (villain["name"] + " prevailed with " + str(villain["health"]) + "HP left")

print(fight([{'name': 'Genos', 'health': 3000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}, {'name': 'King', 'health': 3750, 'category': 'S', 'score': 1}], {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}))      