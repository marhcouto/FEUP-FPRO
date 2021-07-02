# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:46:24 2019

@author: marhc
"""

def groups(students):
    if len(students) < 3:
        return ()
    atuple = []
    for i in range(len(students) - 2):
        for n in range(i + 1,len(students) - 1):
            for k in range(n + 1, len(students)):
                atuple.append((students[i], students[n], students[k]))
    return tuple(atuple)
print(groups(('Bart', 'Homer', 'Marge', 'Lisa', 'Maggie')))