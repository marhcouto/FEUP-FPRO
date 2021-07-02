# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:04:38 2019

@author: marhc
"""
def media (tuple1):
    soma = 0
    divisor = 0
    for i in tuple1[2]:
        soma += i
        divisor += 1
    av_final = soma / divisor
    return av_final

def name (tuple1):
    name1 = tuple1[0]
    return name1

def user(tuple1):
    user = tuple1[1]
    user1 = user[2:]
    int_user1 = int(user1)
    return int_user1

def sort_grades(records):
    rsort = sorted (records, key = user)
    rsort1 = sorted (rsort, key = name)
    rsort2 = sorted(rsort1, key = media, reverse = True)
    return rsort2
    

print(sort_grades((('Tate', 'up2011111', (50, 60, 40, 30, 80, 100)), ('Jarred', 'up2012112', (60, 45, 29, 31, 42, 81)), ('Ayan', 'up2011112', (59, 61, 71, 52, 37, 0)), ('James', 'up2012111', (60, 60, 60, 70, 55)), ('Tatiana', 'up2013000', (61, 62, 63, 64, 65, 66)), ('Jasper', 'up2013010', (50, 100, 100, 90, 0, 15)), ('Jarrod', 'up2011110', (10, 30, 50, 70, 90, 100)))))


#print(media(('João', 'up20186042', (90, 87, 90))))
