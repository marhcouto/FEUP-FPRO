# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:38:52 2019

@author: marhc
"""
def juggler(n,p):
    if p == 0:
        return n
    elif juggler(n,p-1) % 2 == 0:
        return int((juggler(n,p-1))**(1/2))
    elif juggler(n,p-1) % 2 == 1:
        return int((juggler(n,p-1))**(3/2))

print(juggler(3, 1))