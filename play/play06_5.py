# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:49:31 2019

@author: marhc
"""

def fetch_middle(llists):
    final_list = []
    for alist in llists:
        if len(alist) % 2 == 0:
            n = (alist[len(alist) // 2] + alist[(len(alist) // 2) - 1]) / 2
        else:
            n = alist[len(alist) // 2]
        final_list.append(n)
    return final_list