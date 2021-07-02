# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:47:59 2020

@author: marhc
"""

def squareit(n):
    return n * n

def cubeit(n):
    return n*n*n

def main():
    anum = int(input("(1) Please enter a number: "))
    print(squareit(anum))
    print(cubeit(anum))

# inside this source or is it an import?

# call main() only if the Python interpreter is running this source file
