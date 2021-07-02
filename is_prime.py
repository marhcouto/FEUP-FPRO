# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:08:54 2019

@author: marhc
"""

#def primes(n):
#    alist = []
#    for p in range(10, n - 1):
#        div = 0
#        for i in range(2, p - 1):
#            if p % i == 0:
#                div = 1
#        if div == 0:
#            alist.append(p)
#    return alist
#print(primes(10000))

def is_prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

print(is_prime(701))