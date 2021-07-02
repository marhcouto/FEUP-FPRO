# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:56:08 2019

@author: marhc
"""

def subpatterns(astring):
    grow = 0
    shrink = 0
    for i in range(len(astring) - 1):
        for n in range(i, len(astring) - 1):
            for k in range(n, len(astring) - 1):
                if astring[i:n - 1] > astring[n:k - 1]:
                    grow += 1
                elif astring[i:n - 1] < astring[n:k - 1]:
                    shrink += 1
    print(grow)
    print(shrink)
    return abs(grow - (grow - shrink))
print(subpatterns('ceda'))