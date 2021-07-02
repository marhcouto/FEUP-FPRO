# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:18:26 2019

@author: marhc
"""
def transposed(mx):
    mx2 = []
    for i in range(len(mx)):
        mx3 = []
        for n in range(len(mx)):
            mx3.append(mx[n][i])  
        mx2.append(mx3)
    return mx2


def mult(m, j):
    mj2 = []
    for i in range(len(m)):
        mj = []
        for n in range(len(m[i])):
            a = 0
            for l in range(len(m)):
                a += m[i][l] * j[l][n]
                print(a)
            mj.append(a)
        mj2.append(mj)
    return mj2


def is_orthogonal(mx):
    mxt = transposed(mx)
    I = mult(mx, mxt)
    answer = 0
    for i in range(len(I)):
        if I[i][i] == 1:
            for n in range(len(I)):
                if (I[i][n] == 0 and I[n][i] == 0) or n == i:
                    answer = 1
    if answer == 1:
        return True
    else:
        return False

print(is_orthogonal([[-1, 0], [0, 1]]))

