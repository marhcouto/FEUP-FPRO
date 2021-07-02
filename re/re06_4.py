# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:31:22 2019

@author: marhc
"""

def mult(M,N):
    M_N = []
    if len(M) != len(N[0]):
        return M_N
    for row_M in M:
        row_M_N = []
        for i in range(len(N[0])):
            m_n = 0
            for index in range(len(row_M)):
                m_n += row_M[index] * (N[index])[i]
                print(m_n)
            row_M_N.append(m_n)
            print()
        M_N.append(row_M_N)
    return M_N

print(mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))