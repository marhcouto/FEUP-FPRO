# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:57:28 2019

@author: marhc
"""

def invoice_totals(orders, min1):
    return list(map(lambda a: (a[0],a[2] * a[3] if a[2] * a[3] >= min1 else a[2] * a[3] + 10), orders))
print(invoice_totals([[34587, 'Always Look on the Bright, Eric Idle', 4, 40.95]], 0))