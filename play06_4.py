# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:33:43 2019

@author: marhc
"""

def bagdiff(xs, ys):
    while len(ys) > 0:
        stop = 1
        for i in xs:
            if i in ys:
                print(i)
                xs.remove(i)
                ys.remove(i)
                break
        for n in xs:
            if n in ys:
                stop = 0
        if stop == 1:
            break
    return xs
print(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]))