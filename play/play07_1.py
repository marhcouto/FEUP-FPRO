# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:51:40 2019

@author: marhc
"""

def academy_awards(alist):
    acad = {}
    for i in alist:
        acad[i[1]] = 0
    for i in alist:
        acad[i[1]] += 1
    return acad

print(academy_awards([('Best Picture', 'Moonlight'), ('Best Director', 'La La Land'), ('Best Actor', 'Manchester by the Sea'), ('Best Actress', 'La La Land'), ('Best Supporting Actor', 'Moonlight'), ('Best Supporting Actress', 'Fences'), ('Best Original Screenplay', 'Manchester by the Sea'), ('Best Original Score', 'La La Land')]	))