# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:29:03 2019

@author: marhc
"""
def eu_dis(p1, p2):
    return round(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2), 3)

def x_dis(p1, p2):
    return p1[0] - p2[0] if p1[0] > p2[0] else p2[0] - p1[0]

def closest_pair(points):
    points.sort(key = lambda a: a[0])
    mid = len(points) // 2
    alist1 = points[:mid]
    alist2 = points[mid:]
    alist3 = []
    if len(points) == 4:
        dL = eu_dis(alist1[0], alist1[1])
        dR = eu_dis(alist2[0], alist2[1])
        dLR = min(dL, dR)
        if x_dis(points[1], points[2]) < dLR:
            dM = (eu_dis(points[1], points[2]))
        return round(min(dLR, dM))
                
    else:
        return min(closest_pair(alist1), closest_pair(alist2))
    

print(closest_pair([(2498, 7397), (2168, 8117), (2168, 6677), (1496, 1976), (8893, 9240), (288, 9467), (7465, 8080), (4588, 1774), (4178, 8118), (3459, 7224)]))