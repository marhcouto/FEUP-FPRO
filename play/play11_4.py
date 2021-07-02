# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:00:18 2019

@author: marhc
"""
from math import sqrt
def closest_pair(points):
    return calculate(sorted(points))

def calculate(alist, min_dist=9999999999):
    for x1, y1 in alist:
        for x2, y2 in alist:
            if abs(x2 - x1) < min_dist:
                dist = sqrt((x2-x1)**2 + (y2-y1)**2)
                min_dist = dist if (dist != 0 and dist < min_dist) else min_dist
    return round(min_dist)
















