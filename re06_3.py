# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:37:59 2019

@author: marhc
"""

def local_minima(alist, n):
    list_mins = []
    for i in alist:
        print(i)
        min_interv = int(alist.index(i) - (n - 1) / 2)
        max_interv = int(alist.index(i) + (n - 1) / 2)
        if min_interv < 0:
            min_interv = 0
        if max_interv > len(alist) - 1:
            max_interv = len(alist) - 1
        list_piece = alist[min_interv : max_interv + 1]
        if i == min(list_piece):
            print(i)
            list_mins.append((i, alist.index(i)))
            print(list_mins)
    list_mins_2 = list_mins.copy()
    for k in list_mins:
        list_mins_2.remove(k)
        for m in list_mins_2:
            if k[0] == m[0]:
                list_mins.remove(m)
    return list_mins

print(local_minima([0, 3, 3, 14, 5, 7, 4], 3))   