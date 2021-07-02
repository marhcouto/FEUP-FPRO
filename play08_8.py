# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:31:38 2019

@author: marhc
"""

def permutations(atuple):
    if len(atuple) == 1:
        return {atuple}
    if len(atuple) == 2:
        return {atuple, atuple[::-1]}
    elif len(atuple) >= 3:
        set1 = set(())
        for tup in permutations(atuple[:-1]):
            for i in range(len(tup) + 1):
                set1 = set1 | {tup[:i] + (atuple[-1],) + tup[i:]}
        return set1

print(permutations(('A', 'B', 'C', 'D')))