# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:08:54 2019

@author: marhc
"""

import math
def distance(f):
    if len(f) == 2:
        return math.sqrt((f[0][0] - f[1][0])**2 + (f[0][1] - f[1][1])**2)
    if len(f) == 1:
        return float("inf")
    L = f[:len(f)//2]
    R = f[len(f)//2::]

    dL = distance(L)
    dR = distance(R)
    dM = min(dR,dL)
    for i in L:
        for e in R:
            if (e[0] - i[0]) > dM:
                continue
            s =  math.sqrt((i[0] - e[0])2 + (i[1] - e[1])2)
            if s < dM:
                dM = s
    return dM


def closest_pair(points):
    points = sorted(points, key = lambda x: (x[0]))
    dM = distance(points)
    return round(dM)